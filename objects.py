import nameparser

import settings
import string
from thefuzz import fuzz
import settings
from unidecode import unidecode
import itertools
import string
import constants
import re
import utils
from utils import conform_name, InvalidNameException




class PersonName (object):
    """
        uses python-nameparser (https://github.com/derek73/python-nameparser) to deal with complexity of
        compound titles and family name prefixs which are often entered to incorrect fields

        full name shold be name as a string in signature format:
        (title or prenominal + given_name + middle name or middle initial + familyname + suffix or postnominal)

        - each element is optional but len(full_name) nust be gt 0.
        - do not add or modify puctuation 
        - characters in parenthisis, brackets and brace will be ignored for now 
    """

    def __init__(self, full_name, encoding="utf-8"):
        self.ENCODING = encoding
        self._members = [ "human_name", "name_provided", "conformed_given_name", "conformed_family_name"
            , "conformed_middle_name", "conformed_middle_initial", "conformed_given_initial"
            ,  ] #'issues', 'transfomations']

        self.human_name = nameparser.HumanName(full_name, encoding=encoding)
        self.name_provided = full_name
        self.conformed_given_name = conform_name(self.human_name.first)
        self.conformed_family_name = conform_name(self.human_name.last)
        self.conformed_middle_name = conform_name(self.human_name.middle or '')
        self.conformed_middle_initial = self.conformed_middle_name[0] if len(self.conformed_middle_name) > 0 else ''
        self.conformed_given_initial = self.conformed_given_name[0] if len(self.conformed_given_name) > 0 else ''


    def p_match_given_names(self):
        given_name = conform_name(self.human_name.first)
        names = [given_name, ]
        for name_set in constants.FIRST_NAME_PLESIONYMS:
            if given_name in name_set:
                names = [n for n in name_set]
                break
        return tuple(set(names))


    def p_match_family_names(self):
        family_name = conform_name(self.human_name.last) # deal with variations eg 'DelaCruz' and 'de la Cruz'
        names = [family_name, ]
        for name_set in constants.FAMILY_NAME_PREFIX_PLESIONYMS:
            if family_name.startswith(name_set):
                for n in tuple(sorted(name_set, key=len, reverse=True)): # sort to hit the best match first
                    if family_name.startswith(n): #two loops suck, but need to find the match before the replace
                        pfix = n
                        break

                for n in name_set:
                    if family_name.startswith(n) and n != pfix and not n in names:
                        names.append(family_name.replace(pfix, n, 1))
        return tuple(names)


    def p_match_middle_names(self):
        middle_name = conform_name(self.human_name.middle)
        names = [middle_name, ]
        for name_set in constants.FIRST_NAME_PLESIONYMS:
            if middle_name in name_set:
                names = [n for n in name_set]
                break
        return tuple(set(names))

    def match(self
              , match_name
              , ignore_middle_name=False
              , match_given_name_as_intial=False
              , match_middle_name_as_initial=True
              , fuzzy_ratio_threshold=80):
        """
        :param match_name: PersonName object to compare to
        :type match_name: PersonName
        :param ignore_middle_name: compare middle name (if avaialble in both names)
        :type ignore_middle_name: bool (default False)
        :param match_given_name_as_intial: compare initial for given name (J Baird == Joe Baird)
        :type match_given_name_as_intial: bool (default False)
        :param match_middle_name_as_initial: compare initial for middle name (Joe B Baird == Joe Bedent Baird)
        :type match_middle_name_as_initial: bool default True)
        :param fuzzy_ratio_threshold: "distance" score between names calculated as 100 exact match
        :type fuzzy_ratio_threshold: int 0-99
        :return:
        :rtype:
        """

        # collect permutatuions of self.name in list
        # TODO: determine if we want to further use title and suffix (currently only used in determining name parts
        names_to_test = []

        if not self.conformed_family_name or not match_name.conformed_family_name:
            raise InvalidNameException(
                [self.name_provided, match_name.name_provided]
                , message="could not parse family name"
                )

        min = constants.ONE_CHAR if match_given_name_as_intial else constants.TWO_CHAR
        if len(self.conformed_given_name) < min or len(self.conformed_given_name) < min:
            raise InvalidNameException(
                [self.name_provided, match_name.name_provided]
                , message="could not parse given name"
                ) #f"could not parse given name{ 'or intial' if match_given_name_as_intial else ''}")

        # stage family names
        family_names = self.p_match_family_names()
        family_name_to_match = match_name.conformed_family_name

        # stage given names
        if not match_given_name_as_intial:
            given_names = self.p_match_given_names()
            given_name_to_match = match_name.conformed_given_name
        else:
            given_names = tuple([n[0] for n in self.p_match_given_names()])
            given_name_to_match = match_name.conformed_given_initial

        # stage middle names if needed
        if ignore_middle_name  or match_name.conformed_middle_name == "":
            middle_names = ("", )
            middle_name_to_match = ""
        else:
            if not match_middle_name_as_initial:
                middle_names = self.p_match_middle_names ()
                middle_name_to_match = match_name.conformed_middle_name
            else:
                print (self.p_match_middle_names())
                middle_names = tuple([(n+' ')[0] for n in self.p_match_middle_names ()])
                middle_name_to_match = match_name.conformed_middle_initial

        name_to_match = re.sub(' +', ' ',given_name_to_match + ' ' + middle_name_to_match + ' ' + family_name_to_match)
        names_to_test= [re.sub(' +', ' ', n[0] + ' ' + n[1] + ' ' + n[2])
                        for n in itertools.product(given_names, middle_names, family_names)]

        best_score = 0
        for n in names_to_test:
            score = max(
                fuzz.token_sort_ratio(n, name_to_match)
                , fuzz.ratio(n, name_to_match)
                , fuzz.partial_ratio(n, name_to_match)
                )
            print(n, name_to_match,score)
            if score > best_score:
                best_score = score
                
            if score == 100:
                break

        # # deal with names where first and last transposed (typically japanese names, yoko ono is really ono yono)
        if not best_score >= fuzzy_ratio_threshold \
                and self.conformed_family_name == family_name_to_match \
                and self.conformed_given_name == given_name_to_match:
            best_score = 99


        # deal with compound initials (eg 'JD', 'BJ')
        if not best_score >= fuzzy_ratio_threshold \
            and (len(given_name_to_match) == 2 or len(self.conformed_given_name)==2):
            if self.conformed_given_initial + self.conformed_middle_initial ==given_name_to_match \
                    or given_name_to_match[0] + (middle_name_to_match + '')[0] == self.conformed_given_name :
                best_score = 99


        return (best_score >= fuzzy_ratio_threshold, best_score)
        


    # def match_old(self
    #           , match_name
    #           , ignore_middle_name=False
    #           , match_given_name_as_intial=False
    #           , match_middle_name_as_initial=True
    #           , fuzzy_ratio_threshold=40):
    #     """
    #     :param match_name: PersonName object to compare to
    #     :type match_name: PersonName
    #     :param ignore_middle_name: compare middle name (if avaialble in both names)
    #     :type ignore_middle_name: bool (default False)
    #     :param match_given_name_as_intial: compare initial for given name (J Baird == Joe Baird)
    #     :type match_given_name_as_intial: bool (default False)
    #     :param match_middle_name_as_initial: compare initial for middle name (Joe B Baird == Joe Bedent Baird)
    #     :type match_middle_name_as_initial: bool default True)
    #     :param fuzzy_ratio_threshold: "distance" between names calculated as 100 - fuzz.token_sort_ratio
    #     :type fuzzy_ratio_threshold: int 0-99
    #     :return:
    #     :rtype:
    #     """
    #
    #     comments = []
    #     if not self.conformed_family_name or not match_name.conformed_family_name:
    #         raise InvalidNameException([self.name_provided, match_name.name_provided], message="could not parse family name")
    #
    #     min = constants.ONE_CHAR if match_given_name_as_intial else constants.TWO_CHAR
    #     if len(self.conformed_given_name) < min or len(self.conformed_given_name) < min:
    #         raise InvalidNameException([self.name_provided, match_name.name_provided], message="could not parse given name") #f"could not parse given name{ 'or intial' if match_given_name_as_intial else ''}")
    #
    #     for family_name in self.p_match_family_names():
    #         distance = 100 - fuzz.token_sort_ratio(family_name, match_name.conformed_family_name)
    #         print (distance, family_name, match_name.conformed_family_name)
    #         if distance <= fuzzy_ratio_threshold:
    #             family_name_match = True
    #             if self.conformed_family_name == match_name.conformed_family_name:
    #                 comments.append("family name matched exactly")
    #             else:
    #                 comments.append("family name matched approximately")
    #             break
    #
    #         family_name_match = False
    #
    #     print(f"kilroy was here{family_name_match}")
    #
    #
    #
    #     for given_name in self.p_match_given_names ():
    #         distance = 100 - fuzz.token_sort_ratio(given_name, match_name.conformed_given_name)
    #         print (distance, given_name, match_name.conformed_given_name)
    #         if distance <= fuzzy_ratio_threshold:
    #             given_name_match = True
    #             if self.conformed_given_name == match_name.conformed_given_name:
    #                 comments.append ("given name matched exactly")
    #             else:
    #                 comments.append ("given name matched approximately")
    #             break
    #
    #         given_name_match = False
    #
    #     print(f"kilroy was here to{given_name_match}")
    #
    #
    #     if not given_name_match and match_given_name_as_intial and self.conformed_given_initial == match_name.conformed_given_initial:
    #         given_name_match = True
    #         comments.append("given name matched on initial")
    #
    #     if ignore_middle_name:
    #         middle_name_match = True
    #         comments.append ("middle name ignored")
    #     elif not self.conformed_middle_name or not match_name.conformed_middle_name:
    #         # no middle name
    #         middle_name_match = True
    #         comments.append("middle name missing")
    #     else:
    #         # This seems kind of worthless as it only compares, if provided in both names, but...
    #         for middle_name in self.p_match_middle_names ():
    #             distance = 100 - fuzz.token_sort_ratio (middle_name, match_name.conformed_middle_name)
    #             print (distance, middle_name, match_name.conformed_middle_name)
    #             if distance <= fuzzy_ratio_threshold:
    #                 middle_name_match = True
    #                 if self.conformed_middle_name == match_name.conformed_middle_name:
    #                     comments.append ("middle name matched exactly")
    #                 else:
    #                     comments.append ("middle name matched approximately")
    #                 break
    #
    #             middle_name_match = False
    #
    #         if not middle_name_match and match_middle_name_as_initial and self.conformed_middle_initial == match_name.conformed_middle_initial:
    #             middle_name_match = True
    #             comments.append ("middle name matched on initial")
    #
    #     # # deal with names where first and last transposed (typically japanese names, yoko ono is really ono yono)
    #     # if not given_name_match \
    #     #         and not family_name_match \
    #     #         and self.conformed_family_name == match_name.conformed_given_name \
    #     #         and self.conformed_given_name == match_name.conformed_family_name:
    #     #     given_name_match = True
    #     #     family_name_match = True
    #     #
    #     # # deal with compound initials (eg 'JD', 'BJ'
    #     # if not given_name_match and family_name_match and (len(match_name.conformed_given_name) == 2 or len(self.conformed_given_name)):
    #     #     if self.conformed_given_initial + self.conformed_middle_initial == match_name.conformed_given_name or match_name.conformed_given_initial + match_name.conformed_middle_initial == self.conformed_given_name :
    #     #         given_name_match = True
    #     #         middle_name_match = True
    #
    #     return (given_name_match and middle_name_match and family_name_match, comments)


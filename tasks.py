from objects import PersonName
import itertools

def match_names_task(n1, n2, ignore_middle_name=False,  match_given_name_as_initial=False
                , match_middle_name_as_initial=True, fuzzy_ratio_threshold=80):
    """
    :param n1: a full name in signature format OR a list of full_names (name and known aliases)
    :type n1: string or list of strings
    :param n2: a full name in signature format OR a list of full_names (name and known aliases)
    :type n2: string or list of strings
    :return: boolean

    this is a dumb function that returns no info about  the match or lack thereof. PersonName.match() does return detail
    """

    if type(n1) == str:
        names = [PersonName(full_name=n1)]
    elif type(n1) == list:
        names = [PersonName(full_name=full_name) for full_name in n1]
    else:
        return False

    if type(n2) == str:
        match_names = [PersonName(full_name=n2)]
    elif type(n2) == list:
        match_names = [PersonName(full_name=full_name) for full_name in n2]
    else:
        return False

    for n in itertools.product(names, match_names):
        return n[0].match( n[1]
            , ignore_middle_name=ignore_middle_name
            , match_given_name_as_intial=match_given_name_as_initial
            , match_middle_name_as_initial=match_middle_name_as_initial
            , fuzzy_ratio_threshold=fuzzy_ratio_threshold
            )


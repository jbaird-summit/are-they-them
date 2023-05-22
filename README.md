# are-they-them
playing around with name matching

Tries to match names conforming to english lower case characters then checking:
* exact match
* fuzzy match
* fuzzy match with swapped first and last name (common with english mis-understanding of Japanese names)
* fuzzy match using plesionyms for given names (check for diminutives, common mispellings and non-english spelling)
* fuzzy match using plesionyms for family name prefixes (check for diminutives, common mispellings and non-english spelling)



simple test to see if a name is likely a match...
>>> from objects import PersonName
>>> n = PersonName(full_name="Joseph Baird")
>>> n.conformed_family_name
'baird'

>>> n.match(PersonName(full_name="joe baird"))
joe baird joe baird 100
(True, 100)

>>> n.match(PersonName(full_name="josph baird"))
(True, 96)
>>> n.match(PersonName(full_name="giuseppe baird"))
giuseppe baird giuseppe baird 100
(True, 100)

>>> n.match(PersonName(full_name="sidhant pasricha"))
(False, 42)
>>>
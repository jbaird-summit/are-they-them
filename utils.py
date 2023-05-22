import re
import string
from unidecode import unidecode


class InvalidNameException(Exception):
    """Raised when the parsed name does not have valid family name or given name (or given name initial"""

    def __init__(self, names, message="parsed family and given name (or initial) required"):
        self.names = str(names)
        self.message = message
        super ().__init__ (self.message)

def conform_name(name_part):
    return re.sub(' +', ' ', ' '.join (unidecode (name_part).lower ().translate (
        str.maketrans ('', '', string.punctuation)
        ).split ())) or ''
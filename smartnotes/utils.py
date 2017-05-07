import re
import unicodedata


def remove_unnecessary_chars(string):
    '''
    Removes some characters, like diacritycs
    '''
    nfkd_form = unicodedata.normalize('NFKD', string)
    return "".join(c for c in nfkd_form if not unicodedata.combining(c))


def tokenize(text):
    '''
    Simple tokenizer that extracts only words and numbers (of length 3 and more) from given text
    '''
    return [match.group(0) for match in re.finditer(r'\w{3,}', text)]

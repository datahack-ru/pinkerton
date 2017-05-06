import unicodedata


def remove_uneccesary_chars(string):
    '''
    Removes some characters, like diacritycs
    '''
    nfkd_form = unicodedata.normalize('NFKD', string)
    return "".join(c for c in nfkd_form if not unicodedata.combining(c))

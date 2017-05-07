import re
import pymorphy2
import unicodedata


morph = pymorphy2.MorphAnalyzer()


def remove_unnecessary_chars(string):
    '''
    Removes some characters, like diacritycs
    '''
    nfkd_form = unicodedata.normalize('NFKD', string)
    return ''.join(c for c in nfkd_form if not unicodedata.combining(c))


def normalize(tokens, analyzer=morph):
    '''
    Replaces tokens with its first normal form returned by pymorphy2
    '''

    def get_normal_form(token):
        forms = morph.parse(token)
        return forms[0].normal_form

    return (get_normal_form(t) for t in tokens)


def tokenize(text):
    '''
    Simple tokenizer that extracts only words and numbers (of length 3 and more) from given text
    '''
    tokens = normalize(
        match.group(0) for match in re.finditer(r'\w{3,}', text)
    )
    return [
        remove_unnecessary_chars(token.lower()) for token in tokens
    ]

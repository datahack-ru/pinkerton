import regex as re
import pymorphy2
import unicodedata


morph = pymorphy2.MorphAnalyzer()


def remove_unnecessary_chars(string):
    '''
    Removes some characters, like accent diacritics
    '''
    source = unicodedata.normalize('NFD', string)
    result = ''.join(
        c for c in source if c not in {'´', '́'}
    )
    return unicodedata.normalize('NFC', result)


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
    tokens = (
        match.group(0) for match in re.finditer(r'\w{3,}', text, re.UNICODE)
    )
    tokens = (
        remove_unnecessary_chars(token.lower()) for token in tokens
    )
    return list(
        normalize(tokens)
    )

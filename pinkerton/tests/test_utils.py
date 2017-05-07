import pytest

from pinkerton.utils import (
    remove_unnecessary_chars,
    tokenize,
    normalize,
)


@pytest.fixture
def person_entity():
    return 'пётр первый'


def test_remove_unnecessary_chars(person_entity):
    assert remove_unnecessary_chars(person_entity) == 'петр первыи'


def test_tokenize():
    assert tokenize('Петр родился в 1470 году') == [
        'петр',
        'родиться',
        '1470',
        'год',
    ]


def test_normalize():
    tokens = tokenize('пётр первый вступил на престол в раннем возрасте')
    assert list(normalize(tokens)) == [
        'пётр',
        'один',
        'вступить',
        'престол',
        'раннии',
        'возраст',
    ]

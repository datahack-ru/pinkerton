import pytest

from smartnotes.utils import (
    remove_unnecessary_chars,
    tokenize,
)


@pytest.fixture
def person_entity():
    return 'пётр первый'


def test_remove_unnecessary_chars(person_entity):
    assert remove_unnecessary_chars(person_entity) == 'петр первыи'


def test_tokenize():
    assert tokenize('Петр родился в 1470 году') == [
        'петр',
        'родился',
        '1470',
        'году',
    ]

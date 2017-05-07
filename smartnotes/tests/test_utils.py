import pytest

from smartnotes.utils import remove_unnecessary_chars


@pytest.fixture
def person_entity():
    return 'пётр первый'


def test_remove_unnecessary_chars(person_entity):
    assert remove_unnecessary_chars(person_entity) == 'петр первыи'

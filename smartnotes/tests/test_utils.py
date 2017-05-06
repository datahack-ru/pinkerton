import pytest

from smartnotes.utils import remove_uneccesary_chars


@pytest.fixture
def person_entity():
    return 'пётр первый'


def test_remove_unecessary_chars(person_entity):
    assert remove_uneccesary_chars(person_entity) == 'петр первыи'

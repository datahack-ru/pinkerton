import pytest

from smartnotes.base import Entity, EntityType
from smartnotes.providers.wikipedia import WikipediaProvider
from smartnotes.providers.yandex_maps import YandexMapsProvider


@pytest.fixture
def wiki_provider():
    return WikipediaProvider()


@pytest.fixture
def ya_maps_provider():
    return YandexMapsProvider()


@pytest.fixture
def address_entity():
    return Entity(EntityType.Address, 'спб, цветочная 21', {
        'house': 21,
        'street': 'цветочная',
        'street_descriptor': 'улица',
    })


@pytest.fixture
def person_entity():
    return Entity(EntityType.Person, 'василий иванович', {
        'firstname': 'василий',
        'middlename': 'иванович',
    })

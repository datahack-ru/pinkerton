import pytest

from pinkerton.base import EntityType
from pinkerton.extractor import EntityExtractor


@pytest.fixture
def extractor():
    return EntityExtractor('https://natasha.b-labs.pro/api/')


@pytest.fixture
def test_text():
    return '''
    Ивана Васильевича Иванова, или просто Ваню, застал в расплох Алексей Петрович
    '''

def test_correct_api_urls(extractor):
    assert extractor.api_extract_url == 'https://natasha.b-labs.pro/api/extract'
    assert extractor.api_version_url == 'https://natasha.b-labs.pro/api/version'


@pytest.mark.asyncio
async def test_that_api_returns_some_results(extractor, test_text):
    objects, spans = await extractor.extract(test_text)

    assert objects
    assert spans

    assert objects[0]['type'] == EntityType.Person
    assert objects[0]['fields']['firstname'] == 'Иван'
    assert objects[0]['fields']['middlename'] == 'Василиевич'
    assert objects[0]['fields']['lastname'] == 'Иванов'

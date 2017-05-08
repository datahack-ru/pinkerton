import pytest


from pinkerton.similarity.lda import LDASimilarity
from pinkerton.providers.wikipedia import WikipediaProvider
from pinkerton.providers.yandex_maps import YandexMapsProvider


@pytest.fixture
def wiki_provider():
    return WikipediaProvider()


@pytest.fixture
def ya_maps_provider():
    return YandexMapsProvider()


@pytest.fixture
def person_context():
    return 'Иван Грозный, царь руси, по историческим данным - был тираном'


@pytest.fixture
def address_context():
    return 'Приезжаю в Россию в пятницу, встретимся в Санкт-Петербурге, на цветочной улице, 21'


@pytest.fixture
@pytest.mark.asyncio
async def person_search_results(wiki_provider):
    for e in [
        'Иван Грозный',
    ]:
        yield (await wiki_provider.search(query=e))


@pytest.fixture
@pytest.mark.asyncio
async def address_search_results(ya_maps_provider):
    for e in [
        'улица цветочная 21',
    ]:
        yield (await ya_maps_provider.search(query=e))


@pytest.fixture
def lda_comparator():
    return LDASimilarity()


@pytest.mark.asyncio
async def test_lda_score_for_person_entities(
    person_context,
    person_search_results,
    lda_comparator
):
    async for entities in person_search_results:
        if entities:
            scores = lda_comparator.score(entities, person_context)
            correct_query = entities[0]
            correct_query_score = scores[0][1]
            assert correct_query['title'] == 'Иван Грозный'
            assert round(correct_query_score) >= 0.87


@pytest.mark.asyncio
async def test_lda_score_for_address_entities(
    address_context,
    address_search_results,
    lda_comparator
):
    async for entities in address_search_results:
        if entities:
            scores = lda_comparator.score(entities, address_context)
            correct_query = entities[0]
            correct_query_score = scores[0][1]
            assert correct_query['context'] == 'Санкт-Петербург, Россия'
            assert round(correct_query_score) >= 0.67

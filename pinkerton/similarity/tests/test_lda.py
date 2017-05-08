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
    return 'Встретимся в Санкт-Петербурге, на цветочной улице, 21'


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
            queries = [
                e['context'] for e in entities if e['context']
            ]
            scores = lda_comparator.score(queries, person_context)
            correct_query_score = scores[0]
            assert all(correct_query_score >= q for q in scores[1:])


@pytest.mark.asyncio
async def test_lda_score_for_address_entities(
    address_context,
    address_search_results,
    lda_comparator
):
    async for entities in address_search_results:
        if entities:
            queries = [
                e['context'] for e in entities if e['context']
            ]
            scores = lda_comparator.score(queries, address_context)
            correct_query = queries[0]
            correct_query_score = scores[0]
            assert correct_query == 'Санкт-Петербург, Россия'
            assert round(correct_query_score) >= 0.67

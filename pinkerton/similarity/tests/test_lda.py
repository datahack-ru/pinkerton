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
def organisation_context():
    return '''
    Меркель назвала санкции единственным способом надавить на Россию
    Канцлер считает, что действия Москвы нельзя оставить без последствий, но решить конфликт военным путем нельзя.
    Санкции являются единственным средством нажать на Россию, считает канцлер Германии Ангела Меркель, пишут «Ведомости». Как передает Deutsche Welle, она заявила это в интервью радиостанции rbb-Inforadio, которое вышло в эфир 9 сентября. По словам канцлера, непосредственное участие России в украинском конфликте «очень-очень очевидно». Она считает, что действия Москвы нельзя оставить без последствий, но решить конфликт военным путем нельзя. Как только ситуация на Украине нормализуется, санкции должны быть отменены, добавила Меркель.
    Канцлер также заявила, что правительство не намерено наращивать бюджет министерства обороны, несмотря на планы НАТО создать новые силы быстрого реагирования. По словам Меркель, дополнительные финансовые средства на армию появятся после вывода контингента ВС ФРГ из Афганистана.
    8 сентября Меркель заявила на закрытом заседании в правительстве, что санкции против России необходимо ввести, несмотря на достигнутую договоренность о прекращении огня. Об этом рассказали несколько участников заседания. По их словам, канцлер напомнила, что Россия уже неоднократно обманывала Запад, не выполняя обещания, а также добавила, что российские войска по-прежнему находятся на Украине. ЕС должен действовать более решительно, процитировали ее участники заседания.
    '''


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
@pytest.mark.asyncio
async def organisation_search_results(wiki_provider):
    for e in [
        'министерство обороны',
    ]:
        yield (await wiki_provider.search(query=e))


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


@pytest.mark.asyncio
async def test_lda_score_for_organisation_entities(
    organisation_context,
    organisation_search_results,
    lda_comparator
):
    async for entities in organisation_search_results:
        if entities:
            scores = lda_comparator.score(entities, organisation_context)
            top_3_titles = [s[0]['title'] for s in scores[:3]]

            assert len(scores) > 3
            assert set(top_3_titles) == {
                'Министерство обороны Украины',
                'Министерство обороны Афганистана',
                'Министерство обороны Российской Федерации',
            }

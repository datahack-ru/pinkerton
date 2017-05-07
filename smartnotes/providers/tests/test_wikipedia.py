import pytest


@pytest.mark.asyncio
async def test_query_person(wiki_provider):
    results = await wiki_provider.search(query='пётр 1')
    assert {
        'context': 'Пётр I Алексе́евич, прозванный Вели́кий (30 мая [9 июня] '
        '1672 год — 28 января [8 февраля] 1725 год) — последний царь '
        'всея Руси (с 1682 года) и первый Император Всероссийский (с '
        '1721 года).',
        'source': 'https://ru.wikipedia.org/wiki/%D0%9F%D1%91%D1%82%D1%80_I',
        'title': 'Пётр I',
    } in results


@pytest.mark.asyncio
async def test_query_org(wiki_provider):
    results = await wiki_provider.search(query='петропавловская крепость')
    assert {
        'context': 'Петропа́вловская кре́пость — крепость в Санкт-Петербурге, '
        'расположенная на Заячьем острове, историческое ядро города.',
        'source': 'https://ru.wikipedia.org/wiki/%D0%9F%D0%B5%D1%82%D1%80%D0%BE%D0%BF%D0%B0%D0%B2%D0%BB%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F_%D0%BA%D1%80%D0%B5%D0%BF%D0%BE%D1%81%D1%82%D1%8C',
        'title': 'Петропавловская крепость'
    } in results


@pytest.mark.asyncio
async def test_query_with_limit(wiki_provider):
    results = await wiki_provider.search(query='пётр 1', limit=1)
    assert results == [
        {
            'context': 'Пётр I Алексе́евич, прозванный Вели́кий (30 мая [9 июня] 1672 '
            'год — 28 января [8 февраля] 1725 год) — последний царь всея Руси '
            '(с 1682 года) и первый Император Всероссийский (с 1721 года).',
            'source': 'https://ru.wikipedia.org/wiki/%D0%9F%D1%91%D1%82%D1%80_I',
            'title': 'Пётр I',
        }
    ]


def test_not_accepts_method(wiki_provider, address_entity):
    assert not wiki_provider.accepts(address_entity)


def test_accepts_method(wiki_provider, person_entity):
    assert wiki_provider.accepts(person_entity)

import pytest


@pytest.mark.asyncio
async def test_query_address(ya_maps_provider, address_entity):
    results = await ya_maps_provider.search(query=address_entity.title)
    items = [
        {
            'title': item['title'],
            'context': item['context'],
        } for item in results
    ]
    assert {
        'title': 'Россия, Санкт-Петербург, Цветочная улица, 21',
        'context': 'Санкт-Петербург, Россия',
    } in items

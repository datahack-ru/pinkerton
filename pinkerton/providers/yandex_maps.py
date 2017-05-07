from pinkerton.base import EntityType
from pinkerton.providers.base import BaseDataProvider


class YandexMapsProvider(BaseDataProvider):

    ALLOWED_ENTITY_TYPES = [
        EntityType.Address,
    ]

    def __init__(self):
        self.api_base_url = 'https://geocode-maps.yandex.ru/1.x/'

    async def search(self, query: str, limit=100) -> list:

        params = {
            'geocode': query,
            'results': limit,
            'format': 'json',
        }

        async with self.session as session:
            async with session.get(
                self.api_base_url, params=params
            ) as response:
                response = await response.json()
                response = (
                    response
                    .get('response', {})
                    .get('GeoObjectCollection', {})
                    .get('featureMember', [])
                )
                items = (
                    item.get('GeoObject', {})
                    for item in response
                )
                response = [
                    {
                        'title': (
                            item
                            .get('metaDataProperty')
                            .get('GeocoderMetaData')
                            .get('text')
                        ),
                        'context': item['description'],
                        'source': item,
                    } for item in items
                ]
                return response

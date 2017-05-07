from smartnotes.base import EntityType
from smartnotes.providers.base import BaseDataProvider


class WikipediaProvider(BaseDataProvider):

    ALLOWED_ENTITY_TYPES = [
        EntityType.Person,
        EntityType.Location,
        EntityType.Organisation,
    ]

    def __init__(self, language='ru'):
        self.api_base_url = f'https://{language}.wikipedia.org/w/api.php'

    async def search(self, query: str, limit=100) -> list:

        params = {
            'utf8': 'true',
            'format': 'json',
            'action': 'opensearch',
            'limit': limit,
            'search': query,
        }

        async with self.session as session:
            async with session.get(
                self.api_base_url, params=params
            ) as response:
                _, titles, descriptions, links = await response.json()
                return [
                    {
                        'title': t,
                        'context': d,
                        'source': l,
                    } for (t, d, l) in zip(titles, descriptions, links)
                ]

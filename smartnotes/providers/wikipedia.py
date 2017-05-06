from aiohttp import ClientSession

from smartnotes.settings import DATA_PROVIDER_CLIENT_USER_AGENT
from smartnotes.providers.base import BaseDataProvider


class WikipediaProvider(BaseDataProvider):

    def __init__(self, language='ru'):
        self.api_base_url = f'https://{language}.wikipedia.org/w/api.php'

    async def search(self, entity: str, limit=100) -> list:

        params = {
            'utf8': 'true',
            'format': 'json',
            'action': 'opensearch',
            'limit': limit,
            'search': entity,
        }

        async with ClientSession(headers={
            'User-Agent': DATA_PROVIDER_CLIENT_USER_AGENT,
        }) as session:
            async with session.get(
                self.api_base_url, params=params
            ) as response:
                _, titles, descriptions, links = await response.json()
                return [
                    {
                        'title': t,
                        'context': d,
                        'resource': l,
                    } for (t, d, l) in zip(titles, descriptions, links)
                ]

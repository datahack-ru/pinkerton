from urllib.parse import urljoin
from aiohttp import ClientSession

from pinkerton.base import EntityType
from pinkerton.settings import DATA_PROVIDER_CLIENT_HEADERS


class EntityExtractor:

    '''
    Providers API to Natasha playground
    '''

    ENTITIES_CONVERT_MAP = {
        'person': EntityType.Person,
        'organisation': EntityType.Organisation,
        'location': EntityType.Location,
    }

    def __init__(self, api_base_url: str):
        self.api_base_url = api_base_url
        self.api_extract_url = urljoin(self.api_base_url, 'extract')
        self.api_version_url = urljoin(self.api_base_url, 'version')

    @property
    def session(self):
        return ClientSession(headers=DATA_PROVIDER_CLIENT_HEADERS)

    async def extract(self, text: str) -> dict:
        async with self.session as session:
            async with session.post(self.api_extract_url, data={
                'text': text,
            }) as response:
                response = await response.json()
                objects, spans = response['objects'], response['spans']

                for obj in objects:
                    obj['type'] = self.ENTITIES_CONVERT_MAP[obj['type']]

                return objects, spans

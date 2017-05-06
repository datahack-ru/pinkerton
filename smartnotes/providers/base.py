class BaseDataProvider:

    async def search(self, entity: object) -> list:
        '''
        Query method takes an entity (in most cases: string) and returns list
        of matches from external knowlegde database, like Wikipedia.org
        '''
        raise NotImplementedError

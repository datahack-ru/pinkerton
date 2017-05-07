class BaseDataProvider:

    ALLOWED_ENTITY_TYPES = []

    async def search(self, query: str) -> list:
        '''
        Query method takes an entity (in most cases: string) and returns list
        of matches from external knowlegde database, like Wikipedia.org
        '''
        raise NotImplementedError

    def accepts(self, entity: object) -> bool:
        '''
        Returns true if data provider can return information about given entity
        '''
        return entity.type in self.ALLOWED_ENTITY_TYPES

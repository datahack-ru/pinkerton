class BaseSimilarityComparator:

    def score(self, entities: list, context: str) -> list:
        '''
        Returns list with entities sorted by similarity score
        '''
        raise NotImplementedError

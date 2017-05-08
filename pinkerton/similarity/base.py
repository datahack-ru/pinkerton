class BaseSimilarityComparator:

    def score(self, queries: list, context: str) -> list:
        '''
        Returns list with queries sorted by similarity score
        '''
        raise NotImplementedError

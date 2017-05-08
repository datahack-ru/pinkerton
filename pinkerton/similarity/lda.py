from gensim.corpora import Dictionary
from gensim.models import LdaModel

from pinkerton.utils import tokenize
from pinkerton.similarity.base import BaseSimilarityComparator


class LDASimilarity(BaseSimilarityComparator):

    def __init__(self, **kwargs):
        self.model_kwargs = kwargs or {
            'passes': 20,
            'num_topics': 100,
        }

    def score(self, queries: list, context: str) -> list:

        context = tokenize(context)

        dictionary = Dictionary([context])

        vectors = [
            dictionary.doc2bow(
                tokenize(q)
            ) for q in queries
        ]

        model = LdaModel(id2word=dictionary, **self.model_kwargs)

        scores = [
            model[vec][-1][1] for vec in vectors if model[vec]
        ]

        return scores

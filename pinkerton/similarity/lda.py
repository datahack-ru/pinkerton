from gensim.corpora import Dictionary
from gensim.models import LdaModel

from pinkerton.utils import tokenize
from pinkerton.similarity.base import BaseSimilarityComparator


class LDASimilarity(BaseSimilarityComparator):

    def __init__(self, **kwargs):
        self.model_kwargs = kwargs or {
            'passes': 100,
            'num_topics': 25,
        }

    def score(self, entities: list, context: str) -> list:

        queries = [
            (i, q['context']) for i, q in enumerate(entities) if q['context']
        ]

        context = tokenize(context)

        dictionary = Dictionary([context])

        vectors = [
            dictionary.doc2bow(
                tokenize(q)
            ) for _, q in queries
        ]

        model = LdaModel(id2word=dictionary, **self.model_kwargs)

        ents = (
            entities[i] for i, _ in queries
        )

        scores = (
            model[vec][-1][1] for vec in vectors if model[vec]
        )

        results = zip(ents, scores)

        def sort_by_score(item):
            return item[1]

        return sorted(results, key=sort_by_score, reverse=True)

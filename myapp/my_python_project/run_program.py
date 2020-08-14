import gensim.models.word2vec as w2v
import os

thrones2vec = w2v.Word2Vec.load(os.path.join(os.path.dirname(os.path.dirname(__file__)),'my_python_project/trained/thrones2vec.w2v'))


def nearest_similarity_cosmul(start1, end1, end2):
    similarities = thrones2vec.wv.most_similar_cosmul(
        positive=[end2, start1],
        negative=[end1]
    )
    start2 = similarities[0][0]
    print("{start1} is related to {end1}, as {start2} is related to {end2}".format(**locals()))
    return start2

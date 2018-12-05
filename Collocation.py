from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.collocations import TrigramCollocationFinder
from nltk.metrics import TrigramAssocMeasures

#Word bigram collocations
def get_bigram_colloc(tokens,nbest):
    bcf = BigramCollocationFinder.from_words(tokens)
    return bcf.nbest(BigramAssocMeasures.likelihood_ratio, nbest)

#Word trigram collocations
def get_trigram_colloc(tokens,freq,nbest):
    tcf = TrigramCollocationFinder.from_words(tokens)
    tcf.apply_freq_filter(freq)
    return tcf.nbest(TrigramAssocMeasures.likelihood_ratio, nbest)

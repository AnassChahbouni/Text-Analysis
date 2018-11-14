# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 17:24:53 2018

@author: Anass
"""

#imports
import nltk
import re
from nltk.stem.snowball import FrenchStemmer
from nltk.corpus import stopwords
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.collocations import TrigramCollocationFinder
from nltk.metrics import TrigramAssocMeasures

#Reading in the text from the file
def read_file(path):
    f = open(path,'r')
    raw = f.read()
    return raw

#Tokenize the text in sentences
def get_sent_tokens(raw,encoding='utf8'):
    tokens = nltk.sent_tokenize(raw,"french")
    print( "Nombre de phrases  : %d" % len(tokens))
    return tokens

#Tokenize the text in words
def get_word_tokens(raw,encoding='utf8'):
    tokens = nltk.word_tokenize(raw,"french")
    print( "Nombre de mots  : %d" % len(tokens))
    return tokens

def get_nltk_text(raw,encoding='utf8'):
    no_commas = re.sub(r'[.|,|\']',' ', str(raw))
    tokens = nltk.word_tokenize(no_commas)
    text=nltk.Text(tokens,encoding)
    return text

#Clean tokens from stopwords and punctuation and size more then
def filter_tokens(text):
    #French punctuation
    punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'",'»','«','’','–','-','_']
    #More french stopwords
    #Nombres, déterminants, pronoms, conjonctions, prépositions et adverbes
    dico = [
        #NOMBRES
            "zéro", "un", "deux", "trois", "quatre", "cinq", "six", 
            "sept", "huit", "neuf", "dix", "onze", "douze", "treize", 
            "quatorze", "quinze", "seize", "dix-sept", "dix-huit", "dix-neuf", 
            "vingt", "trente", "quarante", "cinquante", "soixante", 
            "soixante-dix", "quatre-vingts", "quatre-vingt-dix", "cent",
    	# ARTICLES / DETERMINANTS
        	"le", "la", "les", "l'", "un", "une", "des", "d'",
    		"du", "de", "au", "aux", "ce", "cet", "cette", "ces",
    		"mon", "son", "ma", "ta", "sa", "mes", "ses",
    		"notre", "votre", "leur", "nos", "vos", "leurs",
    		"aucun", "aucune", "aucuns", "aucunes",
    		"tel", "telle", "tels", "telles",
    		"tout", "toute", "tous", "toutes",
    		"chaque",
    	# PRONOM
        	"je", "tu", "il", "elle", "on", "nous", "vous", "ils", "elles",
    		"me", "m'", "moi", "te", "t'", "toi", "ça",
    		"se", "y", "le", "lui", "soi", "leur", "leures", "leurs", "eux", "lui",
    		"qui", "que", "quoi", "dont", "où", "quiconque", 
            "rien", "autrui", "nul", "personne", "autre", "autres", "certains", "plusieurs",
            "aucun", "chacun", "même", "tout", "toute", "tous", "toutes",
    	# CONJONCTION
        	"mais", "ou", "et", "donc", "or", "ni", "car",
    		"que", "quand", "comme", "si", "puis",
    		"lorsque", "quoique", "puisque", "parce",
    	# PREPOSITION
        	"à", "devant", "derrière", "malgré", "sauf", "autour",
    		"selon", "avant", "devant", "sous", "avec", 
    		"en", "par", "sur", "entre", "parmi", "chez",
    		"envers", "pendant", "vers", "dans", "pour", "de", 
    		"près", "depuis", "sans",
        #ADVERBE
            "toujours", "plus", "moins", "encore", "peu", "trop", 
            "très", "assez", "autant", "beaucoup", "quelque", "quelques", "voilà",
            "quelques", "davantage", "guére", "tant", "alors", 
            "ici", "alors", "enfin", "cependant", "maintenant"
    ]
    words = [w.lower() for w in text]
    clean_tokens = []
    for word in words:
        if word not in dico and word not in stopwords.words('french') and word not in punctuation and len(word) > 1:
            clean_tokens.append(word)
    #clean_tokens.sort()
    return clean_tokens

#Count Word Frequency
def top_word_freq(words):
    freq = nltk.FreqDist(words)
    print("Les mots les plus occurrent: ")
    for key,val in freq.items(): 
        if val>15 :
            print (str(key) + '  : ' + str(val) + " fois")
    return freq.plot(25, cumulative=False)

#Word bigram collocations
def get_bigram_colloc(tokens,nbest):
    bcf = BigramCollocationFinder.from_words(tokens)
    return bcf.nbest(BigramAssocMeasures.likelihood_ratio, nbest)

#Word trigram collocations
def get_trigram_colloc(tokens,freq,nbest):
    tcf = TrigramCollocationFinder.from_words(tokens)
    tcf.apply_freq_filter(freq)
    return tcf.nbest(TrigramAssocMeasures.likelihood_ratio, nbest)

#Stemming words
def stem_words(words):
    '''stems the word list using the French Stemmer'''
    stemmed_words = [] #declare an empty list to hold our stemmed words
    stemmer = FrenchStemmer() #create a stemmer object in the FrenchStemmer class
    for word in words:
        stemmed_word=stemmer.stem(word) #stem the word
        stemmed_words.append(stemmed_word) #add it to our stemmed word list
    stemmed_words.sort() #sort the stemmed_words
    return stemmed_words

text = read_file('C:\\Users\\Anass\\Desktop\\Chap1.txt')


get_sent_tokens(text)
words = get_nltk_text(get_word_tokens(text,'utf8'))
#print(stem_words(filter_tokens(words)))
top_word_freq(filter_tokens(words))


#Word collocations
print(get_bigram_colloc(filter_tokens(words), 6))
get_trigram_colloc(filter_tokens(words), 2, 2)


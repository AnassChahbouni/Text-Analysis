#prétraitement 
import nltk
from nltk.corpus import stopwords
import re


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


#Découpage du texte en phrase et renvoie un arbre (tree)        
def chunkSentences(text):
    sentences = nltk.sent_tokenize(text)
    tokenizedSentences = [nltk.word_tokenize(sentence)
                          for sentence in sentences]
    taggedSentences = [nltk.pos_tag(sentence)
                       for sentence in tokenizedSentences]
    if nltk.__version__[0:2] == "2.":
        chunkedSentences = nltk.batch_ne_chunk(taggedSentences, binary=True)
    else:
        chunkedSentences = nltk.ne_chunk_sents(taggedSentences, binary=True)
    return chunkedSentences
    

#Fait un dictionnaire des occurences/ entités noommées
def buildDict(chunkedSentences, _entityNames=None):

    if _entityNames is None:
        _entityNames = []

    for tree in chunkedSentences:
        extractEntityNames(tree, _entityNames=_entityNames)

    return _entityNames

raw_stopword_list = ["Ap.","autrefois","mais ","les","bigre","enfin","voici","quelquefois","quoique","allons","puis", "Apr.", "comment","tant","tiens","certes", "GHz", "MHz", "USD", "a", "afin", "ah", "ai", "aie", "aient", "aies", "ait", "alors", "après", "as", "attendu", "au", "au-delà", "au-devant", "aucun", "aucune", "audit", "auprès", "auquel", "aura", "aurai", "auraient", "aurais", "aurait", "auras", "aurez", "auriez", "aurions", "aurons", "auront", "aussi", "autour", "autre", "autres", "autrui", "aux", "auxdites", "auxdits", "auxquelles", "auxquels", "avaient", "avais", "avait", "avant", "avec", "avez", "aviez", "avions", "avons", "ayant", "ayez", "ayons", "b", "bah", "banco", "ben", "bien", "bé", "c", "c'", "c'est", "c'était", "car", "ce", "ceci", "cela", "celle", "celle-ci", "celle-là", "celles", "celles-ci", "celles-là", "celui", "celui-ci", "celui-là", "celà", "cent", "cents", "cependant", "certain", "certaine", "certaines", "certains", "ces", "cet", "cette", "ceux", "ceux-ci", "ceux-là", "cf.", "cg", "cgr", "chacun", "chacune", "chaque", "chez", "ci", "cinq", "cinquante", "cinquante-cinq", "cinquante-deux", "cinquante-et-un", "cinquante-huit", "cinquante-neuf", "cinquante-quatre", "cinquante-sept", "cinquante-six", "cinquante-trois", "cl", "cm", "cm²", "comme", "contre", "d", "d'", "d'après", "d'un", "d'une", "dans", "de", "depuis", "derrière", "des", "desdites", "desdits", "desquelles", "desquels", "deux", "devant", "devers", "dg", "différentes", "différents", "divers", "diverses", "dix", "dix-huit", "dix-neuf", "dix-sept", "dl", "dm", "donc", "dont", "douze", "du", "dudit", "duquel", "durant", "dès", "déjà", "e", "eh", "elle", "elles", "en", "en-dehors", "encore", "enfin", "entre", "envers", "es", "est", "et", "eu", "eue", "eues", "euh", "eurent", "eus", "eusse", "eussent", "eusses", "eussiez", "eussions", "eut", "eux", "eûmes", "eût", "eûtes", "f", "fait", "fi", "flac", "fors", "furent", "fus", "fusse", "fussent", "fusses", "fussiez", "fussions", "fut", "fûmes", "fût", "fûtes", "g", "gr", "h", "ha", "han", "hein", "hem", "heu", "hg", "hl", "hm", "hm³", "holà", "hop", "hormis", "hors", "huit", "hum", "hé", "i", "ici", "il", "ils", "j", "j'", "j'ai", "j'avais", "j'étais", "jamais", "je", "jusqu'", "jusqu'au", "jusqu'aux", "jusqu'à", "jusque", "k", "kg", "km", "km²", "l", "l'", "l'autre", "l'on", "l'un", "l'une", "la", "laquelle", "le", "lequel", "les", "lesquelles", "lesquels", "leur", "leurs", "lez", "lors", "lorsqu'", "lorsque", "lui", "lès", "m", "m'", "ma", "maint", "mainte", "maintes", "maints", "mais", "malgré", "me", "mes", "mg", "mgr", "mil", "mille", "milliards", "millions", "ml", "mm", "mm²", "moi", "moins", "mon", "moyennant", "mt", "m²", "m³", "même", "mêmes", "n", "n'avait", "n'y", "ne", "neuf", "ni", "non", "nonante", "nonobstant", "nos", "notre", "nous", "nul", "nulle", "nº", "néanmoins", "o", "octante", "oh", "on", "ont", "onze", "or", "ou", "outre", "où", "p", "par", "par-delà", "parbleu", "parce", "parmi", "pas", "passé", "pendant", "personne", "peu", "plus", "plus_d'un", "plus_d'une", "plusieurs", "pour", "pourquoi", "pourtant", "pourvu", "près", "puisqu'", "puisque", "q", "qu", "qu'", "qu'elle", "qu'elles", "qu'il", "qu'ils", "qu'on", "quand", "quant", "quarante", "quarante-cinq", "quarante-deux", "quarante-et-un", "quarante-huit", "quarante-neuf", "quarante-quatre", "quarante-sept", "quarante-six", "quarante-trois", "quatorze", "quatre", "quatre-vingt", "quatre-vingt-cinq", "quatre-vingt-deux", "quatre-vingt-dix", "quatre-vingt-dix-huit", "quatre-vingt-dix-neuf", "quatre-vingt-dix-sept", "quatre-vingt-douze", "quatre-vingt-huit", "quatre-vingt-neuf", "quatre-vingt-onze", "quatre-vingt-quatorze", "quatre-vingt-quatre", "quatre-vingt-quinze", "quatre-vingt-seize", "quatre-vingt-sept", "quatre-vingt-six", "quatre-vingt-treize", "quatre-vingt-trois", "quatre-vingt-un", "quatre-vingt-une", "quatre-vingts", "que", "quel", "quelle", "quelles", "quelqu'", "quelqu'un", "quelqu'une", "quelque", "quelques", "quelques-unes", "quelques-uns", "quels", "qui", "quiconque", "quinze", "quoi", "quoiqu'", "quoique", "r", "revoici", "revoilà", "rien", "s", "s'", "sa", "sans", "sauf", "se", "seize", "selon", "sept", "septante", "sera", "serai", "seraient", "serais", "serait", "seras", "serez", "seriez", "serions", "serons", "seront", "ses", "si", "sinon", "six", "soi", "soient", "sois", "soit", "soixante", "soixante-cinq", "soixante-deux", "soixante-dix", "soixante-dix-huit", "soixante-dix-neuf", "soixante-dix-sept", "soixante-douze", "soixante-et-onze", "soixante-et-un", "soixante-et-une", "soixante-huit", "soixante-neuf", "soixante-quatorze", "soixante-quatre", "soixante-quinze", "soixante-seize", "soixante-sept", "soixante-six", "soixante-treize", "soixante-trois", "sommes", "son", "sont", "sous", "soyez", "soyons", "suis", "suite", "sur", "sus", "t", "t'", "ta", "tacatac", "tandis", "te", "tel", "telle", "telles", "tels", "tes", "toi", "ton", "toujours", "tous", "tout", "toute", "toutefois", "toutes", "treize", "trente", "trente-cinq", "trente-deux", "trente-et-un", "trente-huit", "trente-neuf", "trente-quatre", "trente-sept", "trente-six", "trente-trois", "trois", "très", "tu", "u", "un", "une", "unes", "uns", "v", "vers", "via", "vingt", "vingt-cinq", "vingt-deux", "vingt-huit", "vingt-neuf", "vingt-quatre", "vingt-sept", "vingt-six", "vingt-trois", "vis-à-vis", "voici", "voilà", "vos", "votre", "vous", "w", "x", "y", "z", "zéro", "à", "ç'", "ça", "ès", "étaient", "étais", "était", "étant", "étiez", "étions", "été", "étée", "étées", "étés", "êtes", "être", "ô"]


#Enlève les stopWords du texte
def removeStopwords(entityNames, customStopWords=None):
    for name in entityNames:
        if name.lower() in stopwords.words('french') or name.lower() in raw_stopword_list or len(name)<=3:
            entityNames.remove(name)

#Sépare le texte en phrase en utilisant les expressions réégulières
def splitIntoSentences(text):
    sentenceEnders = re.compile(r"""
    (?:               
      (?<=[.!?])      
    | (?<=[.!?]['"])  
    )                 
    (?<!  M\.   )    
    (?<!  Mme\.  )    
    (?<!  Mlle\.   )    
    (?<!  Dr\.   )    
    \s+               
    """, re.IGNORECASE | re.VERBOSE)
    return sentenceEnders.split(text)

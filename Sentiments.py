from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer
import Pretraitement as ptr
import Personnage_principal as pp


# Analyse des setiments
with open("C:/Users/Ryan/Downloads/chap1.txt", "rb") as f:
        text = f.read().decode('iso-8859-15')

chunkedSentences = ptr.chunkSentences(text)
entityNames = ptr.buildDict(chunkedSentences)
ptr.removeStopwords(entityNames)
majorCharacters = pp.getMajorCharacters(entityNames)

# Sentiments des personnages
blob = TextBlob(text, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
for sentence in blob.sentences:
    s = str(sentence)
    for name in majorCharacters :
        if (name in s.split()):
            if ((float(sentence.sentiment[0])>0.2) or(float(sentence.sentiment[0])< -0.2)):
                print(blob.sentences.index(sentence),name, " =  ", sentence.sentiment[0])
                
text.close()
import re
import numpy as np
from collections import defaultdict
import Personnage_principal as pp

with open("C:/Users/User/Downloads/chap1.txt", "rb") as f:
        text = f.read().decode('iso-8859-15')

#Compare les listes de phrases avec les noms des personnages 
#Renvoie les phrases contenant les noms des personnages
def compareLists(sentenceList, majorCharacters):
    characterSentences = defaultdict(list)
    for sentence in sentenceList:
        for name in majorCharacters:
            if re.search(r"\b(?=\w)%s\b(?!\w)" % re.escape(name),
                         sentence,
                         re.IGNORECASE):
                characterSentences[name].append(sentence)
    return characterSentences

            


characterSentences=compareLists(pp.sentenceList, pp.majorCharacters)
""" CREATION MATRICE ADJ COOCURENCE PERSONNAGE """
vector1 = list()
vector2 = list()
for i in range(0,len(pp.majorCharacters)):
    vector1.append(0)
for j in range(0,len(pp.majorCharacters)):
    vector2.append(vector1)
matrice_perso=np.matrix(vector2)
print(matrice_perso)
""" ------------------ """

import networkx as nx
G = nx.Graph()

""" REMPPLISSAGE MATRICE ADJ COOCURENCE PERSONNAGE + GRAPHE"""
i=0
for name in pp.majorCharacters:
    w = 0
    for sentence in characterSentences[name]:
        j=0
        for name2 in pp.majorCharacters:
            if name2 != name :
                if sentence.find(name2)!=-1:
                    print(name,"-....-",name2)
                    matrice_perso[i,j]+=1
                    w = w + 0.1
                    print(matrice_perso)
                    G.add_edge(name,name2,with_labels=True,weight=w)
                    print(w)
            j+=1
    i+=1
""" ----------------- """                    

""" affichage de la matrice """
print(matrice_perso)

""" affichage du graphe (sans les poids pour l'instant) """
nx.draw(G,with_labels=True, font_weight='bold')
    
text.close()
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
for i in range(0,len(majorCharacters)):
    vector1.append(0)
for j in range(0,len(majorCharacters)):
    vector2.append(vector1)
matrice_perso=np.matrix(vector2)
print(matrice_perso)
""" ------------------ """

import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()

""" REMPPLISSAGE MATRICE ADJ COOCURENCE PERSONNAGE + GRAPHE"""
i=0
for name in majorCharacters:
    for sentence in characterSentences[name]:
        print("sentence : "+sentence)
        j=0
        for name2 in majorCharacters:
            if name2 != name :
                if sentence.find(name2)!=-1:
                    print(name,"-....-",name2)
                    matrice_perso[i,j]+=1
            j+=1
    i+=1
""" ----------------- """    

""" REMPPLISSAGE  GRAPHE + AFFICHAGE GRAPHE AVEC POID """ 
print(matrice_perso)                 
i = 0
for name in majorCharacters:
    j = 0
    for name2 in majorCharacters:
        if name2 != name :
            if matrice_perso[i,j] > 0:
                w = 1 * matrice_perso[i,j]
                print("nom1 : "+name+"| nom2 : "+name2+"| posI : "+str(i)+"| posJ : "+str(j)+"| weight : "+str(w))
                G.add_edge(name,name2,with_labels=True,weight=w)
        j+=1
    i+=1               

pos=nx.spring_layout(G)
nx.draw_networkx(G, pos, with_labels=True)
nx.draw(G,pos)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels,font_size=10, font_color='k', font_family='sans-serif', font_weight='normal', alpha=1.0)
""" ----------------- """  

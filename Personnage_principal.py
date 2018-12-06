#Prend en entrée le tree et renvoie les entités nommées
def extractEntityNames(tree, _entityNames=None):

    if _entityNames is None:
        _entityNames = []
    try:
        if nltk.__version__[0:2] == "2.":
            label = tree.node
        else:
            label = tree.label()
    except AttributeError:
        pass
    else:
        if label == 'NE':
            _entityNames.append(' '.join([child[0] for child in tree]))
        else:
            for child in tree:
                extractEntityNames(child, _entityNames=_entityNames)
    return _entityNames

#Renvoie tout les personnages 
def getMajorCharacters(entityNames):
    return {name for name in entityNames if entityNames.count(name) > 2}

#Renvoie les personnages principaux en fonction de la frequence d'apparition 
def getMajorCharacters(entityNames, feq):
    return {name for name in entityNames if entityNames.count(name) > feq}

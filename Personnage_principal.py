#Renvoie les personnages principaux
def getMajorCharacters(entityNames):
    return {name for name in entityNames if entityNames.count(name) > 2}
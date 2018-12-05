from geotext import GeoText
#CHANGER De code !!

book = open("C:/Users/Name/Downloads/chap1.txt","r")
bow = list()
majuscule = list()
for i in book :
        bow.append(i.split(" "))
        
for i in bow :
    for j in i :
        if (len(j)> 1):
            if (j[0].isupper()):
                majuscule.append(j)
                
ville = ' '.join(majuscule)
res = GeoText(ville)
print("Pays = ",res.country_mentions)
print("-----------------------------------")
print("Villes = ", res.cities)

places_occurence = dict()
for c in res.cities:
    places_occurence[c] = places_occurence.get(c, 0) + 1
    
print(places_occurence)   
book.close()

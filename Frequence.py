import nltk

#Count Word Frequency
def top_word_freq(words):
    freq = nltk.FreqDist(words)
    print("Les mots les plus occurrent: ")
    for key,val in freq.items(): 
        if val>15 :
            print (str(key) + '  : ' + str(val) + " fois")
    return freq.plot(25, cumulative=False)

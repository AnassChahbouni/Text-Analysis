# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 17:24:53 2018

@author: Anass
"""

#imports
import nltk
import Pretraitement as p
import Collocation as c
import Frequence as f

text = read_file('C:\\Users\\Anass\\Desktop\\Chap1.txt')


p.get_sent_tokens(text)
words = p.get_nltk_text(p.get_word_tokens(text,'utf8'))
f.top_word_freq(filter_tokens(words))


#Word collocations
print(c.get_bigram_colloc(p.filter_tokens(words), 6))
c.get_trigram_colloc(p.filter_tokens(words), 2, 2)


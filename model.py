#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 11:19:52 2020

@author: maggietjia
"""

class sentiment(object):

    
    def tokener(self, txt):
        import nltk
        import re
        from nltk import WordNetLemmatizer
        from nltk.tokenize import sent_tokenize, word_tokenize
        from sklearn.feature_extraction.text import TfidfVectorizer
        import pandas as pd
        from nltk.corpus import stopwords
        my_lemma = WordNetLemmatizer()
        
        token = nltk.word_tokenize(txt)
        token_text = [word for word in token if word not in stopwords.words('english')]
        lemma = [my_lemma.lemmatize(word) for word in token_text]
        
        file_nw = open('/Users/maggietjia/Documents/Spring2020/NLP/nw.rtf', 'r')
        content_nc = file_nw.read()
        nw_words = content_nc.split('\n\\\n')
        nw = list(set(lemma).intersection(nw_words))
        nc = len(nw)
        
        file_pw = open('/Users/maggietjia/Documents/Spring2020/NLP/pw.rtf', 'r')
        content_pc = file_pw.read()
        pw_words = content_pc.split('\n\\\n')
        pw = list(set(lemma).intersection(pw_words))
        pc = len(pw)
        
        tc = nc + pc
        S = ((nc * -1) + (pc * 1))/(tc)
  
        return S
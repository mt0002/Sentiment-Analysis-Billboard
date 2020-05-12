#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 22:31:28 2020

@author: maggietjia
"""

import pandas as pd
import nltk

file = pd.read_csv('/Users/maggietjia/Documents/Spring2020/NLP/billboard_lyrics_1964-2015.csv', encoding = "ISO-8859-1")
file = file[(file.Lyrics != "  ") & (file.Lyrics != "instrumental") & (file.Lyrics != "Instrumental")]
file = file.dropna()

sixties = file[file['Year'] < 1970]
seventies = file[(file['Year'] < 1980) & (file['Year'] >= 1970)]
eighties = file[(file['Year'] < 1990) & (file['Year'] >= 1980)]
nineties = file[(file['Year'] < 2000) & (file['Year'] >= 1990)]
thousands = file[(file['Year'] < 2010) & (file['Year'] >= 2000)]
tens = file[(file['Year'] < 2020) & (file['Year'] >= 2010)]

sixties_score = sixties['Lyrics'] 
sixties_score = sixties_score.to_string()
sixties_score = ''.join(sixties_score)

seventies_score = seventies['Lyrics'] 
seventies_score = seventies_score.to_string()
seventies_score = ''.join(seventies_score)

eighties_score = eighties['Lyrics'] 
eighties_score = eighties_score.to_string()
eighties_score = ''.join(eighties_score)


nineties_score = nineties['Lyrics'] 
nineties_score = nineties_score.to_string()
nineties_score = ''.join(nineties_score)

thousands_score = thousands['Lyrics'] 
thousands_score = thousands_score.to_string()
thousands_score = ''.join(thousands_score)

tens_score = tens['Lyrics'] 
tens_score = tens_score.to_string()
tens_score = ''.join(tens_score)
#print(file)
from model import sentiment
func = sentiment()
six_data = func.tokener(sixties_score)

seven_data = func.tokener(seventies_score)

eight_data = func.tokener(eighties_score)

nine_data = func.tokener(nineties_score)

thousand_data = func.tokener(thousands_score)

ten_data = func.tokener(tens_score)

data = {'Year': ['1960s', '1970s', '1980s', '1990s', '2000s', '2010s'],
        'Sentiment Score': [six_data, seven_data, eight_data, nine_data, thousand_data, ten_data]
        }

df = pd.DataFrame(data, columns = ['Year', 'Sentiment Score'])
print(df)

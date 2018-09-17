# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 19:40:04 2018

@author: jattal
"""

import pickle
import pandas as pd
from textblob import TextBlob as tb

save_extract_nlp_info = "C:/Users/jattal/Documents/Python Scripts/TwitStream/Tests/save_nlp_info"
df = pd.DataFrame()


with open(save_extract_nlp_info,'rb') as f:
    mon_depickler = pickle.Unpickler(f)
    df = mon_depickler.load()
    
df["tb_lang_detect"]= "n.a"
df["tb_sentiment"] = 0

print(range(len(df)))

for index,row in df.iterrows():
    print(index,row["text"])
    wiki = tb(row["text"]) 
    
    row["tb_lang_detect"] = wiki.detect_language()
    
    row["tb_sentiment"] = wiki.sentiment

wiki = tb(df["text"].iloc[1]) 

df["tb_lang_detect"].iloc[1] = wiki.detect_language()

df["tb_sentiment"].iloc[1] = wiki.sentiment


# -*- coding: utf-8 -*-
"""
Created on Mon May 14 09:28:30 2018

@author: jattal
"""

import json
import csv
import pandas as pd


f = open('C:/Users/jattal/Documents/Python Scripts/TwitStream/tweetunitaire.json','r')

outfile = "output.csv"
print(f)
data = json.load(f)
f.close()
f = open('output.csv','w')
csv_file = csv.writer(f)
for item in data:
    f.writerow(item)
    

f.close()


df = pd.read_json('tweetStream0.json')
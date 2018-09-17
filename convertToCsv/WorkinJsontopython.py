# -*- coding: utf-8 -*-
"""
Created on Wed May 23 23:44:45 2018

@author: jattal
"""

import json
import pandas as pd
from pandas.io.json import json_normalize
import re


def check_dict(data_dict):
    for cle,valeur in data_dict.items():
        if isinstance(valeur,list):
            check_list(valeur)
        
        if isinstance(valeur,dict):
            check_dict(valeur)
 
        elif isinstance(valeur,str):
            newvalue = re.sub(r'\n','',valeur,0)
            newvalue = re.sub(r'\r','',newvalue,0)
            newvalue = re.sub(r'&gt','',newvalue,0)
            data_dict[cle]=newvalue
    return data_dict

        
def check_list(data_list):
    for cle, valeur in enumerate(data_list):
        if isinstance(valeur,dict):
            check_dict(valeur)
        elif isinstance(valeur,str):
            newvalue = re.sub(r'\n','',valeur,0)
            newvalue = re.sub(r'\r','',newvalue,0)
            newvalue = re.sub(r'&gt','',newvalue,0)
            data_list[cle]=newvalue
    return data_list


    

inputfile = 'C:/Users/jattal/Documents/Python Scripts/TwitStream/Tests/tweetStream0unix.json'
a={}
c=[]

with open(inputfile,'r') as f:
    for line in f:
        a=line
        b = json.loads(a)
        c.append(b)
#print(b)
df3=pd.DataFrame()
#for i in range(len(c)):
#    check_dict(c[i])
#    df = json_normalize(c[i],sep="_")
#    df3 = pd.concat([df3, df])
        
    
check_dict(c[2])
df = json_normalize(c[1],sep="_")
df2 = json_normalize(c[2],sep="_")
df3 = pd.concat([df, df2])
#----------------OK au dessus -----------------

#df = pd.DataFrame(c)
#df2 = pd.DataFrame(df["entities"])
#
df4=json_normalize(c,sep="_")

#df3 = pd.DataFrame(c)

df3.to_csv("C:/Users/jattal/Documents/Python Scripts/TwitStream/Tests/out.csv", encoding='utf-8', sep = "¦")

for i in range(len(c)):
    if c[i]["id"] == 994990153838903296:
        print(i)
#
#temp = df["entities"]
#temp2= temp.tolist()
##
#
#
#
#for i in df.columns:
#    temp = df[i]
#    temp2= temp.tolist()
#    print(df[i],temp,temp2)
#    temp3 = pd.DataFrame(temp2)
#    rows, column = temp3.shape
#    if column > 1:
#        for j in range(column):
#            dftemp=temp3.add_prefix(i+"_").append
#        
#temp2 = pd.DataFrame(temp2)
#rows, column = temp2.shape
#dftemp=pd.DataFrame()
#
#        
        
dftemp.to_csv("C:/Users/jattal/Documents/Python Scripts/TwitStream/Tests/out2.csv", encoding='utf-8', sep = "|")
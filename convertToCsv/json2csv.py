# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 13:29:35 2018

@author: jattal
"""

import json
import pandas as pd
from pandas.io.json import json_normalize
import re
import pickle


# # #  look for strings with \n and \r inside so it messes up the csv export # # # 
  # # check for the value &gt and &lt and replace it # # 
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

def check_web_adress(df):
    for index,row in df.iterrows():
        liste_web=[]
        liste_web=re.findall(r'(https?://\S+)',df["text"][index]) #text)
        if index%50==0:
            print(index)
        df["Nbr_link"][index]=len(liste_web)
        if len(liste_web) > 0:
            for i in range(len(liste_web)):
                link=''.join('link_'+str(i+1))
                df[link][index]=liste_web[i]
                df["text"][index]=re.sub(re.escape(liste_web[i]),'',df["text"][index],0)
                df["text"][index]=re.sub('  ',' ',df["text"][index],0)

    return df

def extract_nlp_info(df):
    if df["truncated"] is True:
        text="extended_tweet_full_text"
    else:
        text="text"
    extract = ["created_at","id","truncated",text,"user_id", "user_screen_name", 
               "user_statuses_count","user_lang","user_followers_count","user_friends_count",
               "favorite_count", "favorited","retweeted","reply_count","retweet_count"]
    df_extract=df[extract]
    df_extract["link_1"]=""
    df_extract["link_2"]=""
    df_extract["link_3"]=""
    df_extract["link_4"]=""
    df_extract["Nbr_link"]=""
    return df_extract

if __name__=='__main__':
    inputfile = 'C:/Users/jattal/Documents/Python Scripts/TwitStream/Tests/tweetStream0unix.json'
    a={}
    c=[]
    
    with open(inputfile,'r') as f:
        for line in f:
            a=line
            b = json.loads(a)
            c.append(b)

    df=pd.DataFrame()
    
    df=json_normalize(c,sep="_")
    
    df.to_csv("C:/Users/jattal/Documents/Python Scripts/TwitStream/Tests/out.csv", encoding='utf-8', sep = "¦")
    
    df_extract = extract_nlp_info(df)
    
    df_extract=check_web_adress(df_extract)
    
    save_extract_nlp_info = "C:/Users/jattal/Documents/Python Scripts/TwitStream/Tests/save_nlp_info"
    with open(save_extract_nlp_info, "wb") as f:
        mon_pickler = pickle.Pickler(f)
        mon_pickler.dump(df_extract)
        
        
        

    print(df_extract.iloc[10])
    
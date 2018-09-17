# -*- coding: utf-8 -*-
"""
Created on Tue May 15 23:34:22 2018

@author: jattal
"""
import sys
import urllib
import codecs
import json
import unicodecsv
import dateutil.parser as parser


infile  = "C:/Users/jattal/Documents/Python Scripts/TwitStream/tweetTest.json"
outfile = "output.csv"

writer = open(outfile, mode='w')#, delimiter=',', quotechar='"')

#for line in codecs.open(infile, 'r', 'utf8'):
#    print(line)
#    tweet = json.load(line,encoding='utf-8')
#    json.load()
#  # convert the created_at string to friendly ISO date
#  ts = (parser.parse(tweet['created_at']))
#
#  row = []
#  row.append(tweet['id'])
#  row.append(tweet['text'])
#  row.append(tweet['source'])
#  row.append(ts.strftime("%Y-%m-%d %H:%M:%S"))
#  row.append(tweet['user']['id'])
#  row.append(tweet['user']['name'])
#  row.append(tweet['user']['description'])
#  row.append(tweet['user']['location'])
#  row.append(tweet['user']['followers_count'])
#  row.append(tweet['user']['friends_count'])
#  row.append(tweet['user']['profile_image_url'])

#  print(row)
  #writer.writerow(row)
  
  
  
with open(infile) as json_data:
    d = json.load(json_data)
    

print(d)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
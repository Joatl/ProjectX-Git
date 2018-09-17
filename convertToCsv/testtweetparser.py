# -*- coding: utf-8 -*-
"""
Created on Fri May 18 20:38:57 2018

@author: jattal
"""

from tweet_parser.tweet import Tweet
from tweet_parser.tweet_parser_errors import NotATweetError
import fileinput
import json

for line in fileinput.FileInput("C:/Users/jattal/Documents/Python Scripts/TwitStream/tweetTest.json"):
    try:
        tweet_dict = json.loads(line)
        tweet = Tweet(tweet_dict)
    except (json.JSONDecodeError,NotATweetError):
        pass
    print(tweet.created_at_string, tweet.all_text)
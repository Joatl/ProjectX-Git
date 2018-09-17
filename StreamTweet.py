
# coding: utf-8
from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import os
import re

#re est pour les regex pour les noms de fichiers
#os est pour récupérer la taille du fichier

import twitter_credentials


# # # Test file size # # #

class TestFileSize:
    def __init__(self,fetched_tweets_filename, file_size_limit=None):
        self.file_name=fetched_tweets_filename
        self.file_size_limit = file_size_limit
        
    def get_file_size(self):
        file_size = os.stat(self.file_name).st_size
        return file_size

    def file_exist(self):
        if os.path.isfile(self.file_name) is False:
            open(self.file_name, 'a').close()
            
    def change_file_name(self): #-5 pour commencer au 5eme avant dernier caratère (avant l'extension)
        if self.get_file_size() >= file_size_limit:
            nb_file = int(re.search('tweetStream(.+?).txt', self.file_name).group(1)) + 1
            self.file_name= ''.join('tweetStream'+str(nb_file)+'.txt')
            self.file_exist()
            self.change_file_name()
            return self.file_name
        else:
            return self.file_name
    
        
# # # Twitter Client # # #

class TwitterClient():
    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)
        self.twitter_user = twitter_user
        
    def get_user_timeline_tweets(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets


# # # Twitter Authenticater # # #

class TwitterAuthenticator():
    
    def __init__(self):
        pass
    
    def authenticate_twitter_app(self):
        auth = OAuthHandler(twitter_credentials.Consumer_key,twitter_credentials.Consumer_secret)
        auth.set_access_token(twitter_credentials.Access_token,twitter_credentials.Access_secret)
        return auth
#les crédentials sont dans des variables dans un fichier à part pour que ce soit plus modulable

class TwitterStreamer():
    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()
    
    def stream_tweets(self, fetched_tweets_filename, hash_tag_list,file_size_limit=None):
        listener = TwitterListener(fetched_tweets_filename,file_size_limit)
        auth = self.twitter_authenticator.authenticate_twitter_app()
        stream = Stream(auth, listener)
        stream.filter(track=hash_tag_list)
    


#override tweepy.StreamListener to add logic to on_data
class TwitterListener(StreamListener):
    """
    Class permettant de récupérer des tweets et de les écrire dans un fichier .csv
    """
    
    def __init__(self, fetched_tweets_filename,file_size_limit):
        self.fetched_tweets_filename = fetched_tweets_filename
        self.file_size_limit = file_size_limit
    
    def on_data(self, data):
        try:
           # print(data)
            file = TestFileSize(fetched_tweets_filename,file_size_limit).change_file_name()
            with open(file, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on Data : %s" % str(e))
            return True

    def on_error(self, status):
        if status == 420:
            #returning false on_data method in case rate limit occurs
            print(status)
            return False
#        return True # Don't kill the stream



if __name__=='__main__':
    hash_tag_list = ['Bitcoin']
    fetched_tweets_filename = "tweetStream0.txt"
    TestFileSize(fetched_tweets_filename).file_exist()
    file_size_limit = 100000000
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename,hash_tag_list, file_size_limit)
    

#   affiche la taille du fichier en octet, 100 mo=100 000 000 octets
#print(os.stat('tweetStream.txt').st_size)






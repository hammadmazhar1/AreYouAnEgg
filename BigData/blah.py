import time
import tweepy
import json
import csv

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
ckey = 'dCR0q0WL1JULWcEoWXJdudCUF'
csecret = 'p6KuaGIPyLw5tgsyHlaT9cKYzXTCeeKpVFgfsNjCzZADHGwqbV'
atoken = '817207051-Hx7e9epWO7AbQyYSPduBZjwfOkuWlUfWj2OI06uy'
asecret= 'is7cVhaACtlI89pvVUkUGHv6JmjQ1K6uswLI32ZaEWKuh'


auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
auth.set_access_token(atoken,asecret)
#twitterStream = Stream(auth,listener())
api = tweepy.API(auth)

user = api.get_user('HmdMazhar')
print((user.friends()[3].name))
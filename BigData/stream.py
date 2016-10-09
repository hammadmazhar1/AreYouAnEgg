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

#ckey='SFFFtZHQH9W2hpTJAzNZgZdhg'
#csecret='YoJpnFFWpLa9TdWm3sd2Ks3cWOnZQXswgT51Jt7wyHhOkRkLvN'
#atoken='2615625900-yEM7Ny76MY2EFg44cM6fNpFotYFQa1eAWMvyaUi'
#asecret='dMxqQRpTyOrQzmFP3qq1gU7iDZyTPOxtWNQslNshuIzWi'
ver_acc_file = open('check_people.csv','r')
ver_reader =csv.reader(ver_acc_file)
rat_real_file = open('check_people_rat.csv','w')
rat_real_csv = csv.writer(rat_real_file,delimiter=",")
auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
auth.set_access_token(atoken,asecret)
#twitterStream = Stream(auth,listener())
api = tweepy.API(auth)
#user_file = open('fake_users.csv', 'r')
#user_reader = csv.reader(user_file)
k = 0
for i in ver_reader:
	if k < 150:
		k +=1
	else:
		break
	stuff = None
	try:
		stuff = api.user_timeline(screen_name = i[0], count = 200, include_rts = True)
	except tweepy.error.TweepError:
		continue
	else:
		retweets = 0
		tot_tweets =0
		for tweet in stuff:
			if 'RT @' in tweet.text[:4]:
				retweets +=1
			tot_tweets +=1
	#print('RT @' in tweet_one.text[:4])
	#print(dir(tweet_one))
		print(retweets)
		print(tot_tweets)
		try :
			rat =float(retweets)/float(tot_tweets)
		except ZeroDivisionError:
			continue
		else:
			print(i[0])
			print(rat)
			rat_real_csv.writerow([i[0],rat])
#stuff = api.user_timeline(screen_name = 'verified/lists/verified-accounts', count = 200, include_rts = True)
#stuff = api.user_timeline(screen_name = '5tonedReviewer', count = 10, include_rts = True)
#print(tweet_one.retweet_count)
#print(tweet_one.retweeted)
	
#print(api.get_user('verified').lists())
	
import time
import tweepy
import json
import csv, math
import threading
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

def retweet_ratios(reader,api,follower):
	for i in reader:
		csv_file = open("follower_ratios/"+i[0]+"_follower_rat.csv","w")
		csv_writer = csv.writer(csv_file,delimiter=",")
		csv_file2 = open("fo/"+i[0]+"_followers.csv","r")
		csv_reader = csv.reader(csv_file2)
		
		for row in csv_reader:
			try:
				stuff = api.user_timeline(screen_name = row[0], count = 200, include_rts = True)
			except tweepy.error.TweepError,Argument:
				print(Argument)
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
					rat = 1
				finally:
					print(i[0]+ "," + row[0]+",follower")
					print(rat)
					csv_writer.writerow([row[0],rat])
				time.sleep(5)
		csv_file.close()
		csv_file2.close()
		csv_file = open("following_ratios/"+i[0]+"_following_rat.csv","w")
		csv_writer = csv.writer(csv_file,delimiter=",")
		csv_file2 = open("fo/"+i[0]+"_following.csv","r")
		csv_reader = csv.reader(csv_file2)
		stuff = None
		for row in csv_reader:
			try:
				stuff = api.user_timeline(screen_name = row[0], count = 200, include_rts = True)
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
					rat = 1
				finally:
					print(i[0]+ "," + row[0]+",following")
					print(rat)
					csv_writer.writerow([row[0],rat])
			time.sleep(5)
		csv_file.close()
		csv_file2.close()

## add twitter app keys for each api in the form:
# ckey<num> = 'customer API key'
# csecret<num> = 'customer API secret'
# atoken<num> = 'application access token'
# asecret<num> = 'application secret'

ver_acc_file = open('real_people_rat.csv','r')
fake_acc_file = open('fake_people_rat.csv','r')
ver_acc_reader = list(csv.reader(ver_acc_file))
fake_acc_reader = list(csv.reader(fake_acc_file))

auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
auth.set_access_token(atoken,asecret)
#twitterStream = Stream(auth,listener())
api = tweepy.API(auth)

auth2 = OAuthHandler(ckey2,csecret2)
auth2.set_access_token(atoken2,asecret2)
auth2.set_access_token(atoken2,asecret2)
#twitterStream = Stream(auth,listener())
api2 = tweepy.API(auth2)

auth3 = OAuthHandler(ckey3,csecret3)
auth3.set_access_token(atoken3,asecret3)
auth3.set_access_token(atoken3,asecret3)
#twitterStream = Stream(auth,listener())
api3 = tweepy.API(auth3)

auth4 = OAuthHandler(ckey4,csecret4)
auth4.set_access_token(atoken4,asecret4)
auth4.set_access_token(atoken4,asecret4)
#twitterStream = Stream(auth,listener())
api4 = tweepy.API(auth4)

auth5 = OAuthHandler(ckey5,csecret5)
auth5.set_access_token(atoken5,asecret5)
auth5.set_access_token(atoken5,asecret5)
#twitterStream = Stream(auth,listener())
api5 = tweepy.API(auth5)

auth6 = OAuthHandler(ckey6,csecret6)
auth6.set_access_token(atoken6,asecret6)
auth6.set_access_token(atoken6,asecret6)
#twitterStream = Stream(auth,listener())
api6 = tweepy.API(auth6)

auth7 = OAuthHandler(ckey7,csecret7)
auth7.set_access_token(atoken7,asecret7)
auth7.set_access_token(atoken7,asecret7)
#twitterStream = Stream(auth,listener())
api7 = tweepy.API(auth7)

auth8 = OAuthHandler(ckey8,csecret8)
auth8.set_access_token(atoken8,asecret8)
auth8.set_access_token(atoken8,asecret8)
#twitterStream = Stream(auth,listener())
api8 = tweepy.API(auth8)

ver_reader1 = ver_acc_reader[:int(math.floor(0.25*len(ver_acc_reader)))]
ver_reader2= ver_acc_reader[int(math.ceil(0.25*len(ver_acc_reader))):int(math.floor(0.5*len(ver_acc_reader)))]
ver_reader3= ver_acc_reader[int(math.ceil(0.5*len(ver_acc_reader))):int(math.floor(0.75*len(ver_acc_reader)))]
ver_reader4= ver_acc_reader[int(math.ceil(0.75*len(ver_acc_reader))):]
fake_reader1 = fake_acc_reader[:int(math.floor(0.25*len(fake_acc_reader)))]
fake_reader2= fake_acc_reader[int(math.ceil(0.25*len(fake_acc_reader))):int(math.floor(0.5*len(fake_acc_reader)))]
fake_reader3= fake_acc_reader[int(math.ceil(0.5*len(fake_acc_reader))):int(math.floor(0.75*len(fake_acc_reader)))]
fake_reader4= fake_acc_reader[int(math.ceil(0.75*len(fake_acc_reader))):]

limit=200
t1 = threading.Thread(target=retweet_ratios,args=(ver_reader1,api,limit))
t1.daemon =True
t1.start()
t2 = threading.Thread(target=retweet_ratios,args=(ver_reader2,api2,limit))
t2.daemon =True
t2.start()
t3 = threading.Thread(target=retweet_ratios,args=(ver_reader3,api3,limit))
t3.daemon =True
t3.start()
t4 = threading.Thread(target=retweet_ratios,args=(ver_reader4,api4,limit))
t4.daemon =True
t4.start()

t5 = threading.Thread(target=retweet_ratios,args=(fake_reader1,api5,limit))
t5.daemon =True
t5.start()
t6 = threading.Thread(target=retweet_ratios,args=(fake_reader2,api6,limit))
t6.daemon =True
t6.start()
t7 = threading.Thread(target=retweet_ratios,args=(fake_reader3,api7,limit))
t7.daemon =True
t7.start()
t8 = threading.Thread(target=retweet_ratios,args=(fake_reader4,api8,limit))
t8.daemon =True
t8.start()
a = t1.join()
b = t2.join()
a = t3.join()
b = t4.join()
a = t5.join()
b = t6.join()
a = t7.join()
b = t8.join()	
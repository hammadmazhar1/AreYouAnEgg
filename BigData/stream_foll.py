import time
import tweepy
import json
import csv, math
import threading
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

#ckey='SFFFtZHQH9W2hpTJAzNZgZdhg'
#csecret='YoJpnFFWpLa9TdWm3sd2Ks3cWOnZQXswgT51Jt7wyHhOkRkLvN'
#atoken='2615625900-yEM7Ny76MY2EFg44cM6fNpFotYFQa1eAWMvyaUi'
#asecret='dMxqQRpTyOrQzmFP3qq1gU7iDZyTPOxtWNQslNshuIzWi'
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


# ver_acc_file = open('check_real_rat.csv','r')
# ver_acc_reader =csv.reader(ver_acc_file)
#fake_acc_file = open('fake_rat_full.csv','r')
#fake_reader = csv.reader(fake_acc_file)

ckey = 'dCR0q0WL1JULWcEoWXJdudCUF'
csecret = 'p6KuaGIPyLw5tgsyHlaT9cKYzXTCeeKpVFgfsNjCzZADHGwqbV'
atoken = '817207051-Hx7e9epWO7AbQyYSPduBZjwfOkuWlUfWj2OI06uy'
asecret= 'is7cVhaACtlI89pvVUkUGHv6JmjQ1K6uswLI32ZaEWKuh'

ckey2='SFFFtZHQH9W2hpTJAzNZgZdhg'
csecret2='YoJpnFFWpLa9TdWm3sd2Ks3cWOnZQXswgT51Jt7wyHhOkRkLvN'
atoken2='2615625900-yEM7Ny76MY2EFg44cM6fNpFotYFQa1eAWMvyaUi'
asecret2='dMxqQRpTyOrQzmFP3qq1gU7iDZyTPOxtWNQslNshuIzWi'

ckey3 = '31giOCItIOkAIe1KihD53JmeH'
csecret3 = 'U4XakK8ZR0AiPBqmmSlVJO4oC7VyBRaQOa6zq3CORgiU4xrnyl'
atoken3 = '2615625900-UXxKAETfgNpTwZNb9f0iAGFDnyo0DJkntPQXNHL'
asecret3= '1qkK3nDmuNs9PYgpSua9y5ZwYH5sVrW6T2j3YK76AI3ZV'


ckey4 = '2huVVfcN1IQ8khshoHellOnpP'
csecret4 = 'XFPjHdWWVYrY4Gt5EqymIokxdnFZ4O77bQYyLZ3tfrf21UZw6S'
atoken4 = '2615625900-398eOT4FePftTXnWaqzscJU6dN9VQcIIpScQcV5'
asecret4= 'pq4fRi9mvcpUBGQPqXVjDOI3MWnkkgD4uCfewwMhx8gW0'

ckey5 = 'BrSrE60fXrAzpdIFVlVEd0GeF'
csecret5 = 'TjRIICqpmdNWa9sHqW43Oi88w68CVgz8hn6RbTrPVlZmP24uWb'
atoken5 = '2615625900-zNbMDapIgWURp9VyIwNmLfHsMC8jdBJmraUsHxK'
asecret5= 'IO0xIbOIVSgQd6T44KwhLayHR94FbBkiiOTp8OVsZRK5u'

ckey6 = '9ldCKmRrC3AxugdlaexayuE9N'
csecret6 = 'gIfZHBmyTb4JsQUeNjMnaPHzeEsOL21dcLeSQQRs6AMg2YHULA'
atoken6 = '817207051-XoCUaz50aPUg7ynD6Ju6pXHFLfQpctcmlhn6xolH'
asecret6= 'HOayFz1O0zpoq41TY50pQUNskicyhdzPTqMjU0pM0p6Np'

ckey7 = 'R73aH39nidiKtCVRE4F2F2udg'
csecret7 = 'zCDCdUuhELb3uqgKt0tLZjhTavtOQmXYD53LoeQCDmEDMV5cDl'
atoken7 = '817207051-vzm1FMy8NVI5lc7Cf4a5wuwkNwwv2ocWr7hTSWH6'
asecret7= 'iiZvqveM8346fR553IUr1LPUQyKVnTR1pyf22nMw3OsJT'

ckey8 = '9lQCI6rxnwLlqSIihEJEUpv72'
csecret8 = 'tkDExltHuL9vI6Boui0gqBAJ7AyHnezwR7bQuR6TzvxGsYTaGB'
atoken8 = '817207051-ck6uWUB7imtOn9Ur6bNxbnt3Hk0kE3rZ7irO4rdw'
asecret8= 'tHNrQs7iiFOgnvbrwt4ZxlPoHPhENvIBwaPSHpGY9HzFB'

ver_acc_file = open('check_people_rat.csv','r')
#fake_acc_file = open('fake_rat_full.csv','r')
ver_acc_reader = list(csv.reader(ver_acc_file))
# fake_acc_reader = list(csv.reader(fake_acc_file))

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

# auth5 = OAuthHandler(ckey5,csecret5)
# auth5.set_access_token(atoken5,asecret5)
# auth5.set_access_token(atoken5,asecret5)
# #twitterStream = Stream(auth,listener())
# api5 = tweepy.API(auth5)

# auth6 = OAuthHandler(ckey6,csecret6)
# auth6.set_access_token(atoken6,asecret6)
# auth6.set_access_token(atoken6,asecret6)
# #twitterStream = Stream(auth,listener())
# api6 = tweepy.API(auth6)

# auth7 = OAuthHandler(ckey7,csecret7)
# auth7.set_access_token(atoken7,asecret7)
# auth7.set_access_token(atoken7,asecret7)
# #twitterStream = Stream(auth,listener())
# api7 = tweepy.API(auth7)

# auth8 = OAuthHandler(ckey8,csecret8)
# auth8.set_access_token(atoken8,asecret8)
# auth8.set_access_token(atoken8,asecret8)
# #twitterStream = Stream(auth,listener())
# api8 = tweepy.API(auth8)

# auth9 = OAuthHandler(ckey9,csecret9)
# auth9.set_access_token(atoken6,asecret6)
# auth9.set_access_token(atoken6,asecret6)
# #twitterStream = Stream(auth,listener())
# api9 = tweepy.API(auth9)

# auth10 = OAuthHandler(ckey10,csecret10)
# auth7.set_access_token(atoken7,asecret7)
# auth7.set_access_token(atoken7,asecret7)
# #twitterStream = Stream(auth,listener())
# api7 = tweepy.API(auth7)

# auth8 = OAuthHandler(ckey8,csecret8)
# auth8.set_access_token(atoken8,asecret8)
# auth8.set_access_token(atoken8,asecret8)
# #twitterStream = Stream(auth,listener())
# api8 = tweepy.API(auth8)
#stuff = api.user_timeline(screen_name = 'verified/lists/verified-accounts', count = 200, include_rts = True)
#stuff = api.user_timeline(screen_name = '5tonedReviewer', count = 10, include_rts = True)
#print(tweet_one.retweet_count)
#print(tweet_one.retweeted)
ver_reader1 = ver_acc_reader[:int(math.floor(0.25*len(ver_acc_reader)))]
ver_reader2= ver_acc_reader[int(math.ceil(0.25*len(ver_acc_reader))):int(math.floor(0.5*len(ver_acc_reader)))]
ver_reader3= ver_acc_reader[int(math.ceil(0.5*len(ver_acc_reader))):int(math.floor(0.75*len(ver_acc_reader)))]
ver_reader4= ver_acc_reader[int(math.ceil(0.75*len(ver_acc_reader))):]
# fake_reader1 = fake_acc_reader[:int(math.floor(0.25*len(fake_acc_reader)))]
# fake_reader2= fake_acc_reader[int(math.ceil(0.25*len(fake_acc_reader))):int(math.floor(0.5*len(fake_acc_reader)))]
# fake_reader3= fake_acc_reader[int(math.ceil(0.5*len(fake_acc_reader))):int(math.floor(0.75*len(fake_acc_reader)))]
# fake_reader4= fake_acc_reader[int(math.ceil(0.75*len(fake_acc_reader))):]

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

# t5 = threading.Thread(target=retweet_ratios,args=(fake_reader1,api5,limit))
# t5.daemon =True
# t5.start()
# t6 = threading.Thread(target=retweet_ratios,args=(fake_reader2,api6,limit))
# t6.daemon =True
# t6.start()
# t7 = threading.Thread(target=retweet_ratios,args=(fake_reader3,api7,limit))
# t7.daemon =True
# t7.start()
# t8 = threading.Thread(target=retweet_ratios,args=(fake_reader4,api8,limit))
# t8.daemon =True
# t8.start()
a = t1.join()
b = t2.join()
a = t3.join()
b = t4.join()
# a = t5.join()
# b = t6.join()
# a = t7.join()
# b = t8.join()




#print(api.get_user('verified').lists())
	
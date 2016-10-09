import time
import tweepy
import json
import csv
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ver_file = open('ver_2', "r")
lines = ver_file.readlines()
ver_list =[]
csv_file = open('ver_acc2.csv','w')
writer = csv.writer(csv_file)
for line in lines:
	j = json.dumps(line)
	#l = line.encode('utf_8', 'ignore')
	#print(l)
	line_str_idx = 0
	j=str(j)
	#print(j[39904:39934])
	sub_str_idx = 0
	while (True):
		sub_str_idx = j.find("data-screen-name=",line_str_idx)
		if (sub_str_idx == -1):
			break
		#print(sub_str_idx)
		#print(j[sub_str_idx:sub_str_idx+40])
		sub_str_idx = sub_str_idx+21
		sub_end_idx = j.find('\\',sub_str_idx)
		name = j[sub_str_idx:sub_end_idx]
		print name
		ver_list.append(name)
		line_str_idx =sub_end_idx
for i in set(ver_list):
	writer.writerow([i])
csv_file.close()

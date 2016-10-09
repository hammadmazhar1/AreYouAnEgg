import csv
import time

real_file=open("real_people_rat.csv","r")
fake_file=open("real_rat_full.csv","r")
label_inst=open("labelled_instances.csv","w")
real_reader=csv.reader(real_file)
fake_reader=csv.reader(fake_file)
label_inst_writer=csv.writer(label_inst,delimiter=",")
count = 1.0
tot= 0.0
for i in real_reader:
	try:
		followers = open("follower_ratios/"+i[0]+"_follower_rat.csv","r")
		friends = open("following_ratios/"+i[0]+"_following_rat.csv","r")
	except:
		continue
	else:
		follower_reader = csv.reader(followers)
		following_reader = csv.reader(friends)
		real_followers =0.0
		fake_followers =0.0
		real_following = 0.0
		fake_following = 0.0
		for j in follower_reader:
			print(j[1])
			if (float(j[1]) > 0.63):
				fake_followers +=1
			else:
				real_followers +=1
		for j in following_reader:
			if (float(j[1])> 0.63):
				fake_following +=1
			else:
				real_following +=1
		friend_purity =0.0
		follower_purity =0.0
		print(i[0]+"real_follower:"+str(real_followers)+",fake_follower:"+str(fake_followers))
		try:
			friend_purity=float(real_following)/float(real_following+fake_following)
		except ZeroDivisionError:
			friend_purity =tot/count
		try:
			follower_purity=float(real_followers)/float(real_followers+fake_followers)
		except ZeroDivisionError:
			follower_purity =0
		if count < 10:
			count+=1
			tot+=friend_purity

		label_inst_writer.writerow([i[0],i[1],friend_purity,follower_purity,0])
		followers.close()
		friends.close()

for i in fake_reader:
	try:
		followers = open("follower_ratios/"+i[0]+"_follower_rat.csv","r")
		friends = open("following_ratios/"+i[0]+"_following_rat.csv","r")
	except:
		continue
	else:
		follower_reader = csv.reader(followers)
		following_reader = csv.reader(friends)
		real_followers =0.0
		fake_followers =0.0
		real_following = 0.0
		fake_following = 0.0
		friend_purity =0.0
		follower_purity =0.0
		for j in follower_reader:
			if (float(j[1]) > 0.63):
				fake_followers +=1
			else:
				real_followers +=1
		for j in following_reader:
			if (float(j[1])> 0.63):
				fake_following +=1
			else: 	
				real_following +=1
		try:
			friend_purity=float(real_following)/float(real_following+fake_following)
		except ZeroDivisionError:
			friend_purity =tot/count
		try:
			follower_purity=float(real_followers)/float(real_followers+fake_followers)
		except ZeroDivisionError:
			follower_purity=0
		label_inst_writer.writerow([i[0],i[1],friend_purity,follower_purity,1])
	followers.close()
	friends.close()
label_inst.close()
real_file.close()
fake_file.close()

import urllib2, csv	
ver_lists=['ufc','cycling','world-leaders','nba','us-congress','spanish','cricket','olympians','basketball','soccer','baseball','foodies','business','india','technology','charity-ngo','music','entertainment','sports','politics']
ver_list =[]
csv_file = open('ver_acc.csv','w')
writer = csv.writer(csv_file)
for i in ver_lists:
	print(i)
	line =urllib2.urlopen("https://twitter.com/verified/lists/"+i+"/members").read()
	line_str_idx = 0
	sub_str_idx = 0
	while (True):
		sub_str_idx = line.find("data-screen-name=",line_str_idx)
		if (sub_str_idx == -1):
			break
		#print(sub_str_idx)
		#print(j[sub_str_idx:sub_str_idx+40])
		sub_str_idx = sub_str_idx+18
		sub_end_idx = line.find('\"',sub_str_idx)
		name = line[sub_str_idx:sub_end_idx]
		print name
		ver_list.append(name)
		line_str_idx =sub_end_idx
for i in set(ver_list):
	writer.writerow([i])

#get retweet ratios for real_people.csv and fake_people.csv
python stream.py

#get followers and friends for real_people and fake_people.csv
cd fo/
python find_foll.py
cd ..

#calculate retweet ratio for followers and following for real and fake people
python stream_foll.py

#create labelled instances for classifier
python make_labelled_instances.py


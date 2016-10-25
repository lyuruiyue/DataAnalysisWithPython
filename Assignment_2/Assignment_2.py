
# coding: utf-8

# In[4]:

import requests
import json
from requests_oauthlib import OAuth1
import os
from datetime import datetime
import pytz
import time

search_url = 'https://api.twitter.com/1.1/search/tweets.json?q='
search_term = input("Search:")

search_url = search_url + search_term + '&count=100'
    
consumer_key = 'ajPMhCizj8t5TWsMCBA3Hw3sb'
consumer_secret = '5jH2mzn59NQCV4KJP7Aiv1ZyuDN2pEvbAezAtNui3m7FQsMW36'
access_token = '789176579863695360-2qUKcpc0l8bA0QfP2ahwY8opWaZaQFY'
access_token_secret = 'CAyupgeqZq483QNXabcDMxKLnXuZOdOjwXxA7KgXT4sad'
auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)

results = requests.get(search_url, auth=auth)
better_results = results.json()

#search_term+'_'+tweet['created_at'][:-17]+'H'
if not os.path.exists(search_term):
    os.makedirs(search_term)

#fileObject = open(search_term+'/'+time.strftime("%Y-%m-%d %H-%M", time.localtime())+' Min'+'.json', 'w')
with open(search_term+'/'+time.strftime("%Y-%m-%d %H-%M", time.localtime())+' Min'+'.json', 'w') as f:
    f.write(json.dumps(better_results))
#for tweet in better_results['statuses']:
    
    #jsObj = json.dumps(tweet)
    #fileObject.write(jsObj)
#fileObject.close()
f.close()


# In[5]:

import requests
import json
from requests_oauthlib import OAuth1
import os
from datetime import datetime
import pytz
import time
from geopy.geocoders import Nominatim

geolocator = Nominatim()
search_url = 'https://api.twitter.com/1.1/search/tweets.json?q='

search_term = input("Search:")
location = input("location:")
location = geolocator.geocode(location)

max_range = 10
geocode = "%f,%f,%dmi" % (location.latitude, location.longitude, max_range)
url = search_url + search_term+ "&geocode="+ geocode+"&count=100"

consumer_key = 'ajPMhCizj8t5TWsMCBA3Hw3sb'
consumer_secret = '5jH2mzn59NQCV4KJP7Aiv1ZyuDN2pEvbAezAtNui3m7FQsMW36'
access_token = '789176579863695360-2qUKcpc0l8bA0QfP2ahwY8opWaZaQFY'
access_token_secret = 'CAyupgeqZq483QNXabcDMxKLnXuZOdOjwXxA7KgXT4sad'
auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)

results = requests.get(url, auth=auth)
better_results = results.json()
if not os.path.exists(search_term+'_with_location'):
    os.makedirs(search_term+'_with_location')
with open(search_term+'_with_location'+'/'+time.strftime("%Y-%m-%d %H-%M", time.localtime())+' Min'+'.json', 'w') as f:
    f.write(json.dumps(better_results))
f.close()


# ## 1.Average followers of user who tweet about the search keyword
# ## 2.Tweets amount in Boston and New York related to the keyword
# ## 3.Day which tweets post the most
# ## 4.Top 10 retweeted twitter related to the search keyword and location
# ## 5.Top influential tweet related to the search keyword and location

# In[3]:

import os
import json

num =input("which analysis?")
#root_dir = input("which directory")

root_dir = 'Vote Trump'
count1 = 0
followers = []
locations = []
days = []
for parent, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        filepath = parent + os.sep + filename
        if filepath.endswith(".json"):
            myfile = open(filepath)
            data = json.load(myfile)
            for value in data["statuses"]:
                followers.append(value["user"]["followers_count"])
                locations.append(value["user"]["location"])
                days.append(value["created_at"])
if (num in "1"):
    sum = 0
    for i in range(len(followers)):
        sum = sum + int(followers[i])
        avg = sum/len(followers)
    print("The average followers of '%s' is %f" %(root_dir,avg))

if (num in "2"):
    count1 =0
    for i in range(len(locations)):
        city = locations[i].split(",")
        if(city[0] not in " "):
            if(city[0]in 'NYCNew YorkNew York CityBuffaloRochesterYonkersSyracuseAlbanyNew RochelleCheektowagaMount VernonSchenectadyUticaBrentwoodTonawanda CDPWhite PlainsHempsteadLevittown'):
                count1 = count1 +1
    print ("NY: %d" %count1)

    count2=0
    for i in range(len(locations)):
        city = locations[i].split(",")
        if(city[0] not in " "):
            if(city[0]in 'MABostonmassachusettsWorcesterSpringfieldLowellCambridgeNew BedfordBrocktonQuincyLynnFall RiverNewtonSomervilleLawrenceFraminghamWalthamHaverhillLexington'):
                count2 = count2 +1
    print ("MA: %d" %count2)

if (num in "3"):
    m=0
    t=0
    w=0
    r=0
    f=0
    sat=0
    sun=0
    dic={}
    for i in range(len(days)):
        day = days[i][:3]
        if day in "Mon":
            m=m+1
        if day in "Tue":
            t=t+1
        if day in "Wed":
            w=w+1
        if day in "Thu":
            r=r+1
        if day in "Fri":
            f=f+1
        if day in "Sat":
            sat=sat+1
        if day in "Sun":
            sun=sun+1
    dic.update({"Mon":m})
    dic.update({"Tue":t})
    dic.update({"Wed":w})
    dic.update({"Thu":r})
    dic.update({"Fri":f})
    dic.update({"Sat":sat})
    dic.update({"Sun":sun})
    dict = sorted(dic.items(), key = lambda d:d[1], reverse = True)
    print ("Most people tweet %s on %s"%(root_dir,dict[0]))
if (num in "4"):
    root_dir = "Trump_with_location"
    top_ten_dic={}
    for parent, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            filepath = parent + os.sep + filename
            if filepath.endswith(".json"):
                myfile = open(filepath)
                data = json.load(myfile)
                for value in data["statuses"]:
                    top_ten_dic.update({value["text"]:value["retweet_count"]})
    top_ten_dict = sorted(top_ten_dic.items(), key = lambda d:d[1], reverse = True)
    print("The top 10 retweeted twitters in %s are:" %(root_dir[:-14]))
    for i in range(10):
        print (top_ten_dict[i])
if (num in "5"):
    root_dir = "Trump_with_location"
    top_inf_dic={}
    for parent, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            filepath = parent + os.sep + filename
            if filepath.endswith(".json"):
                myfile = open(filepath)
                data = json.load(myfile)
                for value in data["statuses"]:
                    top_inf_dic.update({value["text"]:value["retweet_count"]*value["user"]["followers_count"]})
    top_inf_dict = sorted(top_inf_dic.items(), key = lambda d:d[1], reverse = True)
    print ("The top influential tweet is:")
    print (top_inf_dict[0])


# In[ ]:




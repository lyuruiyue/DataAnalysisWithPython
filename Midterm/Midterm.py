
# coding: utf-8

# In[21]:

import requests
import time
import os
import json

key = '&key=CYsmhq4XXxO6Rq2gvfjPpw(('

for i in range(1,6):
    r = requests.get('https://api.stackexchange.com/2.2/questions/no-answers?page=%d&order=desc&sort=activity&tagged=python&site=stackoverflow%s' %(i,key))
    json_r =r.json()
    if not os.path.exists("stack_exchange_result"):
        os.makedirs("stack_exchange_result")
    with open("stack_exchange_result"+'/'+time.strftime("%Y-%m-%d %H-%M", time.localtime())+' Min_%d'%(i)+'.json', 'w') as f:
        f.write(json.dumps(json_r))
    f.close()


# In[13]:

root_dir = "stack_exchange_result"
no_answer_dic = {}
question_id = []
for parent, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        filepath = parent + os.sep + filename
        if filepath.endswith(".json"):
            myfile = open(filepath)
            data = json.load(myfile)
            for value in data["items"]:
                no_answer_dic.update({value["title"]:value["view_count"]})
                question_id.append(value["question_id"])
no_answer_dic = sorted(no_answer_dic.items(),key = lambda d:d[1], reverse = True)
for i in range(10):
    print (no_answer_dic[i])                


# In[28]:

bounty_dic = {}
for i in range(len(question_id)):
    r = requests.get('https://api.stackexchange.com/2.2/questions/%d?order=desc&sort=activity&site=stackoverflow%s'%(question_id[i],key) )
    json_result =r.json()
    
    for value in json_result['items']:
        if("bounty_amount" in value):
            bounty_dic.update({value["title"]:value["bounty_amount"]})
bounty_dic = sorted(bounty_dic.items(),key = lambda d:d[1], reverse = True)
for i in range(len(bounty_dic)):
    print (bounty_dic[i]) 


# In[16]:

for i in range(1,6):
    r = requests.get('https://api.stackexchange.com/2.2/answers?page=%d&order=desc&sort=votes&site=stackoverflow%s' %(i,key))
    json_r =r.json()
    if not os.path.exists("stack_exchange_answer_result"):
        os.makedirs("stack_exchange_answer_result")
    with open("stack_exchange_answer_result"+'/'+time.strftime("%Y-%m-%d %H-%M", time.localtime())+' Min_%d'%(i)+'.json', 'w') as f:
        f.write(json.dumps(json_r))
    f.close()


# In[39]:

root_dir = "stack_exchange_answer_result"
user_id = []
weightage_dic={}
for parent, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        filepath = parent + os.sep + filename
        if filepath.endswith(".json"):
            myfile = open(filepath)
            data = json.load(myfile)
            for value in data["items"]:
                if("user_id" in value['owner']):
                    user_id.append(value["owner"]["user_id"])
                    r = requests.get('https://api.stackexchange.com/2.2/users/%d?order=desc&sort=reputation&site=stackoverflow%s' %(value["owner"]["user_id"],key))
                    json_r =r.json()    
                    for badge in json_r['items']:
                        name = badge['display_name']
                        weightage=badge['badge_counts']['bronze'] + badge['badge_counts']['silver']*2 + badge['badge_counts']['gold']*3
                    weightage_dic.update({name:weightage})
weightage_dic = sorted(weightage_dic.items(),key = lambda d:d[1], reverse = True)
for i in range(len(weightage_dic)):
    print (weightage_dic[i]) 


# In[53]:

name=[]
userid = []
for i in range(5):
    r = requests.get('https://api.stackexchange.com/2.2/users/%d/badges?order=desc&sort=rank&site=stackoverflow%s' %(user_id[i],key))
    json_r =r.json()
    for value in json_r['items']:
        if(value['name'] == "Teacher"):
            name.append(value['user']['display_name'])
            userid.append(value['user']['user_id'])
for i in range(len(name)):
    print (name[i])


# In[59]:

import random
title =[]
for i in range(len(userid)):
    r = requests.get('https://api.stackexchange.com/2.2/users/%d/favorites?order=desc&sort=activity&site=stackoverflow%s' %(userid[i],key))
    json_r =r.json()
    for value in json_r['items']:
        title.append(value['title'])
for i in range(5):
    pos = random.randint(0,len(title)-1)
    print (title[pos])



# coding: utf-8

# In[1]:

import pandas as pd
frames = []
for i in range(1,17):
    frames.append(pd.read_csv(r'data\dataset%d.csv'%(i), error_bad_lines=False,sep=';'))
us_election = pd.concat(frames,ignore_index=True)


# In[2]:

us_election.head()


# In[2]:

import random
state = set()
for i in range(3113):
    if (type(us_election.ST[i]) is not float):
        state.add(us_election.ST[i])
data = random.sample(range(50),10)
select_state =set()
for i in range(10):
    select_state.add(list(state)[data[i]])

states = list(select_state)


# In[3]:

df3 = pd.DataFrame({'State':'','Year':0,'Party':'Republicans','Mean':0},range(3))
df4 = pd.DataFrame({'State':'','Year':0,'Party':'Democrats','Mean':0},range(3))
df5 = pd.DataFrame({'State':'','Year':0,'Party':'','Mean':0},range(0))
df5


# In[4]:

from numpy import mean
for i in range(10):
    republicans_16 = []
    republicans_12 = []
    republicans_08 = []
    democrats_16 = []
    democrats_12 = []
    democrats_08 = []
    for j in range(3113):
        if us_election.ST[j] == states[i]:
            republicans_16.append(us_election['Republicans 2016'][j])
            republicans_12.append(us_election['Republicans 2012'][j])
            republicans_08.append(us_election['Republicans 2008'][j])
            democrats_16.append(us_election['Democrats 2016'][j])
            democrats_12.append(us_election['Democrats 2012'][j])
            democrats_08.append(us_election['Democrats 2008'][j])
    r_mean_2016 = mean(republicans_16)
    r_mean_2012 = mean(republicans_12)
    r_mean_2008 = mean(republicans_08)
    d_mean_2016 = mean(democrats_16)
    d_mean_2012 = mean(democrats_12)
    d_mean_2008 = mean(democrats_08)
    
    df3.loc[0,'Mean'] = r_mean_2016
    df3.loc[1,'Mean'] = r_mean_2012
    df3.loc[2,'Mean'] = r_mean_2008
    df3.loc[0,'State'] = states[i]
    df3.loc[1,'State'] = states[i]
    df3.loc[2,'State'] = states[i]
    df3.loc[0,'Year'] = 2016
    df3.loc[1,'Year'] = 2012
    df3.loc[2,'Year'] = 2008
    df5 = pd.concat([df5,df3])
    df4.loc[0,'Mean'] = d_mean_2016
    df4.loc[1,'Mean'] = d_mean_2012
    df4.loc[2,'Mean'] = d_mean_2008
    df4.loc[0,'State'] = states[i]
    df4.loc[1,'State'] = states[i]
    df4.loc[2,'State'] = states[i]
    df4.loc[0,'Year'] = 2016
    df4.loc[1,'Year'] = 2012
    df4.loc[2,'Year'] = 2008
    df5 = pd.concat([df5,df4])
df5


# In[5]:

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic('matplotlib inline')
g = sns.factorplot(x="State", y="Mean", hue="Year",col="Party", data=df5)
plt.savefig("Republicans_and_Democrats_2008_2012_2016.png")


# In[6]:

df5.to_csv('Analysis4_output.csv', sep='\t',encoding='utf-8')


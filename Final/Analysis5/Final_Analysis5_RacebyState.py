
# coding: utf-8

# In[1]:

import pandas as pd
frames = []
for i in range(1,17):
    frames.append(pd.read_csv(r'data\dataset%d.csv'%(i), error_bad_lines=False,sep=';'))
us_election = pd.concat(frames,ignore_index=True)


# In[39]:

us_election.shape


# In[2]:

state = set()
for i in range(3113):
    if (type(us_election.ST[i]) is not float):
        state.add(us_election.ST[i])
state_list = list(state)
df3 = pd.DataFrame({'Votes':0,'Total':0},index = state_list)

for i in range(3113):
    if(us_election.ST[i] in state):
        df3.loc[us_election.ST[i],'Votes'] = df3.loc[us_election.ST[i],'Votes'] + us_election['Trump D'][i]
        df3.loc[us_election.ST[i],'Total'] = df3.loc[us_election.ST[i],'Total'] + us_election['votes'][i]
df3.shape


# In[3]:

vote_rate_dic = {}
for i in range(50):
    rate = df3.loc[state_list[i],'Votes']/df3.loc[state_list[i],'Total']
    vote_rate_dic.update({state_list[i]:rate})
vote_rate_dic = sorted(vote_rate_dic.items(),key = lambda d:d[1], reverse = True)
result = []
for i in range(5):
    result.append(str(vote_rate_dic[i])[2:4])
for i in range(5):
    result.append(str(vote_rate_dic[i+45])[2:4])
result


# In[4]:

#df3 = pd.DataFrame({'White not Latino':0,'African American':0,'Native American':0,'Asian American':0,'Latino':0,'Other races':0},index = result)
df3 = pd.DataFrame({'Race':'','Percent':0},index = result)
df3


# In[5]:

#White not Latino
pres_WNL =[]
#African American
pres_AA = []
#Native American
pres_NA = []
#Asian American
pres_AsA = []
#Latino
pres_L = []
#Others
pres_O = []
for i in range(10):
    WNL= 0
    AA=0
    NA=0
    AsA=0
    L=0
    O=0
    total = 0
    for j in range(3113):
        if us_election.ST[j] == result[i]:
            WNL= WNL + (us_election['White.not.Latino.Population'][j] * us_election['Total.Population'][j])
            AA= AA + (us_election['African.American.Population'][j] * us_election['Total.Population'][j])
            NA = NA + (us_election['Native.American.Population'][j]* us_election['Total.Population'][j])
            AsA = AsA + (us_election['Asian.American.Population'][j]* us_election['Total.Population'][j])
            L = L + (us_election['Latino.Population'][j]* us_election['Total.Population'][j])
            O = O + (us_election['Population.some.other.race.or.races'][j]* us_election['Total.Population'][j])
            total = total + us_election['Total.Population'][j]
    pres_WNL.append(WNL/total)
    pres_AA.append(AA/total)
    pres_NA.append(NA/total)
    pres_AsA.append(AsA/total)
    pres_L.append(L/total)
    pres_O.append(O/total)


# In[31]:

print(pres_WNL)


# In[6]:

import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
n = len(pres_O)
index = np.arange(n)
bar_width = 0.15
rects1 = plt.bar(index, pres_WNL, bar_width,
                 color='r',
                 label='White not Latino')
rects2 = plt.bar(index + bar_width, pres_AA, bar_width,
                 color='k',
                 label='African American')
rects3 = plt.bar(index + bar_width*2, pres_NA, bar_width,
                 color='g',
                 label='Native American')
rects4 = plt.bar(index + bar_width*3, pres_AsA, bar_width,
                 color='y',
                 label='Asian American')
rects5 = plt.bar(index + bar_width*4, pres_L, bar_width,
                 color='b',
                 label='Latino')
rects6 = plt.bar(index + bar_width*5, pres_O, bar_width,
                 color='m',
                 label='Others')

plt.xlabel('State')
plt.ylabel('Presentage')
plt.title('Race Presentage in States')

plt.xticks(index+bar_width*3.5, result)
ax.legend(loc='upper center',bbox_to_anchor=(0.5, -0.15),
          ncol=3, fancybox=True)
plt.tight_layout()
plt.savefig('Race_Presentage_in_States.png')
plt.show()



# coding: utf-8

# In[1]:

import pandas as pd

data1 = pd.read_csv(r'data\dataset1.csv', error_bad_lines=False,sep=';')
data2 = pd.read_csv(r'data\dataset2.csv', error_bad_lines=False,sep=';')
data3 = pd.read_csv(r'data\dataset3.csv', error_bad_lines=False,sep=';')
data4 = pd.read_csv(r'data\dataset4.csv', error_bad_lines=False,sep=';')
frames = [data1,data2,data3,data4]
us_election = pd.concat(frames,ignore_index=True)


# In[2]:

us_election.head(10)


# In[3]:

state = set()
for i in range(3113):
    if (type(us_election.ST[i]) is not float):
        state.add(us_election.ST[i])
state_list = list(state)
votes_in_state_df = pd.DataFrame({'Votes':0,'Total':0},index = state_list)
votes_in_state_df.shape


# In[4]:

for i in range(3113):
    if(us_election.ST[i] in state):
        votes_in_state_df.loc[us_election.ST[i],'Votes'] = votes_in_state_df.loc[us_election.ST[i],'Votes'] + us_election['Trump D'][i]
        votes_in_state_df.loc[us_election.ST[i],'Total'] = votes_in_state_df.loc[us_election.ST[i],'Total'] + us_election['votes'][i]
votes_in_state_df


# In[5]:

vote_rate_dic = {}
for i in range(50):
    rate = votes_in_state_df.loc[state_list[i],'Votes']/votes_in_state_df.loc[state_list[i],'Total']
    vote_rate_dic.update({state_list[i]:rate})
vote_rate_dic = sorted(vote_rate_dic.items(),key = lambda d:d[1], reverse = True)
#State that Trump has the highest vote rate
ST_T = str(vote_rate_dic[0])[2:4]
#State that Hillary has the highest vote rate
ST_H = str(vote_rate_dic[49])[2:4]


# In[6]:

#Management professional and related occupations
MPRO_T = []
MPRO_H = []
#Service occupations
SO_T = []
SO_H = []
#Sales and office occupations
SOO_T = []
SOO_H = []
#Farming fishing and forestry occupations
FFFO_T = []
FFFO_H = []
#Construction extraction maintenance and repair occupations
CEMRO_T = []
CEMRO_H = []
#Production transportation and material moving occupations
PTMMO_T = []
PTMMO_H = []
County_T = []
County_H = []
for i in range(3113):
    if us_election.ST[i] == ST_T:
        MPRO_T.append(us_election['Management.professional.and.related.occupations'][i])
        SO_T.append(us_election['Service.occupations'][i])
        SOO_T.append(us_election['Sales.and.office.occupations'][i])
        FFFO_T.append(us_election['Farming.fishing.and.forestry.occupations'][i])
        CEMRO_T.append(us_election['Construction.extraction.maintenance.and.repair.occupations'][i])
        PTMMO_T.append(us_election['Production.transportation.and.material.moving.occupations'][i])
        County_T.append(us_election['County'][i])
    if us_election.ST[i] == ST_H:
        MPRO_H.append(us_election['Management.professional.and.related.occupations'][i])
        SO_H.append(us_election['Service.occupations'][i])
        SOO_H.append(us_election['Sales.and.office.occupations'][i])
        FFFO_H.append(us_election['Farming.fishing.and.forestry.occupations'][i])
        CEMRO_H.append(us_election['Construction.extraction.maintenance.and.repair.occupations'][i])
        PTMMO_H.append(us_election['Production.transportation.and.material.moving.occupations'][i])
        County_H.append(us_election['County'][i])


# In[7]:

import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
n = len(MPRO_T)
index = np.arange(n)
bar_width = 0.1
rects1 = plt.bar(index, MPRO_T, bar_width,
                 color='b',
                 label='Management')
rects2 = plt.bar(index + bar_width, SO_T, bar_width,
                 color='m',
                 label='Service')
rects3 = plt.bar(index + bar_width*2, SOO_T, bar_width,
                 color='r',
                 label='Sales')
rects4 = plt.bar(index + bar_width*3, FFFO_T, bar_width,
                 color='y',
                 label='Farming')
rects5 = plt.bar(index + bar_width*4, CEMRO_T, bar_width,
                 color='k',
                 label='Construction')
rects6 = plt.bar(index + bar_width*5, PTMMO_T, bar_width,
                 color='g',
                 label='Transportation')

plt.xlabel('County')
plt.ylabel('Rate')
plt.title('The work occupations in '+ST_T)
#plt.legend((rects1[0],rects2[0],rects3[0],rects4[0],rects5[0],rects6[0]),('Management','Service','Sales','Farming','Construction','Transportation'))

ax.legend(loc='upper center',bbox_to_anchor=(0.5, -0.5),
          ncol=3, fancybox=True)
plt.xticks(index+bar_width*3, County_T, rotation='vertical')
plt.tight_layout()
plt.savefig('Work_Occupation_in_%s.png'%(ST_T))
plt.show()


# In[8]:

fig, ax = plt.subplots()
n2 = len(MPRO_H)
index2 = np.arange(n2)
bar_width2 = 0.1
rects7 = plt.bar(index2, MPRO_H, bar_width,
                 color='b',
                 label='Management')
rects8 = plt.bar(index2 + bar_width, SO_H, bar_width,
                 color='m',
                 label='Service')
rects9 = plt.bar(index2 + bar_width*2, SOO_H, bar_width,
                 color='r',
                 label='Sales')
rects10 = plt.bar(index2 + bar_width*3, FFFO_H, bar_width,
                 color='y',
                 label='Farming')
rects11 = plt.bar(index2 + bar_width*4, CEMRO_H, bar_width,
                 color='k',
                 label='Construction')
rects12 = plt.bar(index2 + bar_width*5, PTMMO_H, bar_width,
                 color='g',
                 label='Transportation')

plt.xlabel('County')
plt.ylabel('Rate')
plt.title('The work occupations in '+ST_H)

ax.legend(loc='upper center',bbox_to_anchor=(0.5, -0.15),
          ncol=3, fancybox=True)

plt.xticks(index2+bar_width2*3, County_H)
plt.tight_layout()
plt.savefig('Work_Occupation_in_%s.png'%(ST_H))
plt.show()


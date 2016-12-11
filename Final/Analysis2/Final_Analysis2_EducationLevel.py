
# coding: utf-8

# In[6]:

import pandas as pd
frames = []
for i in range(1,17):
    frames.append(pd.read_csv(r'data\dataset%d.csv'%(i), error_bad_lines=False,sep=';'))
us_election = pd.concat(frames,ignore_index=True)


# In[2]:

us_election.head()


# In[7]:

location = input("State:")
education_level_df = us_election[['ST','Clinton H','Trump D','Less.Than.High.School','At.Least.High.School.Diploma','At.Least.Bachelor.s.Degree','Total.Population']]
less_highschool = 0
highschool= 0
great_highschool = 0
sum_H = 0
sum_T = 0
total_population = 0

for i in range(3113):
    if education_level_df.ST[i] == location:
        less_highschool = less_highschool + education_level_df['Less.Than.High.School'][i] * education_level_df['Total.Population'][i] * 0.01
        highschool = highschool + (education_level_df['At.Least.High.School.Diploma'][i] - education_level_df['At.Least.Bachelor.s.Degree'][i]) * education_level_df['Total.Population'][i] * 0.01
        great_highschool = great_highschool + education_level_df['At.Least.Bachelor.s.Degree'][i] * education_level_df['Total.Population'][i] * 0.01
        sum_H += education_level_df['Clinton H'][i]
        sum_T += education_level_df['Trump D'][i]


# In[4]:

education_level_df.head()


# In[8]:

import seaborn as sns
from matplotlib import pyplot as plt
get_ipython().magic('matplotlib inline')
if sum_T > sum_H:
    print("Trump has higher vote")
else:
    print("Hillary has higher vote")
labels = 'Less Than High School','High School','At Least Bachelor'
sizes = [less_highschool,highschool,great_highschool]
colors = ['yellowgreen', 'gold', 'skyblue']
explode = (0.1, 0, 0)
plt.pie(sizes, explode=explode,labels=labels, autopct='%1.1f%%', colors=colors, shadow=True, startangle=90)

plt.axis('equal')
plt.savefig("education_level_by_county.png")
plt.title('Education level in '+location)
plt.show()


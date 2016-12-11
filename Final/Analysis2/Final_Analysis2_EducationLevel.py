
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

us_election.head()


# In[3]:

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


# In[5]:

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


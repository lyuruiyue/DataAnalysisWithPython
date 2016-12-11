
# coding: utf-8

# In[1]:

import pandas as pd
frames = []
for i in range(1,17):
    frames.append(pd.read_csv(r'data\dataset%d.csv'%(i), error_bad_lines=False,sep=';'))
us_election = pd.concat(frames,ignore_index=True)


# In[2]:

us_election.shape


# In[3]:

us_election.head(10)


# In[2]:

location = input("State:")
votes_by_county_df = us_election[['ST','County','Clinton H','Trump D']]
county = []
vote_T = []
vote_H = []
name_T = []
name_H = []
sum_T = 0
sum_H = 0

for i in range(3113):
    if votes_by_county_df.ST[i] == location:
        county.append(votes_by_county_df['County'][i])
        vote_T.append(votes_by_county_df['Trump D'][i])
        vote_H.append(votes_by_county_df['Clinton H'][i])
        name_H.append('Clinton H')
        name_T.append('Trump D')
        sum_H += votes_by_county_df['Clinton H'][i]
        sum_T += votes_by_county_df['Trump D'][i]
df3 = pd.DataFrame({'County':county,'Name':name_T,'Vote':vote_T})
df4 = pd.DataFrame({'County':county,'Name':name_H,'Vote':vote_H})
mean_T = sum_T/len(county)
mean_H = sum_H/len(county)
result_df = pd.concat([df3,df4])

result_df


# In[3]:

import seaborn as sns
from matplotlib import pyplot as plt
get_ipython().magic('matplotlib inline')
ax=sns.factorplot(x='County',y='Vote',data = result_df,hue="Name",aspect =3)
ax.set_xticklabels(rotation = 45)
plt.axhline(y=mean_T,color='b',ls='dashed')
plt.axhline(y=mean_H,color='g',ls='dashed')
if sum_T > sum_H:
    print("Trump has higher vote")
else:
    print("Hillary has higher vote")
plt.title('Votes Result in '+location)
plt.savefig("vote_result_by_county.png")


# In[9]:

location


# In[4]:

from bokeh.io import show, output_notebook
from bokeh.models import (
    ColumnDataSource,
    HoverTool,
    LogColorMapper
)
from bokeh.palettes import Viridis6 as palette
from bokeh.plotting import figure
import bokeh
bokeh.sampledata.download()
from bokeh.sampledata.us_counties import data as counties
from bokeh.sampledata.unemployment import data as unemployment

palette.reverse()

counties = {
    code: county for code, county in counties.items() if county["state"] == location.lower()}

county_xs = [county["lons"] for county in counties.values()]
county_ys = [county["lats"] for county in counties.values()]

county_names = [county['name'] for county in counties.values()]
county_rates = [unemployment[county_id] for county_id in counties]
vote_trump = vote_T
vote_hillary = vote_H
color_mapper = LogColorMapper(palette=palette)

source = ColumnDataSource(data=dict(
    x=county_xs,
    y=county_ys,
    name=county_names,
    rate=vote_trump,
    rate2=vote_hillary,
))

TOOLS = "reset,hover,save"

p = figure(
    title="Results in " +location, tools=TOOLS,
    x_axis_location=None, y_axis_location=None
)
p.grid.grid_line_color = None

p.patches('x', 'y', source=source,
          fill_color={'field': 'rate', 'transform': color_mapper},
          fill_alpha=0.7, line_color="white", line_width=0.5)

hover = p.select_one(HoverTool)
hover.point_policy = "follow_mouse"
hover.tooltips = [
    ("Name", "@name"),
    ("Vote Trump", "@rate"),
    ("Vote Hillary", "@rate2"),
    ("(Long, Lat)", "($x, $y)"),
]

output_notebook()
show(p,notebook_handle=True)


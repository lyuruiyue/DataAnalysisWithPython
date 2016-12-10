# Final

Dataset: usa-2016-presidential-election-by-county.csv   Downloaded from [usa-2016-presidential-election-by-county](https://data.opendatasoft.com/explore/dataset/usa-2016-presidential-election-by-county@public/)
   The total size is 288MB, so I split the file into several smaller files.
After read all the csv files, the dataframe has 3113 rows and 145 columns
![image](https://github.com/lyuruiyue/DataAnalysisWithPython/raw/master/Final/dataset.PNG)


## VoteByCounty
### Users could use this analysis to see how many votes that Trump and Hillary got in each county of a state.
* Read the csv files using pandas and then concatenate them into one dataframe.
* Let the users to input a state code(like MA, CA, TX...)
* Select the needed data from orignal dataframe to form a new dataframe
* Calculate the total votes that Trump and Hillary got from each county, get the mean value
![image](https://github.com/lyuruiyue/DataAnalysisWithPython/raw/master/Final/Analysis1/votes_in_MA.PNG)
* Print who has higher votes in that state
* Create the graph, x = county, y = total votes, and two lines show the mean value
![image](https://github.com/lyuruiyue/DataAnalysisWithPython/raw/master/Final/Analysis1/vote_result_by_MA.PNG)

## EducationLevel
### Users could use this analysis to get the education level of a state.
* Let the user to input a state code(like MA, CA, TX...) 
* Select the needed data from orignal dataframe to form a new dataframe
![image](https://github.com/lyuruiyue/DataAnalysisWithPython/raw/master/Final/Analysis2/education_df.PNG)
* Calculate the percent of population that the education level is under high school
* Calculate the percent of population that the education level is between high school and bachelor
* Calculate the percent of population that the education level is at least bachelor
* Print who has higher votes in the state
* Create the pie chart to show the result!
   
   [image](https://github.com/lyuruiyue/DataAnalysisWithPython/raw/master/Final/Analysis2/Education_Level_State.PNG)

## JobOccupation
### Users could use this analysis to get the job occupations in two states. One state is Trump has the highest vote rate, the other state is Hillary has the highest vote rate.
* Get all the unique state codes from the dataframe
* Calculate the total votes that Trump got from each state!

   [image](https://github.com/lyuruiyue/DataAnalysisWithPython/raw/master/Final/Analysis3/total_votes.PNG)
* Sort the result then get the highest one and the lowest one
* Calculate the percent of 6 types of jobs in each county of that state
* Create one bar chart display the job occupations in the county that Trump has the highest votes
![image](https://github.com/lyuruiyue/DataAnalysisWithPython/raw/master/Final/Analysis3/Work_Occupation_in_WY.PNG)
* Create the other bar chart display the job occupations in the county that Hillary has the highest votes
![image](https://github.com/lyuruiyue/DataAnalysisWithPython/raw/master/Final/Analysis3/Work_Occupation_in_DC.PNG)

## RepublicansVsDemocrats
### Users could use this analysis to see the trend of how republicans and democrats rate changes from 2008 to 2016
* Get random 10 unrepeated state codes from the dataframe
* Create dataframe to store the result of party names, state code, year and mean value
![image](https://github.com/lyuruiyue/DataAnalysisWithPython/raw/master/Final/Analysis4/party_rate.PNG)
* Create graph to display the trend of how percents of __Republicans__ and __Democrats__ changes from 2008 to 2016
![image](https://github.com/lyuruiyue/DataAnalysisWithPython/raw/master/Final/Analysis4/Republicans_and_Democrats_2008_2012_2016.png)

## RaceByState
### Users could use this analysis to see the races rate in specific 10 states
* Get the top 5 states that Trump has higher votes and top 5 states Hillary has higher votes
* Create a dateframe to store the data of percent of each race

   ![image](https://github.com/lyuruiyue/DataAnalysisWithPython/raw/master/Final/Analysis5/state_percent.PNG)
* Calculate the total population of each race and then calculate the percentage
* Create bar chart to display the race percent in each state 
![image](https://github.com/lyuruiyue/DataAnalysisWithPython/raw/master/Final/Analysis5/Race_Presentage_in_States.png.PNG)

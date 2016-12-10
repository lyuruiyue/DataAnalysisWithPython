# Final

Dataset: usa-2016-presidential-election-by-county.csv
Downloaded from [OpenDataSoft](https://data.opendatasoft.com/explore/dataset/usa-2016-presidential-election-by-county@public/)
The total size is 288MB, so I split the file into two smaller files. The first one named data01.csv and the other named data02.csv
## VoteByCounty
* Read the two csv files using pandas and then concatenate them into one dataframe.
* Let the user to input a state code(like MA, CA, TX...)
* Select "ST", "County", "Clinton H" and "Trump D" columns from the dataframe to form a new dataframe
* Calculate the total votes that Trump and Hillary got from each county, get the mean value
* Shows who has higher votes in the state
* Create the graph, x = county, y = total votes, and two lines show the mean value

## EducationLevel
* Let the user to input a state code(like MA, CA, TX...) 
* Calculate the percent of population that the education level is under high school
* Calculate the percent of population that the education level is between high school and bachelor
* Calculate the percent of population that the education level is at least bachelor
* Shows who has higher votes in the state
* Create the pie chart to show the result

## WorkOccupation
* Get all the state code from the dataframe
* Calculate the total votes that Trump got of each state
* Sort the result then get the highest one and the lowest one
* Calculate the percent of 6 types of jobs
* Create one bar chart display the job occupations in the county that Trump has the highest votes 
* Create the other bar chart display the job occupations in the county that Hillary has the highest votes 

## RepublicansVsDemocrats
* Get random 10 unrepeated state code from the dataframe
* Create dataframe to store the result of party names, state code, year and mean value
* Create graph to display the trend of how percents of __Republicans__ and __Democrats__ changes from 2008 to 2016

## RaceByState
* Get the top 5 states that votes Trump and top 5 states votes Hillary
* Create a dateframe to store the data of percent of each race
* Calculate the total population of each race and then calculate the percentage
* Create bar chart to display the race percent in each state 
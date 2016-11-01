# Midterm

### Copy and paste the code into Jupyter Notebook and run

First of all, after you run the script, it would send 5 requests using "/questions/no-answers" api to get the questions which has no answers and tagged "python". Then stored the JSON format results into the folder named "stack_exchange_result"

Secondly, create a dictionary and the key is question title and the value is view count. After all the data were writen into the dictionary, sort it by the view count. Print the top 10 results that the question has the highest view count with no answer. The output is like ('question title', view count)

Thirdly, get all the question ids from the saved JSON results and send requests using "/questions/{ids}" api to get the bounty amount. Create a dictionary and the key is question title and the value is bounty amount. This would give the result that all the unanswered question with bounty amount sorted by bounty amount. The output format is like('question title', bounty amount)

Fourthly, send 5 requests using "/answers" api, and save the JSON format results into "stack_exchange_answer_result" folder. Get all the user ids from the result and send the requests using "/users/{ids}" api. Then calculate the weightage of each user and print the results sorted by the weightage. The output is like('user name', weightage) (weightage = bronze count + silver count * 2 + gold count * 3)

Fifthly, send request using "/users/{ids}/badges" api to get all the badges the user earned. And print the user names who earned the badge named "Teacher".

Lastly, send the requests using "/users/{ids}/favorites" api to get the items that each user had favorited. And then from the results print random 5 questions. 

# Used apis

## /questions/no-answers
## /questions/{ids}
## /answers
## /users/{ids}
## /users/{ids}/badges
## /users/{ids}/favorites
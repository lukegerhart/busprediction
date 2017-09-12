# Repository: 2017-09.project-1.template
# Assignment #1: Python 

> Course: **[CS 1656 - Introduction to Data Science](http://cs1656.org)** (CS 2056) -- Fall 2017    
> Instructor: [Alexandros Labrinidis](http://labrinidis.cs.pitt.edu)  
> 
> Assignment: #1.  
> Released: September 12, 2017  
> **Due:      September 25, 2017**

### Description
This is the **first assignment** for the CS 1656 -- Introduction to Data Science (CS 2056) class, for the Fall 2017 semester.

### Goal
The goal of this assignment is to familiarize you with the Python programming language and also to be exposed to real data and real APIs.

### What to do -- wheresmybus.py
You are asked to write a Python program, called `wheresmybus.py` that will act as an interface to the TrueTime API v3 of the [Port Authority of Allegheny County](http://www.portauthority.org/paac/) that provides real-time information on bus arrivals.

You can find more information about TrueTime at <http://www.portauthority.org/paac/CompanyInfoProjects/DeveloperResources.aspx>

You program should exhibit the following behavior:
`wheresmybus.py command optional_argument`

### command = getroutes
`wheresmybus.py getroutes` should connect to the TrueTime API and download all the available bus routes, using the `getroutes` call. Your program should do two things:
* print the rt/rtnm fields separated by a comma, one route per line, e.g.,:
```
61D, MURRAY
65, SQUIRREL HILL
'''
* save the data as a json object, in a file named (`allroutes.json`), as follows:
```
{{'rt':'61D', 'rtnm':'MURRAY'},
 {'rt':'65',  'rtnm':'SQUIRREL HILL'}}
'''

### command = getdirections
`wheresmybus.py getdirections` should connect to the TrueTime API and download the available directions for all routes from `allroutes.json` **that start from a `6`** (to keep things manageable). You should keep in mind the rate limitations for the TrueTime API (10,000 requests per day), so you should implement a delay timer. As before, your program should do two things:
* print the available rt/rtnm/direction combination for each route separated by a comma, one combination per line, e.g.,:
```
61D, MURRAY, INBOUND
61D, MURRAY, OUTBOUND
65, SQUIRREL HILL, INBOUND
65, SQUIRREL HILL, OUTBOUND
'''
* save the data as a json object, in a file named (`6routes.json`), as follows:
```
{{'rt':'61D', 'rtnm':'MURRAY', 'dir':'INBOUND'},
 {'rt':'61D', 'rtnm':'MURRAY', 'dir':'OUTBOUND'},
 {'rt':'65', 'rtnm':'SQUIRREL HILL', 'dir':'INBOUND'},
 {'rt':'65', 'rtnm':'SQUIRREL HILL', 'dir':'OUTBOUND'}}
'''







``` 
 
### Important notes about grading
It is absolutely imperative that your python program:  
* runs without any syntax or other errors (using Python 3) -- we will run it using the following command:  
`python3 team1 team2 year rain` OR `python3 team1 team2 year snow`  
* strictly adheres to the format specifications for input and output, as explained above.     

Failure in any of the above will result in **severe** point loss. 


### Allowed Python Libraries
You are allowed to use the following Python libraries (although a fraction of these will actually be needed):
```
argparse
collections
csv
glob
math 
os
pandas
re
requests
string
sys
```
If you would like to use any other libraries, you must ask permission by Wednesday, January 25, 2017, using [piazza](http://piazza.cs1656.org).


### About your github account
It is very important that:  
* Your github account can do **private** repositories. If this is not already enabled, you can do it by visiting <https://education.github.com/>  
* You use the same github account for the duration of the course  
* You use the github account that you specified during the test assignment (i.e., this one)  

### How to submit your assignment
For this assignment, you must use the repository that was created for you after visiting the classroom link. You need to update the repository to include file `weatherbowl.py` as described above, and other files that are needed for running your program. You need to make sure to commit your code to the repository provided. We will clone all repositories shortly after midnight:  
* the day of the deadline **Sunday, January 29th, 2017 (i.e., at 12:15am, Monday, January 30, 2017)**  
* 24 hours later (for submissions that are one day late / -5 points), and  
* 48 hours after the first deadline (for submissions that are two days late / -15 points). 

Our assumption is that everybody will submit on the first deadline. If you want us to consider a late submission, you need to email us at `cs1656-staff@cs.pitt.edu`

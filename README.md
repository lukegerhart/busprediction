# Repository: 2017-01.project-1.template
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
You are asked to write a Python program, called `wheresmybus.py` that will act as an interface to the TrueTime API of the [Port Authority of Allegheny County](http://www.portauthority.org/paac/) that provides real-time information on bus arrivals.

You can find more information about TrueTime at <http://www.portauthority.org/paac/CompanyInfoProjects/DeveloperResources.aspx>

You program should exhibit the following behavior:
`wheresmybus.py command optional_argument`

### command = getroutes
`wheresmybus.py getroutes`







that will take as input the names of two NFL teams (e.g., `Steelers` and `Patriots`), a year (e.g., `1995`), and the word `rain` (or the word `snow`), in order to determine which team "won" in terms of **total** precipitation for rain (or for snow) for the specified year (i.e., all 12 months), using weather data from `WeatherUnderground.com` for the  cities of the two teams. Winning means highest precipitation.  

Your program should be called as follows:  
`python3 team1 team2 year rain` OR `python3 team1 team2 year snow`   
For example: `python3 weatherbowl.py steelers patriots 1998 snow`

The information about the NFL team names and the corresponding cities is provided as a CSV file, named `NFL_data.csv`, which is included in this repository. Note that you should be matching even part of the team name, provided there is a single match, otherwise it would return an error message. For example, `Pit` or `pitt` or `Pittsburgh` or `Steelers` should all match `Pittburgh Steelers` and lead to using KPIT for the weather data. You should also ignore case.

You should get the WeatherUnderground weather data using their historical data interface, e.g., 
`https://www.wunderground.com/history/airport/KPIT/2016/1/1/MonthlyHistory.html?format=1`
to get a CSV with the readings for all days in January 2016 from Pittsburgh's airport.

Please note that the type of precipitation should match even if it is part of the event as well, so `snow` should also match cases of `snow-rain`, `rain-snow`, `fog-rain-snow`, etc

### Output format
Your program should report:  
* the year 
* the total precipitation for each team/city,  
* the winning team, and  
* the percent of win (i.e., if W is the total precipitation of the winning team, L is the total precipitation of the losing team, you need to report 100 * (W / L - 1)     
 
Here is an example of the proper output format (only used to indicate the format, the precipitation amounts are fictitious):
```
YEAR: 1850
TYPE: snow 
TEAM-1: Pittsburgh Steelers 
CITY-1: KPIT 
PRECIP-1: 26.5
TEAM-2: New England Patriots 
CITY-2: KOWD
PRECIP-2: 25.0
WINNER: Pittsburgh Steelers 
PERCENT: 6.00%
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

# 99Acres Scrapper
A small Selenium-BS4 program to scrap 99Acres data of a city to CSV

## Prerequisites

- Python 3
- Selenium
- Beautiful Soup 4
- Pandas
## What should I know before running this code?
Not much. Just a couple of points:
- The local path for output CSV is hard-coded in the code. Please make sure to edit it out.
- I have coded the base loop to run 25 times. While this should cover data for most tier-2 Indian cities (like Indore in the program), certain cities will have fewer or more pages. In that case, please edit the loop limit or out-of-range exception will be raised.

As always, please open up issue or comment for assistance. 

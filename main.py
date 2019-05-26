from file_functions import open_html, save_csv
from parser import parser


#create an input date and set up a way to move through dates up to today
#create a check for duplicate data
#create a way to uploda new data? using time maybe

date = '2019-05-24'
location = 'atlanta'
####
#Date works as 2019-5-24 OR 2019-05-24
####
url = 'https://www.wunderground.com/history/daily/us/ga/atlanta/KATL/date/2019-05-24' #url for ATL 5/24/19 weather

parser(url, date, location)

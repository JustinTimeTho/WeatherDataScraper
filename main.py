from file_functions import open_html, save_csv
from parser import parser
from datetime import datetime, timedelta
from time import sleep


#create an input date and set up a way to move through dates up to today
#Include current year??
#create a check for duplicate data
#create a way to uploda new data? using time maybe

#Flesh out initial questions more, ensure that only good numbers used
##could do this using regexs, strings, whatever method
#Make sure date isn't in the future?

#Get location
while True:
    location = input('What city would you like to collect weather data from?\n(Options are atlanta or detroit)\n')
    if location != ('atlanta' or 'detroit'):
        continue
    else:
        break
#Get dates
#Start Date
while True:
    try:
        InputDate = input('Enter the start date for collection (YYYY-MM-DD)')
        StartDate = datetime.strptime(InputDate, '%Y-%m-%d')
        StartDateStr = StartDate.strftime('%Y-%m-%d')
    except:
        print('Invalid date')
        continue
    if StartDateStr > datetime.today().strftime('%Y-%m-%d') or StartDateStr < '1999-12-31':
        print('Date is not between 1999 and the present')
        continue
    else:
        break
#End Date
while True:
    try:
        InputDate = input('Enter the end date for collection (YYYY-MM-DD)')
        EndDate = datetime.strptime(InputDate, '%Y-%m-%d')
        EndDateStr = EndDate.strftime('%Y-%m-%d')
    except:
        print('Invalid date')
        continue
    if EndDateStr > datetime.today().strftime('%Y-%m-%d') or EndDateStr < '1999-12-31' or EndDateStr < StartDateStr:
        print('Date is not between 1999 and the present or before the start date')
        continue
    else:
        break

####
#Date works as 2019-5-24 OR 2019-05-24
#want to avoid 05 because that means octal to python
####
if location == 'atlanta':
    url = 'https://www.wunderground.com/history/daily/us/ga/atlanta/KATL/date/'
elif location == 'detroit':
    url = 'https://www.wunderground.com/history/daily/us/mi/detroit/KDET/date/'

while StartDate <= EndDate:
    IterateDate = StartDate.strftime('%Y-%m-%d')
    print(IterateDate)
    url += IterateDate
    #parser(url, date, location)
    parser(url, IterateDate, location)
    StartDate = StartDate + timedelta(days=1)
    sleep(15)

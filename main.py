from file_functions import open_html, save_csv
from parser import parser


#create an input date and set up a way to move through dates up to today
#Include current year??
#create a check for duplicate data
#create a way to uploda new data? using time maybe

#Flesh out initial questions more, ensure that only good numbers used
##could do this using regexs, strings, whatever method
#Make sure date isn't in the future?
CurrentYear = 2019
CurrentMonth = 5

# while location != ('atlanta' or 'detroit'):
#     location = input('please type atlanta or detroit')
while True:
    location = input('What city would you like to collect weather data from?\n(Options are atlanta or detroit)\n')
    if location != ('atlanta' or 'detroit'):
        continue
    else:
        break


while True:
    try:
        StartYear = int(input('What year would you like to start collection on?\n(Year must be between 2000 and 2019)\n'))
    except ValueError:
        continue
    if 2000 < StartYear < CurrentYear:
        break
    else:
        continue

while True:
    try:
        StartMonth = int(input('What month would you like to start collection on?\n(Month must be 1 to 12)\n'))
    except ValueError:
        continue
    if CurrentYear == StartYear:
        if StartMonth > CurrentMonth:
            continue
    if 0 < StartMonth < 13:
        break
    else:
        continue

Date = str(StartYear) + '-' + str(StartMonth) + '-1'
print(Date)

####
#Date works as 2019-5-24 OR 2019-05-24
####
if location == 'atlanta':
    url = 'https://www.wunderground.com/history/daily/us/ga/atlanta/KATL/date/'
elif location == 'detroit':
    url = 'https://www.wunderground.com/history/daily/us/mi/detroit/KDET/date/'
url += Date
#parser(url, date, location)

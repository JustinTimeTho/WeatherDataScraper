#DO NOT RUN

###Code to create a new file with the categories
#Still usable and needed
from file_functions import new_file

location = 'atlanta'
filename = 'database/' + location + '.csv'
Categories = ['Time','Temperature','Dew Point','Humidity','Wind','Wind Speed','Wind Gust','Pressure','Precip.','Precip Accum','Condition','Date']

new_file(filename, Categories)

from datetime import datetime, timedelta



###Practice with time Iterating
Today = datetime.today()
print(Today.strftime('%Y-%m-%d'))

start_date = '2018-12-25'
stop_date = '2019-01-3'
#strptime converts strings to datetime objects
start = datetime.strptime(start_date, '%Y-%m-%d')
stop = datetime.strptime(stop_date, '%Y-%m-%d')

while start < stop:
    #strftime converts datetime objects to strings?
    print(start.strftime('%Y-%m-%d'))
    start = start + timedelta(days=1)



###Old Code for collecting data information
#Usable but not ideal
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
    if 1999 < StartYear < CurrentYear:
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
    elif 0 < StartMonth < 13:
        break
    else:
        continue

while True:
    try:
        StopYear = int(input('What year would you like to end collection on?\n(Year must be between 2000 and 2019)\n'))
    except ValueError:
        continue
    if StopYear < StartYear:
        print('End year must be after start year')
        continue
    elif 2000 < StopYear < CurrentYear:
        break
    else:
        continue

while True:
    try:
        StopMonth = int(input('What month would you like to stop collection on?\n(Month must be 1 to 12)\n'))
    except ValueError:
        continue
    if StopYear == StartYear and StopMonth < StartMonth:
        print('Pick a month after your start month')
    elif CurrentYear == StartYear:
        if StopMonth > CurrentMonth:
            continue
    elif 0 < StartMonth < 13:
        break
    else:
        continue

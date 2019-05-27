from file_functions import new_file

location = 'atlanta'
filename = 'database/' + location + '.csv'
Categories = ['Time','Temperature','Dew Point','Humidity','Wind','Wind Speed','Wind Gust','Pressure','Precip.','Precip Accum','Condition','Date']

new_file(filename, Categories)

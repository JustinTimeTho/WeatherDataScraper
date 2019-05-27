import csv

def open_html(path):
    with open(path, 'rb') as f: #with closes file automatically
        return f.read()

def new_file(filename, categories):
    with open(filename, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(categories)
    return None

def save_csv(list, location, CategoriesList):
    #if file = empty, put categories as first line
    filename = 'database/' + location + '.csv'
    #If the categories don't match, the data wont either
    Categories = ['Time','Temperature','Dew Point','Humidity','Wind','Wind Speed','Wind Gust','Pressure','Precip.','Precip Accum','Condition','Date']
    if Categories != CategoriesList:
        print('Error: Categories do not match for {}'.format(list[0][-1]))
        return None
    try:
        TestFile = open(filename, 'r')
        TestFile.close()
    except FileNotFoundError:
        print('Creating new csv...')
        new_file(filename, Categories)
    #Writing data to a csv once we know it's good, unique data
    with open(filename, 'a') as f:
        writer = csv.writer(f)
        writer.writerows(list)
    return None

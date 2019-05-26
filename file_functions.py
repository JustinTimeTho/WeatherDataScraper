import csv

def open_html(path):
    with open(path, 'rb') as f: #with closes file automatically
        return f.read()

def save_csv(list, location):
    #if file = empty, put categories as first line
    #check file and see if categories match?
    with open('database/' + location + '.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerows(list)
    return None

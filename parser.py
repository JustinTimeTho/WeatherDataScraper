from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from file_functions import save_csv

def parser(url, date, location):
    #### I didn't come up with this section, this is from python-forum.io/Thread-Web-Scraping-part-2
    #Basically, it uses a firefox broswer to fully load any javascript portions of the site
    options = Options()
    options.set_headless(headless=True)
    caps = webdriver.DesiredCapabilities().FIREFOX
    caps["marionette"] = True
    browser = webdriver.Firefox(firefox_options = options, capabilities=caps, executable_path=r"/usr/bin/geckodriver")
    browser.get(url)
    html = browser.execute_script('return document.documentElement.innerHTML;')
    #html = (browser.page_source).encode('utf-8')
    browser.quit()
    soup = BeautifulSoup(html, 'html.parser') #create soup object to use beautifulsoup4 parsing

    RawCategories = soup.select('.tablesaw-sortable-btn')#selects the first row of the Daily Observations table only
    CategoriesList = []
    for str in RawCategories:
        CategoriesList.append(str.text.strip())
    CategoriesList.append('Date')

    RawWeatherData = soup.select('#history-observation-table tbody tr td')#gets all values within the Daily Observations Table
    WeatherDataTable = []
    TempList = [] #used for appending values to WeatherDataTable by copying them
    for i in range(0,len(RawWeatherData)): #create a list of lists where every list is a row of a table
        if i%(len(CategoriesList)-1) == 0 and i is not 0: #ignoring i=0 because nothing is added to the list yet
            TempList.append(date)
            WeatherDataTable.append(TempList.copy())
            TempList.clear()
        TempList.append(RawWeatherData[i].text.strip().replace('\n',''))
    TempList.append(date)
    WeatherDataTable.append(TempList.copy()) #was missing the last data point
    save_csv(WeatherDataTable, location, CategoriesList)
    return None

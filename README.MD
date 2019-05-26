Project Goals


Detroit Weather Data: https://www.wunderground.com/history/daily/us/mi/detroit/KDET/date/2019-5-25

Atlanta Weather Data: https://www.wunderground.com/history/daily/us/ga/atlanta/KATL/date/2000-5-25

Notes:

Wundergronud has an offset of 8 hrs ahead or 4 hrs behind for ATL and DET

Date works as 2019-5-24 OR 2019-05-24


Naming conventions:

  Variables are camel case, starting with the first letter being capital
  
  Files and functions are underscore_separated


1. Webscrape a single page () with BeautifulSoup to extract and save data from a single day to a CSV file
2. Use strings to dynamically get data from Detroit or Atlanta (links above)
3. Learn use of datetime(https://docs.python.org/2/library/datetime.html) module to get data from all of 2019 (and also include a 10 second delay between requests)
4. Create a python GUI using tkinter to get data for specific days/to display dashboard data
5. Collect data hourly automatically
6. Put data into PowerBI and create dashboards
7. Put data into an SQL server

Requirements:
  BeautifulSoup4
  Pip3
  selenium
  This code to add gecko to path:
            ## Geckodriver
          wget https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-linux64.tar.gz
          sudo sh -c 'tar -x geckodriver -zf geckodriver-v0.23.0-linux64.tar.gz -O > /usr/bin/geckodriver'
          sudo chmod +x /usr/bin/geckodriver
          rm geckodriver-v0.23.0-linux64.tar.gz

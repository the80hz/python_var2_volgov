from datetime import datetime
from bs4 import BeautifulSoup
import csv
import requests

URL = 'https://www.gismeteo.ru/diary/4618'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}

TODAY_YEAR = datetime.now().timetuple().tm_year
TODAY_MONTH = datetime.now().timetuple().tm_mon

start = datetime.now().timestamp()
year = 2008
month = 1

database = open('dataset.csv', 'w+')
database.write('File generated: ' + str(datetime.today()) + '\n')
database.write('data,temperature,pressure,wind \n')

while year <= TODAY_YEAR:
    while month <= 12:
        if year == TODAY_YEAR and month == TODAY_MONTH:
            print('Reached the current date')
            break

        url = URL + str(year) + '/' + str(month) + '/'
        print(url)
        page = requests.get(url, headers=HEADERS)

        writer = csv.writer(database)

        soup = BeautifulSoup(page.text, "html")

        data = list()

        for row in soup:
            data.append()
            

            writer.writerow(data)

        month += 1
    year += 1
    month = 1

end = datetime.now().timestamp()
print(f'Scraping task finished in {round(end - start, 2)} sec')

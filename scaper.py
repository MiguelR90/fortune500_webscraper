import urllib2
import pandas as pd
from bs4 import BeautifulSoup

data = []
for year in range(1955, 2006):
    for batch in range(1, 500, 100):
        print 'Scraping data for == year : {0}, ranks : {1} - {2}'.format(year, batch, batch + 100)
        # print 'http://archive.fortune.com/magazines/fortune/fortune500_archive/full/{0}/{1}.html'.format(year,batch)
        soup = BeautifulSoup(urllib2.urlopen('http://archive.fortune.com/magazines/fortune/fortune500_archive/full/{0}/{1}.html'.format(year, batch)).read())

        table = soup.find_all('table', class_='maglisttable')[0]

        for row in table.find_all('tr', id='tablerow'):
            rank = row.find_all('td', class_='rank')[0].string
            company = row.find_all('td', class_='company')[0].a.string
            dcell = row.find_all('td', class_='datacell')
            data.append((year, rank.strip(), company.strip(), dcell[0].string.strip(), dcell[1].string.strip()))

df = pd.DataFrame(data, columns=['Year', 'Rank', 'Company', 'Revenues ($ millions)', 'Profit ($ millions)'])

df.to_csv('fortune500_data.csv', index=False)
df.to_json('fortune500_data.csv', orient='records')

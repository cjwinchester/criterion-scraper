import csv

import requests
import bs4


r = requests.get('https://www.criterion.com/shop/browse/list')
soup = bs4.BeautifulSoup(r.text, 'html5lib')
rows = soup.find_all('tr', {'class': 'gridFilm'})

with open('criterion.csv', 'w') as outfile:
    headers = ['spine_no', 'cover_img', 'title', 'url',
               'director', 'country', 'year']

    writer = csv.DictWriter(outfile, fieldnames=headers)
    writer.writeheader()

    for row in rows:
        cells = row.find_all('td')
        spine_no, img, title, director, country, year = cells
        data = [spine_no.text.strip(), img.img['src'],
                title.text.strip(), title.a['href'],
                director.text.strip(), country.text.strip().rstrip(','),
                year.text.strip()]
        writer.writerow(dict(zip(headers, data)))

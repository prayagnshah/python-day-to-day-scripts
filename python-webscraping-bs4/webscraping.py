import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.rottentomatoes.com/browse/movies_at_home/sort:popular"

r = requests.get(URL)

## Getting the raw content data from the URL
# print(r.content)
soup = BeautifulSoup(r.content, 'html5lib')

movies = []  ## Adding movies into the empty list 

table = soup.find('div', attrs = {'data-id':'movies_at_home_sort:popular'})

for row in table:
    movie = {}
    
    movie['img'] = row.img['src']
    movies.append(movie)
    
print(movies)
    

# print(soup.prettify())

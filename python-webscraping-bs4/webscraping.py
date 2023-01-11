import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.rottentomatoes.com/browse/movies_at_home/sort:popular"

r = requests.get(URL)

## Getting the raw content data from the URL
# print(r.content)
soup = BeautifulSoup(r.content, 'html5lib')

movies = []  ## Adding movies into the empty list 

## Finding the attribute of the movies where they are stored 
table = soup.find('div', attrs = {'data-id':'movies_at_home_sort:popular'})


# Running the loop of the movies to get its name and link
for movie_row in table.findAll('a'):
    movie = {}
    movie['movie-name'] = movie_row.img['alt']
    movie['movie-link'] = movie_row.img['src']
    movies.append(movie)
    
# print(movies)

# new filename to store the movies name and link    
filename = 'new-movies.csv'

## Storing the data into the file
with open(filename, 'w', newline='') as f: 
    w = csv.DictWriter(f,['movie-name', 'movie-link'])
    w.writeheader()

    for movie in movies:
        w.writerow(movie)

# print(soup.prettify())

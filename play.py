import requests
import collections

MovieResult = collections.namedtuple(
    'MovieResult',
    "imdb_code,title,duration,director,year,rating,imdb_score,keywords,genres"
)

search = 'capital'
url = 'http://movie_service.talkpython.fm/api/search/{}'.format(search)

resp = requests.get(url)
resp.raise_for_status()

movie_data = resp.json()
movies = movie_data.get('hits')

print(type(movie_data), movies)

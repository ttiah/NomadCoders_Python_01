import requests


movie_ids = [
    238, 680, 550, 185, 641, 515042, 152532, 120467, 872585, 906126, 840430
]

API_URL = 'https://nomad-movies.nomadcoders.workers.dev/movies/'

movie_info = []

for id in movie_ids:
    response = requests.get(f'{API_URL}{id}')
    data = response.json()
    movie = {
        'title': data['title'],
        'overview': data['overview'],
        'vote_average': data['vote_average'],
    }
    movie_info.append(movie)

for movie in movie_info:
    for k in movie.keys():
        print(f'{k}: {movie[k]}')
    print('*****'*10)

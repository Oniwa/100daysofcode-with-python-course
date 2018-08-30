import uplink

import requests


@uplink.response_handler
def raise_for_status(response):
    response.raise_for_status()
    return response


@uplink.json
@raise_for_status
class MovieSearchClient(uplink.Consumer):

    def __init__(self):
        super().__init__(base_url='http://movie_service.talkpython.fm')

    @uplink.get('/api/search/{keyword}')
    def search_keyword(self, keyword) -> requests.models.Response:
        """ Get's all movies that have the keyword in the title"""

    @uplink.get('/api/director/{director_name}')
    def search_director(self, director_name) -> requests.models.Response:
        """ Get's all movies directed by the director"""

    @uplink.get('/api/movie/{imdb_number}')
    def search_imdb_code(self, imdb_number) -> requests.models.Response:
        """ Get's the movie that matches the IMDB code"""


if __name__ == "__main__":
    movie = MovieSearchClient()
    response = movie.search_keyword('Scott')

    results = response.json()

    for idx, item in enumerate(results['hits'], 1):
        print(f'{idx}. {item.get("title")}')

    response = movie.search_director('Wright')

    results = response.json()

    for idx, item in enumerate(results['hits'], 1):
        print(f'{idx}. {item.get("title")}')

    response = movie.search_imdb_code('tt0446029')

    results = response.json()

    print(results.get('title'))
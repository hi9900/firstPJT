import requests
from pprint import pprint


def vote_average_movies():
    url = f"https://api.themoviedb.org/3/movie/popular"
    params = {
    'api_key': '3a4accd7ba8d3add19c510122c8c1b72',
    'language': 'ko-KR',
    
}
    response = requests.get(url, params=params).json()
    result = []
    # 평점(vote_average) >= 8
    for movie in response['results']:
        vote = movie['vote_average']
        if vote >= 8:
          result.append(movie)
    # 5개만
    return result

if __name__ == '__main__':
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 반환
    """
    pprint(vote_average_movies())


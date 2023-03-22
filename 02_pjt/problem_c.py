import requests
from pprint import pprint


def ranking():
    pass 
    url = f"https://api.themoviedb.org/3/movie/popular"
    params = {
    'api_key': '3a4accd7ba8d3add19c510122c8c1b72',
    'language': 'ko-KR',
    
}
    response = requests.get(url, params=params).json()
    response = response['results']

    # 평점(vote_average)을 기준으로 정렬
    result = sorted(response, key=lambda x: x['vote_average'], reverse=True)
    return result[:5]


if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화 반환
    """
    pprint(ranking())
    
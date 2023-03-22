import requests


def popular_count():
    url = f"https://api.themoviedb.org/3/movie/popular"

    params = {
    'api_key': '3a4accd7ba8d3add19c510122c8c1b72',
    'language': 'ko-KR',
}
    response = requests.get(url, params=params).json()
    results = len(response['results'])
    return results

if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20

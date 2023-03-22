import requests
from pprint import pprint


def credits(title):
    # 영화 검색
    url = f"https://api.themoviedb.org/3/search/movie"
    params = {
    'api_key': '3a4accd7ba8d3add19c510122c8c1b72',
    'language': 'ko-KR',
    'query' : title
}
    response = requests.get(url, params=params).json()
    response = response['results']

    # 검색된 영화가 없다면 None
    if response == []:
        return None

    # 응답 첫번째 영화의 id값 
    movie_id = response[0]['id']

    # 출연진과 스태프목록
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?"
    recommend = requests.get(url, params=params).json()

    result = {}
    # 출연진
    casts = recommend['cast']        
    # 출연진(cast) cast_id < 10 이면 name 출력
    for cast in casts:
        if cast['cast_id'] < 10:
            result['cast'] = result.get('cast', []) + [cast['name']]
    # 스태프
    crews = recommend['crew']        
    # 스태프(crew) department == Directing 이면 name 출력
    for crew in crews:
        if crew['department'] == 'Directing':
            result['crew'] = result.get('crew', []) + [crew['name']]

    return result

if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 
    주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None

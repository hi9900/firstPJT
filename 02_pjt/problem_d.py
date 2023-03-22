import requests
from pprint import pprint


def recommendation(title):
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

    # 추천영화목록 가져오기
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations?"
    # 결과에 차이는 없는데 사용안해서 뺌
    del(params['query'])
    recommend = requests.get(url, params=params).json()
    recommend = recommend['results']
    
    # 추천영화는 모든 영화 제목 출력
    result = []
    for movie in recommend:
        result.append(movie['title'])

    return result

if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None

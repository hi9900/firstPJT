import json


def max_revenue(movies):
    # movies폴더 파일 하나하나에 접근
    # 파일 하나-> revenue의 value값이 가장 큰 
    # 그 파일의 title의 value 반환
    max_re = 0
    max_id = 0
    for i in range(len(movies)):
        id = movies[i]['id']

        # 파일 명이 id
        movie = open(f'data/movies/{id}.json', encoding='utf-8')
        movie_detail = json.load(movie)

        # 수익0 vs 처음 영화 수익
        # 큰 수익 -> max
        if movie_detail['revenue'] > max_re:
            max_re = movie_detail['revenue']
            # 최대 수익의 idx
            max_id = i

    return movies[max_id]['title']
        
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))

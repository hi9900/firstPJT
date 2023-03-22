import json


def dec_movies(movies):
    movies_list = []
    for i in range(len(movies)):
        id = movies[i]['id']

        # 파일 명이 id
        movie = open(f'data/movies/{id}.json', encoding='utf-8')
        movie_detail = json.load(movie)

        # 개봉일 release_date"1940-10-23" == 12월 
        if movie_detail['release_date'][5:7] == '12':
            movies_list.append(movie_detail['title'])
            
    return movies_list

if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))

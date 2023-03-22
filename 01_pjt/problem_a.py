import json
from pprint import pprint


def movie_info(movie):
    # 필요한 정보: id,1title,1poster_path,1vote_average,1overview,1genre_ids
    # movie[]: movie.json에서 정보 추출
    
    new_dict = {
        'id' : movie['id'],
        'title': movie['title'],
        'poster_path': movie['poster_path'],
        'vote_average': movie['vote_average'],
        'overview': movie['overview'],
        'genre_ids': movie['genre_ids'],
    }
    return new_dict

if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))
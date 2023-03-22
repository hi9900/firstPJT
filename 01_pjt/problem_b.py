import json
from pprint import pprint


def movie_info(movie, genres):
    genres_id = movie['genre_ids']
    genres_name = []
    
    # movie의 ids를 하나씩 genres의 id값에 대입
    for genre in genres:    # genre = genres의 index 단위로 한 딕셔너리
        # id값 같은게 있다면 name값 저장
        if genre['id'] in genres_id:
            genres_name.append(genre['name'])

    new_dict = {
        'id': movie['id'],
        'title': movie['title'],
        'poster_path': movie['poster_path'],
        'vote_average': movie['vote_average'],
        'overview': movie['overview'],
        'genre_names': genres_name 
    }
    return new_dict


if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))

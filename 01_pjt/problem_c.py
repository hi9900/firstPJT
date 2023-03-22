import json
from pprint import pprint


def movie_info(movies, genres):
    movies_list = []
    for i in range(len(movies)):
        new_dict = {}
        movie = movies[i]
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
        movies_list.append(new_dict)
    return movies_list
        
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))

'''
movies의 길이 만큼 반복문을 돌렸으나, 다른 방법이 있을까
'''
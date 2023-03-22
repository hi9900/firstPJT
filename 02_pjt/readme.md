## A. 인기 영화 조회

api_key가 길어서 url에 넣으면 화면 밖으로 잘려서 params을 따로 지정해서 사용
dict.get(url, params=params): `params=` 추가적으로 봐야함
영화 목록 개수는 results 리스트 안의 요소(영화) 개수이므로 results 리스트의 길이 출력

## B. 특정 조건에 맞는 인기 영화 조회 1

movies의 데이터는 'results'에 영화 하나 당 딕셔너리 하나로 저장되어 있음.
영화 정보 중 평점 (vote_average) 키값에 해당하는 점수가 8 이상일 경우 
result 리스트에 영화정보를 추가해서 출력

+page 값이 defalt 1이라 영화정보가 20개까지 보이고 그 안의 8점 이상 값이 출력됨
다음 page도 볼 수 있는 방법?

## C. 특정 조건에 맞는 인기 영화 조회 2

`response['results']`만 사용하기에 response에 할당
특정 key값을 기준으로 정렬하기 위해 `key=lambda x: x['vote_average']`
처음 key값에 `'vote_average'`를 넣었으나, key값에는 하나의 인자를 받는 함수를 지정해야 함. lambda로 함수를 만들어서 넣음
lambda는 아직 편리하게 사용 못하겠음. 구글링을 통해 예시를 보고 넣어봄. 연습이 더 필요하다
sorted 함수는 기본적으로 오름차순 정렬이므로 큰 값부터 정렬하기 위해 `reverse=True`
상위 5개의 값을 반환해야 하므로 처음값부터 인덱스4까지 슬라이싱 후 반환

## D. 특정 추천 영화 조회

`search/movie url`의 양식에 맞춰 query 추가: 검색 할 내용
검색 된 영화가 없다면 response는 빈 리스트, None값 반환
검색되었다면, 응답 첫번째 영화(index 0)의 'id'값을 movie_id에 저장 후
추천 영화목록에 재검색
parms에 query가 들어가 있는데 `movie/{movie_id}/recommendations?`에 필요한 인자로 query가 없어서 결과값에는 변함이 없지만
사용하지 않는 params가 들어와도 필요한 데이터만 사용해서 검색됨
+ 방법 사용하지 않 params를 빼거나, 검색 시 params를 새로 정의하거나, 그냥 다써도 됨
영화제목을 모을 result 리스트를 생성 후 모든 recommend에 나와있는 영화 제목만 저장 후 출력

## E. 출연진, 연출진 데이터 조회

D에서 출연진, 스태프를 검색하는 url만 변경,
출력 값이 dict형태로 result 생성
영화 검색에서는 'results'에 영화 정보가 모두 포함되었으나
출연진, 스태프에는 'cast'와 'crew' key값을 갖는 딕셔너리 형태가 나옴
dict.get을 사용해 키 값에 name 삽입 후 반환
+dict.setdefault() 사용법 익혀보기

---

## F. 선택과제
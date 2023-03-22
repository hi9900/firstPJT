# 반응형 웹 페이지 구현

## 1. nav_footer.html

### 1-1. Navigation Bar

- 부트스트랩에서 예제를 가지고 온 후 내부 글자만 수정했다.

- 부트스트랩 내에서도 반응형으로 작동해서, 원하는 샘플을 찾기 어려웠지만, 모든 항목을 줄여보고 키워보며 알맞은 것을 찾아낼 수 있었다.

- 로고 이미지는 보기에 적당한 120px로 고정

- 부트스트랩의 모달 예제는 버튼으로만 작동해서, 구글링해서 나온 예시를 보며 하이퍼링크로 작동하는 모달 방식을 찾아냈다.

- L34: `class = data-bs-toggle="modal" data-bs-target="#ModalLogin"`

  하이퍼링크에 모달 클래스를 추가하여 모달을 작동하도록 할 수 있다.

  `a` 태그의 하이퍼링크는 이동하지 않으니 #으로 설정

- 모달 div를 nav내에 넣어놓으니 로그인창을 눌러 모달 실행 시 회색 화면만 나타났다.

  모달이 nav안에서 켜져서, 백그라운드(회색)가 보인 것으로 추정

  nav 바깥에 모달div를 위치시켜 해결했다.

- 모달에 로그인 폼을 작성: 부트스트랩 + 이전의 과제 참고했다.

### 1-2. footer

- 글자가 담긴 div를 작성 후 아래에 고정했다.

- `d-flex justify-content-center` 로 수평 가운데 정렬, `align-middle`로 수직 가운데 정렬

## 2. home.html

### 2-1. Header

- nav를 `fixed-top`로 놓으니 본문이 가려져서 `sticky-top`으로 수정

  - bootstrap 페이지의 nav는 위에 고정되고 본문 띄워져있어서 관리자모드로 보니깐 얘네 페이지는 sticky를 쓰고있었음,,, 예제에는 왜 fixed?

- Bootstrap Carousel Component로 구성

- Carousel은 자동으로 넘어감, 임의의 시간을 주려면 따로 class에 추가하는 것

### 2-2. Section

- h1 태그 볼드체, 가운데 정렬

- Bootstrap Card Component로 구성

- 영화 하나 당 `article class="card"`로 설정

  img, title(h5), text(p)로 구성됨

- 카드 하나하나는 세로로 되어있어서 `class="col"`

- L111: article 전체를 감싸는 div class

  `row-cols-sm-3` 768px 이상이면 3개로 정렬

  `row-cols-1`: 그 이하는 1개로 정렬

  `g-4`: 자세히는 모르겠는데 이걸 하니깐 사이가 이쁘게 띄워짐

    거터라고함

- L107: `mb-5`

  맨 아래로 내렸을 때, footer에 겹치지 않게 margin bottom 줌

## 3. community.html

### 3-1. Aside: 게시판 목록

- 가로크기가 992px(lg) 미만일 때는 전체 너비이므로 L98:`class="row"`로 게시판 목록과 게시판을 감싸서 한 줄 씩 나타나게 해줌

- 가로크기가 992px(lg) 이상일 때 1/6이라서 전체 grid(12)의 1/6으로 설정: L98:`col-lg-2`

- List Group 활용, 스크롤스파이에만 있어서 필요한 코드만 가져다 씀

- 하이퍼링크라서 a 태그만 사용했는데, 검정색으로만 표현되어서 ul>li안에 넣으니 됨

  li안에 넣어서 되는 게 아니라, L101: `class="list-group-item list-group-item-action"`을 하면 하이퍼링크에만 나타나던 파란글씨가 사라지는 것 같음

### 3-2. Section: 게시판

- 마찬가지로 lg 미만일 때는 전체너비, 이상일 때는 L98:`col-lg-10`

- lg 미만일 때만 article이 나타날 수 있도록 L114: `class="d-lg-none mt-3"`

- article은 수평선, h3(제목), h5(내용), p(작성자), p(시간)

  p태그에 mb?? 가 있어서 추가로 한 줄 안띄움

- lg 이상일 때 table이 나타나도록 L139:`class="d-none d-lg-block"`

  공식문서에 `.d-none .d-lg-block .d-xl-none`라 적혀있어서 그대로 했는데 안됨

  `.d-xl-none` 빼니깐 됨,,

- 테이블 꾸미기: L141: `class="table table-striped table-hover`

  striped=줄무늬 hover=마우스올리면 회색 반응

- 제목행(thead) dark테마로 설정하고, 내용도 체움

### 3-3. pagiation

- 진짜 bootstrap에서 그대로 가져옴

## 끝

- CSS를 하나도 안쓰고 부트스트랩만 씀

  아마 id랑 class에 example이 들어가 있는데 몇개는 수정하고, 몇개는 놔둔것 같음

  어디까지 건들어도 되는 지를 몰라서 그대로 쓰는 중

  다음번엔 값 수정해보기
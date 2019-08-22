"""
*** 웹 사이트 만들 때 1번만 실행 ***
1. 파이참 프로젝트 만들기
(가상환경 실행)

2. 장고 설치
$ pip install django

3. 장고 프로젝트 만들기
$ django-admin startproject config .

4. DB 초기화
$ python manage.py migrate
(원래는 DB에 갱신할게 있으면 반영하라는 명령, 처음에 실행하면 필요 파일을 설정해주기 때문에 사용)

5. 관리자 계정 생성
$ python manage.py createsuperuser

*** 웹 사이트 기능을 만들 때 반복해서 실 ***
6. 앱 만들기
$ python manage.py startapp bookmark
(settings.py -> INSTALLED APPS에 앱을 추가)
(앱을 만들면 MTV 파일이 다 생성된다, 생성된 파일을 수정만 하면 됨, template 폴더, urls 폴더는 따로 만듦)

7. 모델 생성 : 이 앱에서 어떤 데이터를 다룰 것인지 정의
(어떤 데이터를 어떤 형식으로 어떤 제약조건을 가지고 DB에 저장할 것인가?(DB와 연관))
(+ 사용자에게 입력받을 때 어떤 형식으로 어떤 제약조건을 가지고 입력받을 것인가?(Front-end와 연관))
(1. ORM 기능을 사용하기 위해서 Model 클래스를 상속받는다)
(2. 원하는 데이터가 있다면 필드로 작성)

(모델 작성을 끝낸 후)
$ python manage.py makemigrations
(-> 모델을 돌면서 변경사항을 추적해서 migration할 것들을 리스트업 함 (git status와 비슷))
(-> migrations 디렉토리에 0001_initial.py가 생긴 것을 볼 수 있음, 여기에 어떤식으로 DB에 보낼 것인지 기본 틀을 만듦)
$ python manage.py sqlmigrate bookmark 0001
(-> 우리는 ORM을 쓰기 때문에 어떤 쿼리가 실행되는지 모르지만 이 명령어로 어떤 쿼리가 실행되는지를 먼저 볼 수 있음)
$ python manage.py migrate
(-> 이때 0001_initial.py 파일의 기본 틀을 참고하여 사용하는 DB를 확인하고 그에 맞는 쿼리문을 날린다)

(admin.py에 모델 추가)
(모델을 관리자 페이지에 등록해서 다루고 싶을 때)
(관리자 페이지의 화면을 커스터마이징하고 싶을 때)
(-> admin.site.register(모델 이름))

8. 뷰 생성 : DB와 Front-end 사이에서 데이터를 연결해주는 로직을 작성
(어떤 요청이 있는가? 어떤 데이터가 전달됐는가? 어떤 응답을 주어야 하는가?)
(urls.py을 앱 디렉토리에 만듦)
(config 디렉토리의 urls.py에 path('', include('bookmark.urls')), 추가)

(뷰를 생성한 후)
(urls.py에 뷰를 from .views import * 해주고)
(urlpatterns = [] 안에 path를 작성하여 url과 뷰를 연결)

9. 템플릿 생성
(앱 디렉토리 아래 templates 디렉토리 만들고, 그 안에 앱 이름과 동일한 디렉토리 하나 더 만들고 거기에 html 파일 생성)
(bootstrap으로 디자인)
(template의 분리와 확장(모듈화))
(글로벌 네비게이션 바와 같은 것들은 앱 밖으로 빼서 관리 -> settings.py의 TEMPLATES 부분에 경로 추가)
(-> APP_DIRS : templates 디렉토리들을 훑어서 확인할 것인가, True인 상태로 나두어야 함)
(-> DIRS : 여기에 경로 추가)

10. URL 연결

bookmark
1. Create : 사이트 이름, 주소
2. Read : 사이트 정보 보기(사이트로 넘겨주면 되는 것이기 때문에 실 효용은 X)
3. Update
4. Delete
5. List

애용하는 사이트를 복제해서 구현해보는 것도 좋다
"""
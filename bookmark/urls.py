from django.urls import path
# url - 주소(정규표현식으로 주소를 표현), 뷰
# path - 주소(기존 정규표현식을 간단히 표현할 수 있게 컨버터), 뷰
# re_path - 주소(정규표현식으로 주소를 표현), 뷰

# 뷰는 함수형, 클래스형 두 종류로 만들 수 있다
# 결국은 장고에서는 모든 뷰는 함수형으로 동작하게 되어 있다

from .views import *

# urlpatterns 변수명은 바꿀 수 없음
urlpatterns = [
    # 함수형 뷰 : 함수이름만 쓰면 됨
    # 클래스형 뷰 : 클래스이름.as_view() -> 함수형 뷰처럼 만들어 주는 것
    # naver.com/blog/update/?doc_id=1234
    # naver.com/blog/update/1234 -> 더 깔끔함, <int:pk>
    path("delete/<int:pk>/", BookmarkDelete.as_view(), name='bookmark_delete'),
    path('update/<int:pk>/', BookmarkUpdate.as_view(), name='bookmark_update'),
    path('write/', BookmarkCreate.as_view(), name='bookmark_create'),
    path("", BookmarkList.as_view(), name='bookmark_list'),
    # name은 html에서 써줄 이름
]
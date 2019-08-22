from django.shortcuts import render

# Create your views here.

# 뷰는 페이지를 '어떻게' 보여줄 것인가, 템플릿은 페이지를 '무엇을' 보여줄 것인가

# 1. View + Template
# 2. API View + React or V

# django에 CRUDL은 이미 만들어져 있음  -> 제네릭 뷰(미리 만들어져 있는 자주 사용하는 형태의 뷰)
# 포트폴리오 사이트 만드는데는 아래 5개면 다 됨
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from .models import Bookmark

# 함수형 뷰
# def bookmarkList(request):
#   object_list = Bookmark.objects.all()
#   return render(request, "bookmark/bookmark_list.html",{'object_list':object_list})

# 클래스형
class BookmarkList(ListView):
    # 제네릭 뷰를 사용한다
    # 1. 필요한 제네릭 뷰를 상속받는다
    # 2. 사용할 모델을 설정한다

    model = Bookmark
    # 기본 룰 ->
    # 앱/모델명_list.html을 렌더링 하겠다
    # create, update : 앱/모델명_form.html
    # 앱/모델명_detail.html
    # 앱/모델명_confirm_delete.html

    # 만약 뷰에서 출력해야할 모델 데이터가 있다면,
    # 단일 객체를 보여줘야 하는 경우 : object
    # 복수 객체를 보여줘야 하는 경우 : object_list

from django.urls import reverse_lazy
class BookmarkCreate(CreateView):
    model = Bookmark
    fields = ['site_name','url','description']
    # success_url = '/' -> 하드코딩은 좋지 않다, reverse_lazy를 쓴다
    success_url = reverse_lazy('bookmark_list')

class BookmarkUpdate(UpdateView):
    model = Bookmark
    fields = ['description']
    # site_name과 url은 변경 불가능하게 할거면 지워주면 된다
    success_url = reverse_lazy('bookmark_list')

class BookmarkDelete(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark_list')
    # pk_url_kwarg = 디폴트 값이 pk
    # template_name_suffix = "_delete"
    template_name = "bookmark/bookmark_delete.html"
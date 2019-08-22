from django.contrib import admin
from .models import Bookmark

# Register your models here.
# 모델을 관리자 페이지에 등록해서 다루고 싶을 때
# 관리자 페이지의 화면을 커스터마이징하고 싶을 때
# -> admin.site.register(모델 이름)

admin.site.register(Bookmark)

from django.db import models

# Create your models here.

# 모델은 어떤 데이터를 어떤 형식으로 어떤 제약조건을 가지고 DB에 저장할 것인가?(DB와 연관)
# + 사용자에게 입력받을 때 어떤 형식으로 어떤 제약조건을 가지고 입력받을 것인가?(Front-end와 연관)
# 1. ORM 기능을 사용하기 위해서 Model 클래스를 상속받는다
# 2. 원하는 데이터가 있다면 필드로 작성

class Bookmark(models.Model):
    site_name = models.CharField(max_length=30, verbose_name="사이트명")
    # CharField와 TextField의 차이점은 길이제한이 있는가 없는가의 차이
    # max_length는 필수값
    # 길이제한이 없는 TextField에는 DB에 더 많은 용량을 확보해놓아야 한다
    # 처음에는 관례적인대로 따른다(ex. id는 CharField, description은 TextField)
    url = models.URLField(verbose_name="주소")
    description = models.TextField(blank=True, verbose_name="설명")
    # 필수로 입력받을 값이 아니라면 blank=True

    def __str__(self):
        return self.site_name + " : " + self.url

    class Meta:
    # 모델(여기서는 Bookmark 클래스)에 대한 옵션을 작성
        ordering = ['site_name']
        # 여러가지 정렬기준을 줄 수 있음, 내림차순은 앞에 -를 붙임

    # 모델 작성을 끝낸 후
    # $ python manage.py makemigrations
    # -> 모델을 돌면서 변경사항을 추적해서 migration할 것들로 리스트업 함 (git status와 비슷)
    # -> migrations 디렉토리에 0001_initial.py가 생긴 것을 볼 수 있음, 여기에 어떤식으로 DB에 보낼 것인지 기본 틀을 만듦
    # $ python manage.py sqlmigrate bookmark 0001
    # -> 우리는 ORM을 쓰기 때문에 어떤 쿼리가 실행되는지 모르지만 이 명령어로 어떤 쿼리가 실행되는지를 먼저 볼 수 있음
    # $ python manage.py migrate
    # -> 이때 0001_initial.py 파일의 기본 틀을 참고하여 사용하는 DB를 확인하고 그에 맞는 쿼리문을 날린다
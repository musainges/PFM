# 3. urls 라는 필요한 파일을 만듦


from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

# 4.urls이란 파일에 필수적으로 필요한 코드를 추가함
#5. 최상위 urls 파일이 이 유알엘 파일을 연결해 줘야 한다
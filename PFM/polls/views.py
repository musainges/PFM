from django.shortcuts import render
from django.http import HttpResponse

# 1. 보여지는 코드 작성


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.


# 2. 이 작성한 코드를 호출하기 위해서 url코드를 작성하고 이 파일과 연결 해 줘야 함. url파일이 없기 때문에 생성해 줘야 한다.
"""
URL configuration for PFM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # 6. include 함수를 가져온다는 내용을 추가하고

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')), #7. polls 의 유알엘과 연결함, include 함수는 다른 url파일들을 참조하도록 도와줌
    ]

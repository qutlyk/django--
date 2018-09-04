"""MDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from codestudy.views import index,admin_login,func,add,add_message,edit,edit_message,del_user
from codestudy.views import sort_math,sort_chinese,sort_english,sort_sport,search



urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index),
    path('login/',admin_login),
    path('index/',func),
    path('index/add/',add),
    path('index/add/message/',add_message),
    path('edit_user/',edit),
    path('edit_user/edit_message/',edit_message),
    path('index/del_user/',del_user),
    path('index/math/',sort_math),
    path('index/chinese/',sort_chinese),
    path('index/english/',sort_english),
    path('index/sport/',sort_sport),
    path('index/search/',search),




]

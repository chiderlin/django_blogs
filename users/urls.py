
from django.urls import path, include

# 舊版本 現在不行! (login)
# from django.contrib.auth import views as auth_views 

from . import views

app_name = "users"
urlpatterns = [
    path('', include('django.contrib.auth.urls'), name="login"),
    path('', views.logout_views, name="logout"), #這裡不要設URL logout..會被導到後台頁面
    path('register/', views.register, name="register"),

]

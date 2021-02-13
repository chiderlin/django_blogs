from django.contrib import admin
from django.urls import path
from . import views

app_name = "blog_app"
urlpatterns = [
    path('homepage/',views.homepage, name="homepage"),
    path('newpost/', views.new_post, name="new_post"),
    path('editpost/<int:post_id>/', views.edit_post, name="edit_post"),

]

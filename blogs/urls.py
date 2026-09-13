from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("allposts/", views.blogposts, name="all-posts"),
    path("allposts/<slug:blog>/", views.blog_post, name="blog-post"),
]
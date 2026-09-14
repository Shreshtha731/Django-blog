from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("allposts/", views.all_posts, name="all-posts"),
    path("allposts/<slug:blog>/", views.blog_post, name="blog-post"),
]
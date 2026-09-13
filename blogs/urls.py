from django.urls import path
from . import views

urlpatterns=[
   path("",views.home_page,name="home"),
   path("allposts/",views.blogposts,name="all-posts"),   #app level basically the second leveldd  allpostss section
   path("allposts/<slug:blog>/",views.blog_post ,name="blog-post") #this syntax tells django that to any url after slash for allposts  under allposts section  name is used to name our url and name can be anything now in the above syntax instead of harcoding allposts we can use blog-post
  
]

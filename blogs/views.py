from datetime import date
from django.shortcuts  import render
from django.http import  HttpResponse,HttpResponseNotFound,Http404,HttpResponseRedirect
from django.urls import  reverse
from django.template.loader import render_to_string
from .models import Post
from .forms import CommentForm 

#reverse function allows us to create the paths by refering to the name


def home_page(request):
   latest_blogs=Post.objects.all().order_by("-date")[:2] #retunrs all the blogpost stored in database  "-" sorts all the date in descending order
   return render(request,"blogs/index.html",{"l_blogs":latest_blogs})  #the argument you pass in the given function is the template file

def process_blog_name(blog):
   blog_list=blog.split("-") #for  ex take Python-Core after using the slit func it transforms in ["Python","Core"] form and then by using " ".join it converts to Python Core
   return " ".join(blog_list)


def blogposts(request):
   blogs_details= Post.objects.all()
   return render(request,"blogs/allposts.html",{"blogs":blogs_details})

      
def blog_post(request,blog):
   post_data=Post.objects.get(slug=blog)
   tag_caption = post_data.tags.all()
   all_comments= post_data.comments.all().order_by("-id")

   if request.method =="POST":
      commented_data=request.POST
      form = CommentForm(commented_data)
      if form.is_valid():  #validates the input also validates that the form is valid or not
        
        comment=form.save(commit=False) # to save the data 
        comment.post=post_data
        comment.save()
        return HttpResponseRedirect(reverse("blog-post",args=[blog] )) #this line will redirect you to the page with slug name
      return render(request,"blogs/posts.html",{"post":post_data, "tags": tag_caption,"comment_form":form,"comments": all_comments})
   else:
       
       try: 

          form = CommentForm()
          return render(request,"blogs/posts.html",{"post":post_data, "tags": tag_caption,"comment_form":form,"comments": all_comments})
       except Exception:   
         raise Http404()  
      


def blog_post_by_number(request,blog):
   return HttpResponse(blog)    
# Create your views here.

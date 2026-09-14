from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment


def home_page(request):
    latest_posts = Post.objects.all().prefetch_related("tags")[:2]
    return render(request, "blogs/index.html", {
        "l_blogs": latest_posts,
    })


def all_posts(request):
    query = request.GET.get("q", "").strip()

    if query:
        posts = Post.objects.filter(title__istartswith=query).prefetch_related("tags")
    else:
        posts = Post.objects.all().prefetch_related("tags")

    return render(request, "blogs/allposts.html", {
        "all_posts": posts,
        "search_query": query,
    })


def blog_post(request, blog):
    post = get_object_or_404(
        Post.objects.prefetch_related("tags", "images", "comments"),
        slug=blog
    )

    if request.method == "POST":
        user_name = request.POST.get("user_name", "").strip()
        user_email = request.POST.get("user_email", "").strip()
        comment_text = request.POST.get("comment_text", "").strip()

        if user_name and user_email and comment_text:
            Comment.objects.create(
                user_name=user_name,
                user_email=user_email,
                comment_text=comment_text,
                post=post,
            )
        return redirect("blog-post", blog=post.slug)

    return render(request, "blogs/posts.html", {
        "post": post,
        "post_tags": post.tags.all(),
    })
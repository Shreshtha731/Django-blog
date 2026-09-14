from django.db import models
from django.core.validators import MinLengthValidator


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_add = models.EmailField(max_length=100)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.get_full_name()


class Tag(models.Model):
    caption = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=100)
    preview = models.CharField(max_length=250)
    content = models.TextField(validators=[MinLengthValidator(10)])
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, db_index=True)
    # Primary cover image for thumbnails and headers
    image = models.ImageField(upload_to="posts/", null=True, blank=True)
    author = models.ForeignKey(
        Author, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name="posts"
    )
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.title


class PostImage(models.Model):
    """Gallery table to support multiple images per post."""
    post = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE, 
        related_name="images"
    )
    image = models.ImageField(upload_to="posts/gallery/")
    caption = models.CharField(max_length=150, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.post.title}"


class Comment(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=100)
    comment_text = models.TextField(max_length=400)
    post = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE, 
        related_name="comments"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user_name} on {self.post.title}"
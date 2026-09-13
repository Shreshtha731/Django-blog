from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        #fields = ["user_name","user_email","comment_text"]
        exclude = ["post"]
        labels = {"user_name":"Your Name","user_email":"Your Email","comment_text":"Your Comment"}
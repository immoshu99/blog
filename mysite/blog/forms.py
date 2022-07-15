from django import forms
from django.forms import fields

from .models import Comment,Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')


class PostForm(forms.ModelForm):
    class Meta:

        model = Post
        fields = ('title','author','body')


from django import forms
from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from .models import Post
from .models import Comment

class MakePost(ModelForm):
    class Meta():
        model = Post
        fields = ["postinfo"]

class MakeComment(ModelForm):
    class Meta():
        model = Comment
        fields = ["description"]
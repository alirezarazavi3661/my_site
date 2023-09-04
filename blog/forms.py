from django import forms
from blog.models import Post,Comment
from django.forms import ModelForm
from captcha.fields import CaptchaField

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['post','name','email','subject','message']

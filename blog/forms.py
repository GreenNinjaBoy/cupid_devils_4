from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from . models import Blog

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = '__all__'
from django.shortcuts import render
from .models import Post, WorkingWith


def index(request):
    posts = Post.objects.all()
    working_with = WorkingWith.objects.all()
    return render(request, 'index.html', context={'posts': posts, 'working_with': working_with})


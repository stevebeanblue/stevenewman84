from django.shortcuts import render
from .models import Post, WorkingWith


def index(request):

    if request.method == 'GET':
        posts = Post.objects.all()
        working_with = WorkingWith.objects.filter(support=False)
        support = WorkingWith.objects.filter(support=True)

        return render(request, 'index.html', context={'posts': posts, 'working_with': working_with, 'support': support})



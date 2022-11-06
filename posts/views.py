from django.shortcuts import render
from .models import Post, WorkingWith, TopSection


def index(request):

    if request.method == 'GET':
        posts = Post.objects.all()
        working_with = WorkingWith.objects.filter(support=False)
        support = WorkingWith.objects.filter(support=True)
        top_section = TopSection.objects.get()

        return render(request, 'index.html', context={
            'posts': posts,
            'working_with': working_with,
            'support': support,
            'top_section': top_section,
        })



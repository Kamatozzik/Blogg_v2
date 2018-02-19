from django.shortcuts import render
from .models import PostConstructor


def post_list(request):
    posts = PostConstructor.objects.all()
    return render(request, 'newBlogg/index.html', {'posts': posts})

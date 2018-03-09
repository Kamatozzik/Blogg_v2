
from .models import PostConstructor
from django.shortcuts import get_object_or_404, render


def post_list(request):
    posts = PostConstructor.objects.all()
    return render(request, 'newBlogg/list.html', {'posts': posts})


def post_info(request, pk):
    PostConstructor.objects.get(pk=pk)
    post = get_object_or_404(PostConstructor, pk=pk)
    return render(request, 'newBlogg/post_info.html', {'post': post})

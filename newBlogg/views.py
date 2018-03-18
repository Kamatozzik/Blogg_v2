
from .models import PostConstructor
from django.shortcuts import get_object_or_404, render
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import redirect


def post_list(request):
    posts = PostConstructor.objects.all()
    return render(request, 'newBlogg/list.html', {'posts': posts})


def post_info(request, pk):
    PostConstructor.objects.get(pk=pk)
    post = get_object_or_404(PostConstructor, pk=pk)
    return render(request, 'newBlogg/post_info.html', {'post': post})


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.pubDate = timezone.now()
            post.save()
            return redirect('post_info', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'newBlogg/post_edit.html', {'form': form})









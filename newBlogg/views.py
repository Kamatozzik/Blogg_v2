from django.contrib.auth import authenticate, login

from .models import PostConstructor
from django.shortcuts import get_object_or_404, render
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm


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


def post_edit(request, pk):
    post = get_object_or_404(PostConstructor, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.pubDate = timezone.now()
            post.save()
            return redirect('post_info', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'newBlogg/post_edit.html', {'form': form})


def sign_in(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            my_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=my_password)
            login(request, user)
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request, 'newBlogg/registration_template.html', {'form': form})

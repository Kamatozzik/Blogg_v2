from django import forms
from .models import PostConstructor


class PostForm(forms.ModelForm):

    class Meta:
        model = PostConstructor
        fields = ('title', 'text')

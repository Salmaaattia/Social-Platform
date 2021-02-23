from django import forms 

from .models import Post


class PostForm(forms.Form):
    text = forms.CharField(label="Text", widget=forms.Textarea)

    class Meta:
        model = Post
        fields = ['content']

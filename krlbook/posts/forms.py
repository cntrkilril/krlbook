from django import forms
from .models import Post, Comment

class PostModelForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'wrap': 'hard','rows':1 , 'class': 'form-body__textarea', 'placeholder': 'Что у вас нового?'}))
    class Meta:
        model = Post
        fields = ('content', 'image')

class CommentModelForm(forms.ModelForm):
    body = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Добавить комментарий'}))
    class Meta:
        model = Comment
        fields = ('body',)


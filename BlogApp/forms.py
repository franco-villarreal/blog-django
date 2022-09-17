from django import forms

class CreatePostForm(forms.Form):
    title = forms.CharField(max_length=100)
    subtitle = forms.CharField(max_length=200)
    article = forms.CharField(max_length=10000)

class FindPostByUsernameForm(forms.Form):
    username = forms.CharField(max_length=100)

class CommentPostForm(forms.Form):
    message = forms.CharField(max_length=100)

class UpdatePostForm(forms.Form):
    title = forms.CharField(max_length=100)
    subtitle = forms.CharField(max_length=200)
    article = forms.CharField(max_length=10000)
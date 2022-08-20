from django.shortcuts import render

from BlogApp.models import Post

def home(request):
    posts = Post.objects.all()
    context = { "posts": posts }

    return render(request, 'BlogApp/home.html', context)

def findById(request, id):
    posts = Post.objects.filter(id=id)
    context = { "post": posts[0] }

    return render(request, 'BlogApp/post.html', context)

from django.shortcuts import render

from BlogApp.models import Blog

def home(request):
    blogs = Blog.objects.all()
    context = { "blogs": blogs }

    return render(request, 'BlogApp/home.html', context)

def findById(request, id):
    print(id)
    posts = Blog.objects.filter(id=id)
    print(posts[0].title)
    context = { "post": posts[0] }

    return render(request, 'BlogApp/post.html', context)

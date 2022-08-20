from django.shortcuts import render

from BlogApp.models import Blog

def findAll(request):
    blogs = Blog.objects.all()
    context = { "blogs": blogs }

    return render(request, 'blogs.html', context)

from datetime import datetime
from django.shortcuts import render
from BlogApp.forms import CreatePostForm, FindPostByUsernameForm
from BlogApp.models import Post, User

def home(request):
    posts = Post.objects.all()
    context = { "posts": posts }

    return render(request, 'BlogApp/home.html', context)

def findPostById(request, id):
    posts = Post.objects.filter(id=id)
    context = { "post": posts[0] }

    return render(request, 'BlogApp/post.html', context)

def createPost(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if(form.is_valid()):
            data = form.cleaned_data
            # TODO: User ID must be obtained from user session, once authentication is implemented
            userId = 1
            users = User.objects.filter(id=userId)
            user = users[0]

            post = Post(title=data.get('title'), subtitle=data.get('subtitle'), article=data.get('article'), user=user, created_at=datetime.now())
            post.save()

            return findPostById(request, post.id)

    context = {
        "form": CreatePostForm()
    }

    return render(request, 'BlogApp/create-post.html', context)

def findPostsByUsernameForm(request):
    if request.method == 'POST':
        form = FindPostByUsernameForm(request.POST)
        if(form.is_valid()):
            data = form.cleaned_data
            users = User.objects.filter(username=data.get('username'))
            posts = Post.objects.filter(user=users[0].id)

            context = {
                "posts": posts
            }

            # TODO: Create a view to list user's posts
            return render(request, 'BlogApp/home.html', context)
    
    context = {
        "form": FindPostByUsernameForm()
    }

    return render(request, 'BlogApp/find-posts-by-username.html', context)
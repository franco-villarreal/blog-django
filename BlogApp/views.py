from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from BlogApp.forms import CommentPostForm, CreatePostForm, FindPostByUsernameForm
from BlogApp.models import Post, PostComment, User

def findUsersByUsername(username):
    users = User.objects.filter(username=username)

    return users

def findUserByUsernameOrCreateIt(username):
    users = findUsersByUsername(username)

    if len(users) == 0:
        user = User(username=username)
        user.save()
    else:
        user = users[0]

    return user

@login_required
def home(request):
    if request.method == 'POST':
        form = FindPostByUsernameForm(request.POST)
        if(form.is_valid()):
            data = form.cleaned_data
            users = findUsersByUsername(data.get('username'))
            if not len(users) == 0:
                posts = Post.objects.filter(user=users[0].id)

                context = {
                    "posts": posts
                }

                return render(request, 'BlogApp/home.html', context)
    
    posts = Post.objects.all()
    context = { "user": request.user, "session": request.user.is_authenticated, "posts": posts, "form": FindPostByUsernameForm() }

    return render(request, 'BlogApp/home.html', context)

@login_required
def findPostById(request, id):
    posts = Post.objects.filter(id=id)
    post = posts[0]
    comments = PostComment.objects.filter(post=post)

    if request.method == 'POST':
        form = CommentPostForm(request.POST)
        if(form.is_valid()):
            data = form.cleaned_data
            user = findUserByUsernameOrCreateIt(request.user.username)
            comment = PostComment(post=posts[0], user=user, message=data.get('message'), created_at=datetime.now())
            comment.save()

            comments = PostComment.objects.filter(post=post)

    context = { "user": request.user, "session": request.user.is_authenticated, "post": post, "comments": comments, "form": CommentPostForm() }

    return render(request, 'BlogApp/post.html', context)

@login_required
def createPost(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if(form.is_valid()):
            data = form.cleaned_data
            users = User.objects.filter(username=request.user.username)

            if len(users) == 0:
                user = User(username=request.user.username)
                user.save()
            else:
                user = users[0]
            
            post = Post(title=data.get('title'), subtitle=data.get('subtitle'), article=data.get('article'), user=user, created_at=datetime.now())
            post.save()

            return findPostById(request, post.id)

    context = {
        "user": request.user, "session": request.user.is_authenticated,
        "form": CreatePostForm()
    }

    return render(request, 'BlogApp/create-post.html', context)

@login_required
def about(request):
    return render(request, 'BlogApp/about.html', {"user": request.user, "session": request.user.is_authenticated,})
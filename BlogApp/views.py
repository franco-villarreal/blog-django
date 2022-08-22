from datetime import datetime
from django.shortcuts import render
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

def home(request):
    if request.method == 'POST':
        form = FindPostByUsernameForm(request.POST)
        if(form.is_valid()):
            data = form.cleaned_data
            users = findUsersByUsername(data.get('username'))
            posts = Post.objects.filter(user=users[0].id)

            context = {
                "posts": posts
            }

            return render(request, 'BlogApp/home.html', context)
    
    posts = Post.objects.all()
    context = { "posts": posts, "form": FindPostByUsernameForm() }

    return render(request, 'BlogApp/home.html', context)

def findPostById(request, id):
    posts = Post.objects.filter(id=id)
    post = posts[0]
    comments = PostComment.objects.filter(post=post)

    if request.method == 'POST':
        form = CommentPostForm(request.POST)
        if(form.is_valid()):
            data = form.cleaned_data
            user = findUserByUsernameOrCreateIt(data.get('username'))
            comment = PostComment(post=posts[0], user=user, message=data.get('message'), created_at=datetime.now())
            comment.save()

            comments = PostComment.objects.filter(post=post)

    context = { "post": post, "comments": comments, "form": CommentPostForm() }

    return render(request, 'BlogApp/post.html', context)

def createPost(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if(form.is_valid()):
            data = form.cleaned_data
            # TODO: User ID must be obtained from user session, once authentication is implemented
            users = User.objects.filter(username=data.get('author'))

            if len(users) == 0:
                user = User(username=data.get('author'))
                user.save()
            else:
                user = users[0]
            
            post = Post(title=data.get('title'), subtitle=data.get('subtitle'), article=data.get('article'), user=user, created_at=datetime.now())
            post.save()

            return findPostById(request, post.id)

    context = {
        "form": CreatePostForm()
    }

    return render(request, 'BlogApp/create-post.html', context)
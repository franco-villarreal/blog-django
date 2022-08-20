from django.db import models

class User(models.Model):
    username = models.CharField(max_length=40)

class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    article = models.CharField(max_length=10000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField()

class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    

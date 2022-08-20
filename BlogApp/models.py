from turtle import title
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)

class Blog(models.Model):
    title = models.CharField(max_length=100)
    article = models.CharField(max_length=10000)
    author_id = models.IntegerField()
    created_at = models.DateTimeField()

class BlogComment(models.Model):
    blog_id = models.IntegerField()
    username = models.CharField(max_length=15)
    message = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    

from django.urls import path
from BlogApp.views import home, findPostById, createPost

urlpatterns = [
    path('', home, name="BlogAppHome"),
    path('posts/', createPost, name="BlogAppNewPost"),
    path('posts/(?P<id>\d+)/$', findPostById, name="BlogAppPosts"),
]
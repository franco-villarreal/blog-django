from django.urls import path
from BlogApp.views import home, findPostById, createPost, findPostsByUsernameForm

urlpatterns = [
    path('', home, name="BlogAppHome"),
    path('posts/', createPost, name="BlogAppNewPost"),
    path('posts/(?P<id>\d+)/$', findPostById, name="BlogAppPosts"),
    path('posts/search', findPostsByUsernameForm, name='BlogAppFindPostsByUsername')
]
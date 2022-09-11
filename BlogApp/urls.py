from django.urls import path
from BlogApp.views import home, findPostById, createPost

urlpatterns = [
    path('pages/', home, name="BlogAppHome"),
    path('pages/', createPost, name="BlogAppNewPost"),
    path('pages/(?P<id>\d+)/$', findPostById, name="BlogAppPosts"),
]
from django.urls import path
from BlogApp.views import about, home, findPostById, createPost

urlpatterns = [
    path('', home, name="BlogAppHome"),
    path('pages/', createPost, name="BlogAppNewPost"),
    path('pages/(?P<id>\d+)/$', findPostById, name="BlogAppPosts"),
    path('about/', about, name="BlogAppAbout")
]
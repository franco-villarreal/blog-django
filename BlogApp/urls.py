from django.urls import path
from BlogApp.views import about, deletePostComment, home, findPostById, createPost, posts

urlpatterns = [
    path('', home, name="BlogAppHome"),
    path('pages/', posts, name="BlogAppPosts"),
    path('pages/create', createPost, name="BlogAppNewPost"),
    path('pages/(?P<id>\d+)/$', findPostById, name="BlogAppPostDetail"),
    path('pages/<postId>/comments/<commentId>/delete', deletePostComment, name="BlogAppDeletePostComment"),
    path('about/', about, name="BlogAppAbout")
]
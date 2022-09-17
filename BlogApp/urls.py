from django.urls import path
from BlogApp.views import about, deletePostComment, home, findPostById, createPost, posts, editPostById, deletePostById

urlpatterns = [
    path('', home, name="BlogAppHome"),
    path('pages/', posts, name="BlogAppPosts"),
    path('pages/create', createPost, name="BlogAppNewPost"),
    path('pages/(?P<id>\d+)/$', findPostById, name="BlogAppPostDetail"),
    path('pages/(?P<id>\d+)/$/edit', editPostById, name="BlogAppPostEdit"),
    path('pages/(?P<id>\d+)/$/delete', deletePostById, name="BlogAppPostDelete"),
    path('pages/<postId>/comments/<commentId>/delete', deletePostComment, name="BlogAppDeletePostComment"),
    path('about/', about, name="BlogAppAbout")
]
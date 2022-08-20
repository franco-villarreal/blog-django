from django.urls import path
from BlogApp.views import home, findById

urlpatterns = [
    path('', home, name="BlogAppHome"),
    path('posts/(?P<id>\d+)/$', findById, name="BlogAppPosts"),
]
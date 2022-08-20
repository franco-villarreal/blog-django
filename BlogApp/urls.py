from django.urls import path
from BlogApp.views import home, findById

urlpatterns = [
    path('', home, name="BlogAppHome"),
    path('blogs/', home, name="BlogAppHome"),
    path('blogs/(?P<id>\d+)/$', findById, name="BlogAppBlogs"),
]
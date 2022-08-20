from django.urls import path
from BlogApp.views import findAll

urlpatterns = [
    path('blogs/', findAll, name="blogs"),
]
from django.urls import path
from AuthApp.views import sign_in

urlpatterns = [
    path('sign-in/', sign_in, name="AuthAppSignIn"),
]
from django.urls import path
from django.contrib.auth.views import LogoutView
from AuthApp.views import sign_in, sign_up

urlpatterns = [
    path('sign-in/', sign_in, name="AuthAppSignIn"),
    path('sign-up/', sign_up, name="AuthAppSignUp"),
    path('sign-out/', LogoutView.as_view(template_name='AuthApp/sign-out.html'), name = 'AuthAppSignOut')
]
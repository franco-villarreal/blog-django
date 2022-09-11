from django.contrib.auth.forms import AuthenticationForm, authenticate, UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect

def sign_in(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            username = data.get('username')
            password = data.get('password')

            user = authenticate(username=username, password=password)
        
            if user:
                login(request, user)
                messages.info(request, 'Sign in successfully')
            else:
                messages.error(request, 'Error trying to sign in')
                
        return redirect('BlogAppHome')
    
    context = {
        'form': AuthenticationForm()
    }

    return render(request, 'AuthApp/sign-in.html', context)

def sign_up(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('BlogAppHome')
        else:
            messages.error(request, 'Error trying to sign up')
            return redirect('AuthAppSignUp')
        
    else:
        form = UserCreationForm()

    return render(request, "AuthApp/sign-up.html", {"form": form})
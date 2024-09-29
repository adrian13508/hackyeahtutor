# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomLoginForm


def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('chat:user_panel')  # Change 'home' to your desired redirect URL
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = CustomLoginForm()

    return render(request, 'registration/login.html', {'form': form})

# your_app_name/views.py
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages



# Create your views here.
# render homepage
def home(request):
    return render(request, 'home.html')






def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Replace 'home' with the URL name of your home page
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})



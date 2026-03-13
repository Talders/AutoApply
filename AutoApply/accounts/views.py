from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import CustomUserCreationForm

@login_required
def home(request):
    return render(request, "home.html")

def register(request):
    if request.user.is_authenticated: #Wenn bereits eingeloggt, auf Home weiterleiten
        return redirect("home")
    
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})
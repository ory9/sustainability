from django.shortcuts import render

def home(request):
    return render(request, "home.html", {})

def login(request):
    return render(request, "1-user-login.html", {})
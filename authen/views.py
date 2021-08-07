from django.shortcuts import render

def register(request):

    return render(request, 'authen/register.html')

def login(request):

    return render(request, 'authen/login.html')

def logout(request):

    return render(request, 'authen/logout.html')
from django.shortcuts import render, redirect
from django.contrib  import messages
from validate_email import validate_email
# from .models import User

def register(request):
    if request.method == "POST":
        context = {'has_error': False, 'data': request.POST}
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if len(password) < 6:
            messages.add_message(request, messages.ERROR, 'password too short')
            context['has_error'] = True

        if not validate_email(email):
            messages,add_message(request, messages.ERROR, 'enter a valid email')
            context['has_error'] = True

        # if User.objects.filter(username = username).exists():
        #     messages,add_message(request, messages.ERROR, 'username taken')
        #     context['has_error'] = True

        # if User.objects.filter(email = email).exists():
        #     messages,add_message(request, messages.ERROR, 'email taken')
        #     context['has_error'] = True

        if context['has_error']:
            return   render(request, 'authen/register.html', context)  
    
        # user = User.objects.create_user(username= username, email= email)
        # user.set_password(password)
        # user.save()

        messages.add_message(request, messages.SUCCESS, 'account created')
        return redirect('login')


    return render(request, 'authen/register.html')

def login(request):

    return render(request, 'authen/login.html')

def logout(request):

    return render(request, 'authen/logout.html')
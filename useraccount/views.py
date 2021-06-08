from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')

        else:
            messages.info(request, "invalid Credentials")
            return redirect('login')

    else:
        return render(request, 'login1.html')

def register(request):

    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        password1 = request.POST['password1']
        email = request.POST['email']

        if(password == password1):
            if User.objects.filter(username=username).exists():
                messages.info("Username is already used")
                return redirect('register')
            else:
                user = User.objects.create_user(password=password1, email=email, first_name = first_name, last_name = last_name)
                user.save()

        return redirect('/')
    else:
        return render(request, 'register.html')
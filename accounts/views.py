from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register(request):
    if request.method == 'POST':
        Firstname = request.POST['Firstname']
        Lastname = request.POST['Lastname']
        Email = request.POST['Email']
        Username = request.POST['Username']
        Password = request.POST['Password']
        Password2 = request.POST['Password2']

        if Password == Password2:
            if User.objects.filter(username=Username).exists():
                messages.error(request, 'Username already exists')
                return redirect('register')
            else:
                 if User.objects.filter(email=Email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('register')
                 else:
                    user = User.objects.create(username=Username,password=Password, email=Email,first_name=Firstname, last_name=Lastname)
                    user.save()
                    messages.success(request, 'you can now login') 
                    return redirect('signin')


    return render(request, 'accounts/register.html')

# def signin(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('profile')
#         else:
#             return redirect('register')

#     return render(request, 'accounts/signin.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
            
    return render(request, 'accounts/signin.html')

def profile(request):
    return render(request, 'accounts/profile.html')

def signout(request):
    logout(request)
    return redirect('profile')

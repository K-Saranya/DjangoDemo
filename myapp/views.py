from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User


# Create your views here.

def index_page(request):
    return render(request, 'index.html')

def get_data(request):
    products = Dress.objects.all()
    print("Inside view")
    return render (request, 'products.html', {"products":products}) 


def signup(request):
    print("Inside view")
    return render(request, 'signup.html')

def login(request):
    print("Inside view")
    return render(request, 'login.html')

def signup_function(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                return redirect('signup')
            elif User.objects.filter(email = email).exists():
                return redirect('signup')
            else:
                user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                user.save()
                return redirect('login')
            
        else:
            return redirect('signup')
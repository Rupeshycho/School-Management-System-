from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from .forms import RegisterForm   

from django.contrib import messages

from django.contrib.auth.decorators import login_required


# Create your views here.
def register_view(request):
    if request.method== 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully!")
            return redirect('login')
        
    else: 
        form=RegisterForm()
    return render(request, 'accounts/register.html', {'form':form})

def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user =authenticate(request, username=username, password=password)
        
        if user: 
            login (request, user)
            return(redirect('dashboard'))
    return render(request, 'accounts/login.html')
@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')

def logout_view(request): 
    logout(request)
    return redirect('login')            
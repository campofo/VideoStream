from django.shortcuts import render,HttpResponse,redirect
from .forms import LoginForm,SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def login(request):
    form =LoginForm()
    if request.method=='POST':
        form =LoginForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user= authenticate(request,username=username,password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'You have successfully logged in.')
                return redirect(home)
            else:
                messages.error(request,'Invalid email or password.')
        else:
            messages.error(request,'form error.')
    return render(request,'videoapp/index.html',{'form':form})
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect(home)
    else:
        form = SignUpForm()
    return render(request, 'videoapp/signup.html', {'form': form})

@login_required
def logout(request):
    logout(request)
    redirect(login)

@login_required
def home(request):
    return HttpResponse('logged in')
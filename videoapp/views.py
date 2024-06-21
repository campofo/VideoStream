from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import LoginForm,SignUpForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import Videos
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from .tokens import account_activation_token
from django.db import IntegrityError

# Create your views here.
def login(request):
    form =LoginForm()
    if request.method=='POST':
        form =LoginForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user= authenticate(request,username=username,password=password)
            if user:
                auth_login(request, user)
                video=Videos.objects.all()
                first= video.first()
                if first:
                    return redirect('home', pk=first.pk)  
            else:
                messages.error(request,'Invalid email or password.')
    return render(request,'videoapp/index.html',{'form':form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                form.send_verification_email(user,request)
                messages.success(request,'Please confirm your email address to complete the registration.')
            except IntegrityError:
                messages.error(request,'Email already exist. Please choose a different email') 
    else:
        form = SignUpForm()
    return render(request, 'videoapp/signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Your account has been confirmed.')
        return redirect('login')
    else:
        messages.error(request, 'The confirmation link was invalid, possibly because it has already been used.')
        return redirect('signup')


@login_required
def logout(request):
    auth_logout(request)
    return redirect('login')

@login_required
def home(request, pk):
    video = get_object_or_404(Videos, pk=pk)
    prev_video = Videos.objects.filter(pk__lt=video.pk).order_by('-pk').first()
    next_video = Videos.objects.filter(pk__gt=video.pk).order_by('pk').first()
    return render(request, 'videoapp/home.html', {
        'video': video,
        'prev_video':prev_video,
        'next_video':next_video
        #'next_video': next_video.video_file,
        #'prev_video': prev_video.video_file,
    }
    )
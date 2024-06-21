from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from .tokens import account_activation_token

class SignUpForm(UserCreationForm):
    password2=forms.CharField(required=True,widget=forms.PasswordInput(),label='Confirm Password')
    class Meta:
        model = User
        fields = ('email','first_name','last_name','password1', 'password2')
    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.username = self.cleaned_data['email']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    def send_verification_email(self, user, request):
        current_site = get_current_site(request)
        mail_subject = 'Activate your account.'
        message = render_to_string('videoapp/account_activation_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        to_email = self.cleaned_data.get('email')
        send_mail(mail_subject, message, settings.DEFAULT_FROM_EMAIL, [to_email])
    

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('email', 'password')


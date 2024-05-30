from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    password2=forms.CharField(required=True,widget=forms.PasswordInput(),label='Confirm Password')
    class Meta:
        model = User
        fields = ('email','first_name','last_name','password1', 'password2')
    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.username = self.cleaned_data['email']  # Set username to be the same as email
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
    

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('email', 'password')


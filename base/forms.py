from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from .models import ContactInquiry
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1','password2']
        widgets = {
            'username':forms.TextInput(attrs={'class': 'input'}),
            'first_name':forms.TextInput(attrs={'class': 'input'}),
            'last_name':forms.TextInput(attrs={'class': 'input'}),
            'email':forms.EmailInput(attrs={'class': 'input'}),
            'password1':forms.PasswordInput(attrs={'class': 'input'}),
            'password2':forms.PasswordInput(attrs={'class': 'input'}),
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']



class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactInquiry
        fields = ['name', 'email', 'message']
        
class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category','name', 'description', 'post_pic',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()


class SearchForm(forms.Form):
    query = forms.CharField(label='Search')


class RegistrationForm(UserCreationForm):
    email = forms.CharField(required=True, widget=forms.EmailInput(
        attrs={'placeholder':'Email *'}))
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder':'Username *'}))
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'placeholder':'Password *'}))
    password2 = forms.CharField(label='Confirm Password(again)',
                                widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password *'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(
            attrs={})}


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True,'placeholder':'Username *'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password','placeholder':'Password *'}))

class OTPVerificationForm(forms.Form):
    otp_code = forms.CharField(max_length=6, widget=forms.TextInput(attrs={'class': 'form-control'}))
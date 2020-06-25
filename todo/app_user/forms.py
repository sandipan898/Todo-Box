from django.contrib.auth.forms import UserCreationForm, UsernameField
# from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth import models
from django.contrib.auth.password_validation import password_validators_help_text_html
# from allauth.account.forms import SignupForm
# from django.core import validators
# from django.contrib.auth.password_validation import UserAttributeSimilarityValidator, MinimumLengthValidator
# from django.contrib.auth.validators import UnicodeUsernameValidator

from allauth.account.forms import SignupForm 


"""
    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_datad['last_name']
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
        """

class MySignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={
                    'class': 'form-control',
                    'style': 'width: 500px',
        }))
    first_name = forms.CharField(label="First name", max_length=100, 
                widget=forms.TextInput(attrs={
                    'class': 'form-control',
                    'style': 'width: 500px',
        })
    )
    last_name = forms.CharField(label="Last name", max_length=100, widget=forms.TextInput(attrs={
                    'class': 'form-control',
                    'style': 'width: 500px',
        }))
    
    user_name = UsernameField(widget=forms.TextInput(attrs={
                    'class': 'form-control',
                    'style': 'width: 500px',
        }))
    password1 = forms.CharField(
                    widget=forms.PasswordInput(attrs={
                    'class': 'form-control',
                    'style': 'width: 500px',
                    'autocomplete': 'new-password',
                    }), help_text=password_validators_help_text_html())
    password2 = forms.CharField(
                    widget=forms.PasswordInput(attrs={
                    'class': 'form-control',
                    'style': 'width: 500px',
                    'autocomplete': 'new-password',
                    }), help_text=("Enter the same password as before, for verification."))

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "user_name",
            "email",
            "password1",
            "password2"
        ]
    
        def clean_user_name(self):
            username = self.cleaned_data['username']
            if len(username) < 2:
                raise forms.ValidationError("Username is too short")
            elif User.objects.get(username=username):
                raise forms.ValidationError("This username is already taken")
            return username

# class MySignUpForm(SignupForm): 
# 	first_name = forms.CharField(max_length=30, label='First Name',) 
# 	last_name = forms.CharField(max_length=30, label='Last Name') 

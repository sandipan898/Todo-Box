from django.contrib.auth.forms import UserCreationForm, UsernameField
from django import forms
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth import models
from allauth.account.forms import SignupForm
from django.core import validators
from django.contrib.auth.password_validation import UserAttributeSimilarityValidator, MinimumLengthValidator
from django.contrib.auth.validators import UnicodeUsernameValidator


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
    email = forms.EmailField(label="Email",)
    first_name = forms.CharField(label="First name")
    last_name = forms.CharField(label="Last name")
    
    #user_name = UsernameField()

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            #"user_name",
            "email",
        ]

        def clean_user_name(self):
            username = self.cleaned_data['username']
            if len(username) < 2:
                raise forms.ValidationError("Username is too short")
            """
            elif User.objects.get(username=username):
                raise forms.ValidationError("This username is already taken")
            """
            return username
            
        """
        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control'}),
            "username": forms.TextInput(attrs={'class': 'form-control'}),
            #"email": forms.EmailField(attrs={'class': 'from-control'}),
            "password1": forms.PasswordInput(attrs={'class': 'form-control'}),
            "password2": forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        """

from django.contrib.auth.forms import UserCreationForm, UsernameField
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import models
from django.contrib.auth.password_validation import password_validators_help_text_html
from allauth.account.forms import SignupForm, LoginForm
from django.shortcuts import get_object_or_404
 
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
                    #'style': 'width: 500px',
        }))
    first_name = forms.CharField(label="First name", max_length=100, 
                widget=forms.TextInput(attrs={
                    'class': 'form-control',
                    #'style': 'width: 500px',
        })
    )
    last_name = forms.CharField(label="Last name", max_length=100, widget=forms.TextInput(attrs={
                    'class': 'form-control',
                    #'style': 'width: 500px',
                }))
    username = UsernameField(widget=forms.TextInput(attrs={
                    'class': 'form-control',
                    #'style': 'width: 500px',
                }))
    password1 = forms.CharField(
                    label="Password",
                    widget=forms.PasswordInput(attrs={
                    'class': 'form-control',
                    #'style': 'width: 500px',
                    'autocomplete': 'new-password',
                    }), help_text=password_validators_help_text_html()
                )
    password2 = forms.CharField(
                    label="Re-enter Password",
                    widget=forms.PasswordInput(attrs={
                    'class': 'form-control',
                    #'style': 'width: 500px',
                    'autocomplete': 'new-password',
                    }), help_text=("Enter the same password as before, for verification.")
                )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2"
        ]
        
        def clean_username(self):
            username = self.cleaned_data['username']
            if len(username) < 2:
                raise forms.ValidationError("Username is too short")
            elif User.objects.get_object_or_404(username=username):
                raise forms.ValidationError("This username is already taken")
            return username

    
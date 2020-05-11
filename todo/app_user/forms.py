from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class MySignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email",)
    first_name = forms.CharField(label="First name")
    last_name = forms.CharField(label="Last name")
    user_name = forms.CharField(label="username")

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "user_name"
            "email",
        ]

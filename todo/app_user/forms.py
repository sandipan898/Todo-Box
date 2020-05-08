from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    
    email = forms.EmailField(label = "Email", )
    first_name = forms.CharField(label = "First name")
    last_name = forms.CharField(label = "Last name")

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", )


    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_datad['last_name']
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
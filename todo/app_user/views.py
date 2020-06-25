from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from .forms import MySignUpForm
from django.contrib.auth.models import User
from allauth.account.views import SignupView
from django.contrib.auth.forms import UserCreationForm
from .forms import MySignUpForm
from django.contrib.auth.models import User
from allauth.account.views import SignupView


def user_home_view(request):
    template_name = "app_user/user_home.html"
    context = {}
    return render(request, template_name, context)


class MySignUpView(UserCreationForm):
   form_class = MySignUpForm
   template_name = "app_user/signup_form.html"
   success_url = reverse_lazy('user_login')
   
   def get(self, request, *args, **kwargs):
        #GET method
        form = MySignUpForm()
        context = {'form': form}
        return render(request, self.template_name, context)

   #redirect_field_name = "user_login"
"""   def get_success_url(self):
    return '/user/login'"""

"""
def signup_form(request):
    template_name = "app_user/signup_form.html"
    
    if request.method == 'POST':
        form = MySignUpForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            profile = user.userprofile
            user_group = form.cleaned_data.get('user_type')
            profile.user_type = user_group
            profile.save()
            form.save()
            return redirect('/')
    else:
        form = MySignUpForm()
    return render(request, template_name, {'form': form})
"""


def signup_form(request):
    template_name = "app_user/signup_form.html"
    context = {}
    if request.method == "POST":
        form = MySignUpForm(request.POST or None)
        print(request.POST)
        print(form.errors)
        context['form'] = form
        if form.is_valid() and form.errors:
            form.save()
        return redirect("user_login")
    else:
        form = MySignUpForm()
        context['form'] = form
    return render(request, template_name, context)


class MySignUpView(CreateView):
    form_class = MySignUpForm
    template_name = "app_user/signup_form.html"
    success_url = reverse_lazy('user_login')


"""
class MySignUpView(SignupView):
    template_name = "app_user/signup_form.html"
    form_class = MySignUpForm
    success_url = reverse_lazy('user_login')

    form_class = MySignUpForm
    success_url = reverse_lazy('user_login')
"""

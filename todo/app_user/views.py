from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignUpForm


def user_home_view(request):
    template_name = "app_user/user_home.html"
    context = {}
    return render(request, template_name, context)


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "app_user/signup_form.html"
    success_url = reverse_lazy('/')

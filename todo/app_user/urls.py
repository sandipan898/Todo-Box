from django.urls import path
from .views import signup_form, user_home_view, MySignUpView
from django.contrib.auth.views import LoginView, LogoutView
from allauth.account.views import SignupView


urlpatterns = [
    path('home/', user_home_view, name='user_home'),
    path('login/', LoginView.as_view(template_name="app_user/login_form.html"), name='user_login'),
    path('logout/', LogoutView.as_view(), name='user_logout'),
    #path('signup/', MySignUpView.as_view(), name='user_signup'),
    path('signup/', signup_form, name='user_signup'),
    #path('signup/', SignupView.as_view(), name='user_signup'),
]

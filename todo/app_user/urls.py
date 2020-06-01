from django.urls import path
<<<<<<< ./todo/app_user/urls_LOCAL_6387.py
from .views import signup_form, user_home_view, MySignUpView
||||||| ./todo/app_user/urls_BASE_6387.py
from .views import SignUpView, user_home_view
=======
from .views import signup_form, user_home_view, MySignUpView
>>>>>>> ./todo/app_user/urls_REMOTE_6387.py
from django.contrib.auth.views import LoginView, LogoutView
<<<<<<< ./todo/app_user/urls_LOCAL_6387.py
from allauth.account.views import SignupView

||||||| ./todo/app_user/urls_BASE_6387.py
=======
from allauth.account.views import SignupView

>>>>>>> ./todo/app_user/urls_REMOTE_6387.py

urlpatterns = [
    path('home/', user_home_view, name='user_home'),
    path('login/', LoginView.as_view(template_name="app_user/login_form.html"), name='user_login'),
    path('logout/', LogoutView.as_view(), name='user_logout'),
    path('signup/', MySignUpView.as_view(), name='user_signup'),
    #path('signup/', signup_form, name='user_signup'),
    #path('signup/', SignupView.as_view(), name='user_signup'),
]

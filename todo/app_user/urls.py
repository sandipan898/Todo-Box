from django.urls import path
from .views import SignUpView, user_home_view
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('home/', user_home_view, name='user_home'),
    path('login/', LoginView.as_view(template_name="app_user/login_form.html"), name='user_login'),
    path('logout/', LogoutView.as_view(), name='user_logout'),
    path('signup/', SignUpView.as_view(), name='user_signup'),
]
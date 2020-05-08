from django.urls import path, include
from .views import home_view, delete, done, undone, update, welcome_view, help_view, about_view, contact_view

urlpatterns = [
    path('', welcome_view, name='welcome'),
    path('home/', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('help/', help_view, name='help'),
    path('contact/', contact_view, name='contact'),
    path('delete/<int:id>', delete, name='delete'),
    path('done/<int:id>', done, name='mark_done'),
    path('undone/<int:id>', undone, name='mark_undone'),
    path('update/<int:id>', update, name='update'),
]
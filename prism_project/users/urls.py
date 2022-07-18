from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('edit_user/', views.editUser, name='edit_user'),
    path('password/', views.editPass, name='pass_change'),
    path('profile/', views.index, name='profile'),
]

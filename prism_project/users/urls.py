from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/', views.index, name='profile'),
]


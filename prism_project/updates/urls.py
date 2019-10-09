from django.urls import path
from . import views

urlpatterns = [
    #pattern as follows path('subpage', views function, name)
    path('', views.home, name='pages-home'),
]
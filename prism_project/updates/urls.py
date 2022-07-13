from django.urls import path
from . import views

urlpatterns = [
    #pattern as follows path('subpage', views function, name)
    path('', views.index, name='updates-index'),
]

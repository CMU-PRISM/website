from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('door-toggle', views.doorToggle, name="door-toggle")
]

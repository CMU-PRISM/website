from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('door-open', views.doorOpen, name="door-open"),
    path('door-close', views.doorClose, name="door-close"),
    path('door-busy', views.doorBusy, name="door-busy")
]

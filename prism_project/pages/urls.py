from django.urls import path
from . import views

urlpatterns = [
    #pattern as follows path('subpage', views function, name)
    path('', views.home, name='pages-home'),
    path('about/', views.about, name='pages-about'),
    path('resources/', views.resources, name='pages-about'),
    path('office-hours/', views.officeHours, name='pages-office-hours'),
    path('activities/', views.activities, name='pages-activities'),
    path('activism/', views.activities, name='pages-activism'),
    path('social/', views.social, name='pages-social'),
    path('support-groups/', views.supportGroups, name='pages-support-groups'),
    path('contact/', views.contact, name='pages-contact'),
]
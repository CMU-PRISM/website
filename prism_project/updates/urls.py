from django.urls import path
from . import views

urlpatterns = [
    #pattern as follows path('subpage', views function, name)
    path('', views.index, name='updates-index'),
    path('<str:title>', views.update_viewer, name="update-viewer"), # softcoded match. Any /page/number matches and sends id to views.page_viewer
]
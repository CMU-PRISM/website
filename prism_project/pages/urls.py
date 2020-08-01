from django.urls import path
from . import views

# paterns for /pages/ pages
urlpatterns = [
    #pattern as follows path('subpage', views function, name)
    path('', views.index, name='pages-index'), # hardcoded match. Any /page/ runs views.index
    path('about/', views.about, name='pages-about'),
    path('<int:id>/<str:slug>', views.page_viewer, name="page-viewer") # softcoded match. Any /page/number matches and sends id to views.page_viewer
]

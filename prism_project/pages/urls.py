from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

# paterns for /pages/ pages
urlpatterns = [
    #pattern as follows path('subpage', views function, name)
    path('', views.index, name='pages-index'), # hardcoded match. Any /page/ runs views.index
    path('<str:title>', views.page_viewer, name="page-viewer"), # softcoded match. Any /pages/title matches to views.page_viewer
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/prismdoglowresNOBG.ico'))), # favicon linking for browsers
]

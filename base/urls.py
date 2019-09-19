from django.urls import path, re_path
from base.views import indexView, projectView, configurationView, dashboardView


urlpatterns = [
   path(r'index/', indexView, name='indexpage'),
   path(r'project/', projectView, name='projectpage'),
   path(r'configuration/', configurationView, name='configurationpage'),
   path(r'dashboard/', dashboardView, name='dashboardpage'),
]
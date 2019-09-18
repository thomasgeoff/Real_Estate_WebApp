#To add path
from django.urls import path

#From all import views
from . import views

urlpatterns = [
    #path(location,method,name)
    path('',views.index, name = 'index'),
    path('about',views.about, name = 'about'),
]
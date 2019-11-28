#To add path
from django.urls import path

#From all import views
from . import views

urlpatterns = [
    #path(location,method,name)
    path('login',views.login, name = 'login'),
    path('register',views.register, name = 'register'),
    path('logout',views.logout, name = 'logout'),
    path('dashboard',views.dashboard, name = 'dashboard'),
]
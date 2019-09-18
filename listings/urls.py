#To add path
from django.urls import path

#From all import views
from . import views

urlpatterns = [
    #path(location,method,name)
    path('',views.index, name = 'listings'),
    path('<int:listing_id>',views.listing, name = 'listing'),
    path('search',views.search, name = 'search')
]
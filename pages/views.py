from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing
from realtors.models import Realtor


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings
    }
    #return HttpResponse('<h1>Hello World</h1>')
    return render(request, 'pages/index.html',context)

def about(request):
    realtors = Realtor.objects.order_by('hire_date')

    context ={
        'realtors':realtors
    }
    return render(request, 'pages/about.html',context)

from django.shortcuts import render
#from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator 

from .models import Listing

def index(request):
    #return HttpResponse('<h1>Hello World</h1>')
    #listings = Listing.objects.all()
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    #paginator
    paginator = Paginator(listings,3)
    page = request.GET.get('page')
    paged_listed = paginator.get_page(page)

    context = {
        #'listings': listings
        'listings': paged_listed
    }
    return render(request, 'listings/listings.html',context)

def listing(request,listing_id):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')
    
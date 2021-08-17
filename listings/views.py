from django.shortcuts import render
from django.http import HttpResponse
from .models import Listing;
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator




def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6);
    page = request.GET.get("page");
    page_listing = paginator.get_page(page)
    contex = {
        'listings':page_listing
    }
    return render(request, 'listings/listings.html',contex);

def listing(request, listing_id):
    return render(request, 'listings/listing.html');

def search(request):
    return render(request, 'listings/search.html');
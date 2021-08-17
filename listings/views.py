from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Listing;
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import bedroom_choices, state_choices, price_choices




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
    listing = get_object_or_404(Listing, pk=listing_id);
    contex = {
        'listing':listing,
    }
    return render(request, 'listings/listing.html', contex);

def search(request):
    queryset_list = Listing.objects.order_by("-list_date");

    # keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords'];
        if keywords:
            queryset_list = queryset_list.filter(description__icontains= keywords);
    # city
    if 'city' in request.GET:
        city = request.GET['city'];
        if city:
            queryset_list = queryset_list.filter(city__iexact= city);
    # state
    if 'state' in request.GET:
        state = request.GET['state'];
        if state:
            queryset_list = queryset_list.filter(state__iexact= city);
    
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms'];
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte= city);
    # price
    if 'price' in request.GET:
        price = request.GET['price'];
        if price:
            queryset_list = queryset_list.filter(price__lte= city);

    contex = {
         'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        'state_choices':state_choices,
        'listings':queryset_list,
        'value':request.GET
    }
    return render(request, 'listings/search.html', contex);
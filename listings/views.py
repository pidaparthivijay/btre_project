from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . models import Listing
from listings.choices import price_choices, state_choices, bedroom_choices
# Create your views here.


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {'listings': paged_listings}
    return render(request, 'listings/listings.html', context)


def listing(request, listingId):
    listing = get_object_or_404(Listing, pk=listingId)
    context = {'listing': listing, 'bedroom_choices': bedroom_choices}
    return render(request, 'listings/listing.html', context)


def search(request):
    querySetList = Listing.objects.order_by(
        '-list_date').filter(is_published=True)
    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            querySetList = querySetList.filter(description__icontains=keywords)
    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            querySetList = querySetList.filter(city__iexact=city)
    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            querySetList = querySetList.filter(state__icontains=state)
    # City
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            querySetList = querySetList.filter(bedrooms__lte=bedrooms)
    # MaxPrice
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            querySetList = querySetList.filter(price__lte=price)
    context = {
        'searchResults': querySetList,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)

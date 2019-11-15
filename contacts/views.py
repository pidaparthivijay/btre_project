from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
# Create your views here.


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        user_id = request.POST['user_id']
        phone = request.POST['phone']
        realtor_email = request.POST['realtor_email']
        message = request.POST['message']
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(
                    request, 'You already have made an enquiry on this property')
                return redirect('dashboard')
        contact = Contact(listing=listing, listing_id=listing_id, name=name,
                          email=email, phone=phone, message=message, user_id=user_id)
        contact.save()
        messages.success(
            request, 'Your request has been successfully submitted, the realtor will get back to you soon')
        return redirect('/listings/'+listing_id)

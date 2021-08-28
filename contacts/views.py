from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail

# Create your views here.

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id'];
        listing = request.POST['listing'];
        name = request.POST['name'];
        email = request.POST['email'];
        phone = request.POST['phone'];
        message = request.POST['message'];
        realtor_email = request.POST['realtor_email'];
        user_id = request.POST['user_id'];

        if request.user.is_authenticated:
            user_id = request.user.id;
            has_contacted = Contact.objects.filter(listing_id=listing_id, user_id=user_id);
            if has_contacted:
                messages.error(request, "you have already made and enquiry");
                return redirect('/listings/'+listing_id)
                
            

        contact = Contact(listing_id=listing_id, listing=listing, name=name,email=email,
        phone=phone,message=message,user_id=user_id)

        contact.save()

        send_mail(
            'Listing Property',
            message,
            'rashidcollins16@gmail.com',
            [realtor_email, 'rashidcollins16@gmail.com'],
            fail_silently=False,
        )
        messages.success(request, "your message has been submitted, realtor will get back to you");
        return redirect('/listings/'+listing_id)
        return
    else:
        return redirect('listings');

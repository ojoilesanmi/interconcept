from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

def index(request):
    return render(request, 'interconcept/index.html')

def contact(request):
    if request.method == "POST":
        fullname = request.POST['fullname']
        email = request.POST['email']
        message = request.POST['message']

        contact = Contact(fullname=fullname, email=email, message=message)
        contact.save()
        messages.success(request, "Thank you for your message. We will be in touch shortly!")
        return redirect('contact')
    else:
        return render(request, 'interconcept/contact.html')
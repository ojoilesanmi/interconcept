from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'interconcept/index.html')

def contact(request):
    if request.method == "POST":
        fullname = request.POST["fullname"]
        email = request.POST["email"]
        message = request.POST["message"]

        contact = Conntact(fullname=fullname, email=email, message=message)
        contact.save()
        messages.success("Thank you for your message. We will be in touch shortly!")
        return redirect('index')
    else:
        return render(request, 'interconcept/contact.html')
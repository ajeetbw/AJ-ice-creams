from django.shortcuts import render, HttpResponse
from datetime import datetime
from .models import Contact
from django.contrib import messages

def index(request):
    context ={
        "variable":"this is sent",
    }
    return render(request,'index.html', context)
    #return HttpResponse("this is home page")
def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')
 
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        date = datetime.today()
        contact= Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent successfully!')
        # Save the data to the database or perform any other action
        # For example, you can create a Contact object and save it
        # contact = Contact(name=name, email=email, phone=phone, desc=desc, date=date)
        # contact.save()
        def __str__(self):
            return self.name

        print(name, email, phone, desc)
    return render(request,'contact.html')


def cart(request):
    #return render(request,'cart.html')
    return HttpResponse("this is cart page")   

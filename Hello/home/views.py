from django.shortcuts import render
from datetime import  datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    messages.success(request,"Heyy! You should check in on some of those fields below.")

    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your responce has been submitted.....')
    return render(request, "contact.html")


from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import contact
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        'variable1':"jemin is grate",
        'variable2':"jemin is genious"
    }
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")
    #return HttpResponse("this is about page")

def services(request):
    return render(request,"services.html")
    #return HttpResponse("this is services page")

def contact(request):
    if request.method == "post":
        name=request.post.get("name")
        email=request.post.get("email")
        phone=request.post.get("phone")
        contact=contact(name=name,email=email,phone=phone,date=datetime.today())
        contact.save()
        messages.success(request, 'your massage has been sent.')
        
    return render(request,"contact.html")
    #return HttpResponse("this is contact page")





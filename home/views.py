from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return HttpResponse("this is about page")

def services(request):
    return HttpResponse("this is services page")

def contact(request):
    return HttpResponse("this is contact page")





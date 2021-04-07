from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context={
        'variable1':"jemin is grate",
        'variable2':"jemin is genious"
    }
    return render(request,"index.html",context)

def about(request):
    return HttpResponse("this is about page")

def services(request):
    return HttpResponse("this is services page")

def contact(request):
    return HttpResponse("this is contact page")





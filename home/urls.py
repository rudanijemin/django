from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "jemin ice creames Admin"
admin.site.site_title = "jemin ice creames Portal"
admin.site.index_title = "Welcome to jemin ice creames "


urlpatterns = [
    path("",views.index,name="home"),
    path("about",views.about,name="about"),
    path("services",views.services,name="services"),
    path("contact",views.contact,name="contact"),
       
]
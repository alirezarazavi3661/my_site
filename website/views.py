from django.shortcuts import render
from django.http import HttpResponse

def Home_page(request):
    return render(request,'website/home.html')
def About_page(request):
    return render(request,'website/about.html')
def Contact_page(request):
    return render(request,'website/contact.html')

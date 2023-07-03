from django.shortcuts import render
from django.http import HttpResponse

def Home_page(request):
    return HttpResponse('<h1> Home page </h1> ')
def About_page(request):
    return HttpResponse('<h1> About page </h1> ')
def Contact_page(request):
    return HttpResponse('<h1> Contact page </h1> ')

from django.urls import path
from website.views import *

urlpatterns = [
path('',Home_page),
path('About_page',About_page),
path('contact_page',Contact_page),
]



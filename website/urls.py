from django.urls import path
from website.views import *
app_name='website'
urlpatterns = [
path('',Index_page,name='index'),
path('About',About_page,name='about'),
path('contact',Contact_page,name='contact'),
path('elements',elements_page,name='elements')
]



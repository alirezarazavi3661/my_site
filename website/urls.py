from django.urls import path
from website.views import *
from blog.models import Post,Category
from . import views

app_name='website'
urlpatterns = [
path('',Index_page,name='index'),
path('About',About_page,name='about'),
path('contact',Contact_page,name='contact'),
path('elements',elements_page,name='elements'),
path('blog/<int:pid>',blog_single,name='blog_single'),
path('test',test_view,name='test'),
path('newsletter/success',Newsletter, name='newsletter_success'),
path('contact/success',Contact_success, name='contact_success'),

#path('get_success_value',get_success_value,name='get_success_value')




]



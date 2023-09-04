from django.urls import path
from blog.views import *
from blog.models import Post,Category,Comment
from blog.feeds import LatestEntriesFeed
app_name='blog'
urlpatterns = [
path('',blog_home,name='blog_home'),
path('<int:pid>',blog_single,name='blog_single'),
path('author/<str:author_username>',blog_home,name = 'author'),
path('category/<str:cat_name>',blog_home,name = 'category'),
path('search/',blog_search,name='search'),
path('tag/<str:tag_name>',blog_home,name = 'tag'),
path('/rss/feed/', LatestEntriesFeed()),
#path('/post-<str:pid>',test,name = 'test')
]

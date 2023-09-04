from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

#from django.utils.text import slugify

#class Article(models.Model):
#slug = models.SlugField(allow_unicode=True)
class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='blog',default='blog/default.jpg')
    category = models.ManyToManyField(Category)
    tags = TaggableManager()
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null = True)
    counted_views = models.IntegerField(default=0)
    login_require = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    published_date = models.DateField(null=True)
    class Meta:
        ordering = ['-created_date']
    def __str__(self):
        return "{}-{}".format(self.title,self.id)
    def get_absolute_url(self):
        return reverse('blog:blog_single',kwargs={'pid':self.id})    


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField() 
    subject = models.CharField(max_length=255)
    message = models.TextField()
    approved = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    def __str__(self):
        return self.name
    




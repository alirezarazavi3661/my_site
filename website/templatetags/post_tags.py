from django import template
from blog.models import Post,Category

register = template.Library()

@register.simple_tag
def get_latest_posts(count=6):
    posts = Post.objects.filter(status = 1)
    return posts.order_by('-published_date')[:count]
@register.simple_tag
def get_latest_post(count=1):
    posts = Post.objects.filter(status = 1)
    return posts.order_by('-published_date')[:count]
@register.simple_tag
def get_latest_category():
    return Category.objects.all()
@register.simple_tag
def form_captcha():
    return form.captcha()
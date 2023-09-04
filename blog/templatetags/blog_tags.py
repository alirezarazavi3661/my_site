from django import template
from blog.models import Post,Category,Comment
register = template.Library()
@register.filter
def snippet(value,arg=20):
    return value[:20]+'...'
@register.inclusion_tag('blog/blog-popular.html')
def popularposts():
    posts = Post.objects.filter(status=1).order_by('published_date')[:3]
    return {'posts':posts}
@register.inclusion_tag('blog/blog-category.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories':cat_dict} 
@register.simple_tag(name='comments_count')
def function(pid):
    post = Post.objects.get(pk=pid)
    return Comment.objects.filter(post=post.id,approved=True).count()

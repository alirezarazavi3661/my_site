from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect
from blog.models import Post,Category,Comment
from django.utils import timezone
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage,InvalidPage
from blog.forms import CommentForm
from django.contrib import messages
from django.urls import reverse

time_zone_now = timezone.now()
def blog_home(request,**kwargs):
    posts = Post.objects.filter(status = 1)
    
    if kwargs.get('cat_name')!=None:
        posts = posts.filter(category__name = kwargs['cat_name'])
    if kwargs.get('author_username')!=None:
        posts = posts.filter(author__username = kwargs['author_username'])
    if kwargs.get('tag_name')!=None:
        posts = posts.filter(tags__name = kwargs['tag_name'])
    posts = Paginator(posts,3)
    y=posts.num_pages
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except int(page_number)>y:
        posts = posts.get_page(1)
    except int(page_number)<1:
        posts = posts.get_page(1)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)
def blog_single(request,pid):
    #posts = Post.objects.filter(status = 1)
    #post = get_object_or_404(posts,pk=pid)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your comment submited successfully')
        else:
            messages.add_message(request,messages.ERROR,'your comment have not submited successfully')
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(Post,pk=pid,status=1)
    if not post.login_require:
        comments = Comment.objects.filter(post=post.id,approved=True).order_by('created_date')
        form = CommentForm()
        context = {'post':post,'comments':comments,'form':form}
        return render(request,'blog/blog-single.html',context)
    else:
        if request.user.is_authenticated:
            comments = Comment.objects.filter(post=post.id,approved=True).order_by('created_date')
            form = CommentForm()
            context = {'post':post,'comments':comments,'form':form}
            return render(request,'blog/blog-single.html',context)
        else:
            return HttpResponseRedirect(reverse('accounts:login'))
def blog_search(request):
    posts = Post.objects.filter(status = 1)
    if request.method == 'GET':
        posts = posts.filter(content__contains=request.GET.get('s'))
    
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

    
#def blog_category(request,cat_name):
    #posts = Post.objects.filter(status=1)
    #posts = posts.filter(category__name = cat_name)
    #context = {'posts' : posts}
    #return render(request,'blog/blog-home.html',context)

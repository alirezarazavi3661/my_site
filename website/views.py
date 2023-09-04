from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from blog.models import Post,Category
from blog.views import blog_home
from website.forms import NameForm,ContactForm,NewsletterForm
from django.contrib import messages
from django.http import JsonResponse



def Index_page(request):
    return render(request,'website/index.html')
def About_page(request):
    return render(request,'website/about.html')
def Contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your ticket submited successfully')
            return HttpResponseRedirect('/contact')  
        else:
            messages.add_message(request,messages.ERROR,'your ticket didnt submit')
            return HttpResponseRedirect('/contact')  
    form = ContactForm()
    context = {'form':form}
    return render(request,'website/contact.html',context)
def elements_page(request):
    return render(request,'website/elements.html')
def blog_single(request,pid):
    posts = Post.objects.filter(status = 1)
    #post = get_object_or_404(posts,pk=pid)
    post = get_object_or_404(posts,pk=pid,status=1)
    context = {'post':post}
    return render(request,'blog/blog-single.html',context)

def Newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/newsletter/success')  # Redirect to the success page
        else:
            return redirect('/')
            # Handle form errors here
    else:
        form = NewsletterForm()
        
    return render(request, 'success.html', {'form': form})
def Contact_success(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contact/success')  # Redirect to the success page
        else:
            return redirect('/')
            # Handle form errors here
    else:
        form = ContactForm()
        
    return render(request, 'success.html', {'form': form})
  
def test_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('not valid')  
    form = ContactForm()
    context = {'form':form}
    return render(request,'test.html',context)  
    #def get_success_value(request):
        #success = True  # Calculate the actual success value here
        #return JsonResponse({'success': success})

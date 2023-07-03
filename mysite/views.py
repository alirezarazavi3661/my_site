from django.http import HttpResponse
from django.http import JsonResponse

def http_test(request):
    return HttpResponse('<h1> http_test </h1> ')
def json_test(request):
    return JsonResponse({'name':"alireza \n ",'lastname':'razavi','age':"22","birth":"3 july of 2003"
                         ,"nationality":"iranian"})
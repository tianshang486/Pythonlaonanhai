from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def index(request):
    a = {'name':'chao'}
    ret = JsonResponse(a)
    return ret



def base(request):

    return render(request,'base.html')

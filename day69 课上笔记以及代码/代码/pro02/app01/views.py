from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def index(request):
    a = {'name':'chao'}
    ret = JsonResponse(a)
    ret["Access-Control-Allow-Origin"] = "http://127.0.0.1:8000"
    ret["Access-Control-Allow-Headers"] = "content-type"
    return ret



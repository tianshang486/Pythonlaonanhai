from django.shortcuts import render

# Create your views here.

def index(request):
    num = 100
    return render(request,'index.html')


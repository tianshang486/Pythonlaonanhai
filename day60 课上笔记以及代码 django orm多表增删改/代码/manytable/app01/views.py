from django.shortcuts import render,HttpResponse
from app01 import models
# Create your views here.

def query(request):
    #删除

    # 更新

    #一对多
    models.Publish.objects.filter(pk=2).update(
        id=4, # 没有级联更新,报错!!
    )


    return HttpResponse('ok')


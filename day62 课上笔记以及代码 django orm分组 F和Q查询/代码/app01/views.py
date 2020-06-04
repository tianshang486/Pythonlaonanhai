from django.shortcuts import render,HttpResponse
from app01 import models
# Create your views here.
from django.db.models import Avg,Max,Min,Sum,Count,F,Q


def query(request):

    # 1 查询每个作者的姓名以及出版的书的最高价格
    # ret = models.Author.objects.annotate(a=Max('book__price')).values('name','a')
    # print(ret)

    # 2 查询作者id大于2作者的姓名以及出版的书的平均价格
    # ret = models.Author.objects.filter(id__gt=2).annotate(a=Avg('book__price')).values('name','a')
    # print(ret)

    # 3 查询作者id大于2或者作者年龄大于等于20岁的女作者的姓名以及出版的书的最高价格
    # ret = models.Author.objects.filter(Q(id__gt=2)|Q(age__gt=20),sex='female').annotate(a=Max('book__price')).values('name','a')
    # print(ret)

    # 4 查询每个作者出版的书的最高价格 的平均值
    # ret = models.Author.objects.annotate(a=Max('book__price')).values('a').aggregate(b=Avg('a'))
    # print(ret) #{'b': 23.375}


    # 5 每个作者出版的所有书的价格以及最高价格的那本书的名称
    # ret = models.Author.objects.annotate(m=Max('book__price')).values('book__price','book__title')
    # print(ret)
    return HttpResponse('ok')






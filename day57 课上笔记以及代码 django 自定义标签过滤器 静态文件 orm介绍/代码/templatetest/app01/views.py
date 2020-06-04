from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def index(request):
    num = 100
    name = 'shige'
    name_list = ['大壮','小壮','壮壮','中壮']
    d1 = {'name':'大壮','age':73,'hobby':'xuefei+xiangxi'}
    xx = 'oo'
    class Animal:
        def __init__(self):
            self.kind = 'dog'
        def eat(self):
            return 'shi'
    a = Animal()
    print(locals())
    # return render(request,'index.html',{'num':num,'name':name,'namelist':name_list,'d1':d1,'a':a})
    movesize = 123123124

    import datetime

    now = datetime.datetime.now()

    words = 'i love you my boy'
    # words = '我 爱 你 我的 基友'

    tag = '<a href="http://www.baidu.com">百度</a>'

    return render(request,'index.html',locals())


def tags(request):
    num = 11
    name_list = ['大壮', '小壮', '壮壮', '中壮']
    d1 = {'name': '大壮', 'age': 73, 'hobby': ['xuefei','bge','xiangxi']}

    d2 = [[11,22],[33,44]]
    d4 = {'items':'xx'}
    d3 = [11,22,33,44]

    return render(request,'tags.html',locals())


def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        print(request.POST)

        return HttpResponse('登录成功!!!!')

# def login2(request):
#     print(request.POST)
#     return HttpResponse('登录成功')



def base(request):

    return render(request,'base.html')

def menu1(request):
    return render(request,'menu1.html')
def menu2(request):
    return render(request,'menu2.html')
def menu3(request):
    return render(request,'menu3.html')


def nav(request):
    return render(request,'nav.html')

def newpro(request):
    return render(request,'newpro.html')



def xxoo(request):
    s1 = '李帅和家宝'
    l1 = [11,22,33,44,55]
    return render(request,'xxoo.html',{'s1':s1,'l1':l1})












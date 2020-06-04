from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from django.http import JsonResponse
from ajaxtest import settings
# from django.conf import settings

# Create your views here.

class LoginView(View):

    def get(self,request):

        return render(request,'login.html')

    def post(self,request):
        # name = request.POST.get('username')
        # pwd = request.POST.get('password')

        if 'content-type' == 'application/x-www-form-urlencoded;':

            #uname=123&pwd=123&csrfmiddlewaretoken=niTpR87FOcd80HaMIaxEoYRHHLn2S8DMuxyPU27WqNVf0LaNYdsoAbke6SQh2kSG
            '''
            <QueryDict: {'uname': ['123'], 'pwd': ['123'], 'csrfmiddlewaretoken': ['niTpR87FOcd80HaMIaxEoYRHHLn2S8DMuxyPU27WqNVf0LaNYdsoAbke6SQh2kSG']}>'''

        print(request.POST)
        name = request.POST.get('uname')
        pwd = request.POST.get('pwd')

        if name == 'bge' and pwd == '213':
            # return render(request,'index.html')
            # d1 = {"aa":0,"bb":"/index/"}
            d1 = {"aa":0,"bb":"/index/"}


            # ret = '{"aa":0,"bb":"/index/"}'
            # import json
            # d1_json = json.dumps(d1)
            #conn.send('HTTP/1.1 200 ok\r\n\r\nasdf')
            # return HttpResponse(ret)
            # return HttpResponse(d1_json,content_type='application/json')
            return JsonResponse(d1)
            # return HttpResponse(d1_json)

        else:
            ret = '{"aa":3,"bb":"用户名或者密码错误!!!"}'
            return HttpResponse(ret)


def index(request):

    return render(request,'index.html')

def home(request):


    return render(request,'home.html')


def data(request):
    l1 = [11,22,33]
    # ret = request.GET.get('k1')  #None
    # print(request.get_full_path())
    print(request.POST) #<QueryDict: {}>
    print(request.body) #b'{"k1":"v1","k2":"v2"}'


    # print(ret)
    return JsonResponse(l1,safe=False)

def upload(request):
    if request.method == 'GET':

        return render(request,'upload.html')
    else:
        print(request.POST)   #拿到的是post请求的数据,但是文件相关数据需要用request.FILES去拿
        print(request.FILES)  #<MultiValueDict: {'head-pic': [<InMemoryUploadedFile: 1.png (image/png)>]}>
        
        file_obj = request.FILES.get('head_pic')
        print(file_obj)
        file_name = file_obj.name

        # f = open('xx.txt','rb')
        # with open('xx.txt','wb') as f2:
        #     for i in f:
        #         f2.write(i)
        import os
        path = os.path.join(settings.BASE_DIR,'statics','img',file_name)


        with open(path,'wb') as f:
            # for i in file_obj:
            #     f.write(i)
            for chunk in  file_obj.chunks():
                f.write(chunk)


        return HttpResponse('ok')




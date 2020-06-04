from django.shortcuts import render,HttpResponse,redirect
from django.views import View

# Create your views here.

class LoginView(View):

    def get(self,request):

        return render(request,'login.html')

    def post(self,request):
        # name = request.POST.get('username')
        # pwd = request.POST.get('password')
        name = request.POST.get('uname')
        pwd = request.POST.get('pwd')

        if name == 'bge' and pwd == '213':
            # return render(request,'index.html')
            d1 = {"aa":0,"bb":"/index/"}

            # ret = '{"aa":0,"bb":"/index/"}'
            import json
            d1_json = json.dumps(d1)

            # return HttpResponse(ret)
            return HttpResponse(d1_json)

        else:
            ret = '{"aa":3,"bb":"用户名或者密码错误!!!"}'


            return HttpResponse(ret)


def index(request):

    return render(request,'index.html')
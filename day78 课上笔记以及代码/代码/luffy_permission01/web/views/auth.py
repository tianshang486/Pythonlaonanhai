from rbac import models
from django.shortcuts import (
    HttpResponse,render,redirect
)
from django.conf import settings
from rbac.serve.permissions import init_permission

def login(request):

    if request.method == 'GET':
        return render(request,'login.html')
    else:
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        user_obj = models.Userinfo.objects.filter(name=uname,password=pwd).first()
        if user_obj:

            # 使用rbac组件中的session权限注入功能
            init_permission(request,user_obj)
            return redirect('index')
#permission_list <QuerySet [{'permissions__url': '/customer/list/'}, {'permissions__url': '/customer/add/'}, {'permissions__url': '/customer/edit/(?P<cid>\\d+)/'}, {'permissions__url': '/customer/list/'}, {'permissions__url': '/payment/list/'}, {'permissions__url': '/payment/add/'}, {'permissions__url': '/payment/edit/(?P<pid>\\d+)/'}]>
        else:
            return redirect('login')

# 首页
def index(request):

    return render(request,'index.html')



from rbac import models
from django.shortcuts import (
    HttpResponse,render,redirect
)

def login(request):

    if request.method == 'GET':
        return render(request,'login.html')
    else:
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        user_obj = models.Userinfo.objects.filter(name=uname,password=pwd).first()
        if user_obj:
            request.session['is_login'] = True  # 用来记录是否登录了
            # 登录成功，将权限信息注入到session中

            permission_list = user_obj.roles.values('permissions__url','permissions__title').distinct()
            request.session['permission_list'] = list(permission_list)
            print('permission_list',permission_list)
            return redirect('index')
#permission_list <QuerySet [{'permissions__url': '/customer/list/'}, {'permissions__url': '/customer/add/'}, {'permissions__url': '/customer/edit/(?P<cid>\\d+)/'}, {'permissions__url': '/customer/list/'}, {'permissions__url': '/payment/list/'}, {'permissions__url': '/payment/add/'}, {'permissions__url': '/payment/edit/(?P<pid>\\d+)/'}]>
        else:
            return redirect('login')

# 首页
def index(request):

    return render(request,'index.html')



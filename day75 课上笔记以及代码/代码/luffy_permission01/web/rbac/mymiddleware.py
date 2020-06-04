import re

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,redirect,render
from django.urls import reverse


class PermissionAuth(MiddlewareMixin):

    def process_request(self,request):

        # 登录认证白名单
        white_list = [reverse('login'),]
        request_path = request.path
        if request_path in white_list:
            return
        # 登录认证
        is_login = request.session.get('is_login',None)
        if not is_login:
            return redirect('login')

        # 权限认证白名单
        permisson_white_list = [reverse('index'),]
        if request_path in permisson_white_list:
            return
        # 权限认证
        permission_list = request.session.get('permission_list')

        # [{'permission_url':'/customer/list/',},{'permission_url':'/customer/edit/(\d+)/',}]
        # /customer/edit/3/
        for reg in permission_list:
            reg = r"^%s$"%reg['permissions__url']
            if re.match(reg,request_path):
                return
        else:
            return HttpResponse('您不配！！！')

        # if request_path in permission_list:
        #     return
        # else:
        #     return HttpResponse('您不配！！！')



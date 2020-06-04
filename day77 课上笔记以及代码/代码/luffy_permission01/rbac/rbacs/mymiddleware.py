import re

from rbac import models

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,redirect,render
from django.urls import reverse


class PermissionAuth(MiddlewareMixin):

    def process_request(self,request):
        request_path = request.path
        request.current_id = None  #记录当前访问url权限对应的二级菜单权限的id值

        request.bread_crumbs = [
            {'url':reverse('index'),'title':'首页'},

        ]
        # 登录认证白名单
        white_list = [reverse('login'),'/admin/*']
        for i in white_list:

            ret = re.match(i,request_path)
            if ret:
                return

        # request_path = request.path
        # if request_path in white_list:
        #     return
        # 登录认证
        is_login = request.session.get('is_login',None)
        if not is_login:
            return redirect('login')

        # 权限认证白名单
        permisson_white_list = [reverse('index'),]
        if request_path in permisson_white_list:
            return
        # 权限认证
        permission_dict = request.session.get('permissions')

        # [{'permission_url':'/customer/list/',},{'permission_url':'/customer/edit/(\d+)/',}]
        # /customer/edit/3/
        # print(permission_list)
        for reg_dict in permission_dict.values():
            reg2 = r"^%s$"%reg_dict['permissions__url']
            if re.match(reg2,request_path):
                # 记录当前访问路径的parent_id
                pid = reg_dict.get('permissions__parent_id')
                if pid:
                    request.current_id = pid

                    # ret = models.Permission.objects.filter(pk=pid).first()
                    request.bread_crumbs.append({
                        'url': permission_dict[str(pid)]['permissions__url'],
                        'title': permission_dict[str(pid)]['permissions__title'],
                    })
                    request.bread_crumbs.append({
                        'url': None,
                        'title': reg_dict['permissions__title']
                    })
                else:
                    # 这是添加二级菜单的面包屑数据
                    request.bread_crumbs.append({
                        'url':None,
                        'title':reg_dict['permissions__title']
                    })
                    request.current_id = reg_dict.get('permissions__pk')

                # request.parent = parent
                return
        else:
            return HttpResponse('您不配！！！')

        # if request_path in permission_list:
        #     return
        # else:
        #     return HttpResponse('您不配！！！')



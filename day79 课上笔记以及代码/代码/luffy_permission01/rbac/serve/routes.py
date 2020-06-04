from django.conf import settings
from django.utils.module_loading import import_string
from django.urls import RegexURLResolver, RegexURLPattern
from collections import OrderedDict



def recursion_urls(pre_namespace, pre_url, urlpatterns, url_ordered_dict):
    #None, "/", urlpatterns, url_ordered_dict

    # 递归第二层
    #'rbac', "/", rbac.urls.urlpatterns, url_ordered_dict
    """
           [

               url(r'^', include('web.urls')),--RegexURLResolver
               url(r'^rbac/', include('rbac.urls',namespace='rbac')), -- RegexURLResolver
               url(r'^xx', auth.xx,name='xx') -- RegexURLPattern
           ]

    """
    for item in urlpatterns: #w eb.urls.urlpatterns
        '''
            [
                 # url(r'^login/$', auth.login,name='login'), -- RegexURLPattern 
                 url(r'^role/list/', views.role_list,name='role_list'),

            ]
        '''
        if isinstance(item, RegexURLResolver):
            if pre_namespace:
                if item.namespace:
                    namespace = "%s:%s" % (pre_namespace, item.namespace,) #'rbac':'rbac'
                else:
                    namespace = pre_namespace # 'rbac'
            else:
                if item.namespace: #'rbac'
                    namespace = item.namespace #'rbac'
                else:
                    namespace = None
            # None, "/^", urlpatterns, url_ordered_dict
            recursion_urls(namespace, pre_url + item.regex.pattern, item.url_patterns, url_ordered_dict)
            #'/'+'^'--'/^',
        else:

            if pre_namespace: #None
                name = "%s:%s" % (pre_namespace, item.name,)
            else:
                name = item.name #name = 'login'
            if not item.name:
                raise Exception('URL路由中必须设置name属性')

            url = pre_url + item._regex #'^login/$'--  #/^^login/$
            url_ordered_dict[name] = {'url_name': name, 'url': url.replace('^', '').replace('$', '')} #
            #url_ordered_dict['login'] = {'name': 'login', 'url': url.replace('^', '').replace('$', '')} #/login/

def get_all_url_dict(ignore_namespace_list=None):
    """
    获取路由中
    :return:
    """
    ignore_list = ignore_namespace_list or []
    #ignore_list -- ['admin', ]

    #存放项目所有 url路由用的有序字典
    url_ordered_dict = OrderedDict()

    md = import_string(settings.ROOT_URLCONF)

    urlpatterns = []
    # urlpatterns = [
    #     url(r'^', include('web.urls')),
    #     url(r'^rbac/', include('rbac.urls', namespace='rbac')),
    # ]

    print(md.urlpatterns)
    for item in md.urlpatterns:
        """
        [
            
            url(r'^', include('web.urls')),--RegexURLResolver
            url(r'^rbac/', include('rbac.urls',namespace='rbac')), -- RegexURLResolver
            url(r'^xx', auth.xx,name='xx') -- RegexURLPattern
        ]
        
        """
        # [RegexURLResolver,RegexURLResolver,RegexURLPattern]
        if isinstance(item, RegexURLResolver) and item.namespace in ignore_list:
            continue
        urlpatterns.append(item)
    recursion_urls(None, "/", urlpatterns, url_ordered_dict)
    print('>>>>',url_ordered_dict)
    return url_ordered_dict

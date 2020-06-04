from django.urls import reverse
from django import template
# from django.
from django.http.request import QueryDict

register = template.Library()
@register.simple_tag
def reverse_url(request):
    print(type(request.GET))  #<class 'django.http.request.QueryDict'>
    if request.path == reverse('customers'):
        return '公户信息'
    else:
        return '我的客户信息'

@register.simple_tag
def resole_url(request,url_name,customer_pk):
    # 编辑保存之后跳转回的路径
    next_url = request.get_full_path()  #/customers/?page=3
    #
    reverse_url = reverse(url_name,args=(customer_pk,))  #/edit_customer/1/
    #edit_customer/1/?next=/customers/?page=3
    q = QueryDict(mutable=True)
    q['next'] = next_url  #queryDict({'next':'/customers/?page=3&kw=111'})
    # full_url = rever_url + '?next=' + next_url
    next_url = q.urlencode()  #next=/customers/%3Fpage%3D%26kw%3D111

    # request.GET['next'] = "/customers/?page=3" #/customers/?page=3&kw=111
    # request.GET['page'] = 3
    # request.GET['kw'] = 111
    # full_url = /edit_customer/1/ ?next=%2Fcustomers%2F%3Fpage%3D%26kw%3D111
    #            /edit_customer/217/?next=%2Fcustomers%2F%3Fpage%3D3
   #             /edit_customer/90/?next=%2Fcustomers%2F%3Fsearch_field%3Dqq__contains%26kw%3D111
    full_url = reverse_url + '?' + next_url
    print(full_url)

    return full_url




















import re
import hashlib

from django.shortcuts import (
    render,HttpResponse,redirect
)
from django.urls import reverse
from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.views import View

from sales import models
from sales.utils.hashlib_func import set_md5
from sales.utils.page import MyPagenation
# Create your views here.
#登录
def login(request):

    if request.method == 'GET':
        return render(request,'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = models.UserInfo.objects.filter(username=username,password=set_md5(password)).first()
        if user_obj:

            #将用户信息保存到session中
            request.session['user_id'] = user_obj.id

            return redirect('customers')
        else:
            # return redirect('login')
            return render(request,'login.html',{'error':'用户名或者密码错误'})


def mobile_validate(value):
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')  #自定义验证规则的时候，如果不符合你的规则，需要自己发起错误


class RegisterForm(forms.Form):
    username = forms.CharField(
        max_length=16,
        min_length=6,
        label='用户名',
        widget=forms.widgets.TextInput(attrs={'class':'username','autocomplete':'off','placeholder': '用户名'}),
        error_messages={
            'required':'用户名不能为空',
            'max_length':'用户名不能大于16位',
            'min_length':'用户名不能小于6位',
        }

    )
    #placeholder="输入密码" oncontextmenu="return false"
             #onpaste="return false"
    password = forms.CharField(
        max_length=32,
        min_length=6,
        label='密码',
        widget=forms.widgets.PasswordInput(attrs={'class': 'password', 'placeholder': '输入密码', 'oncontextmenu': 'return false', 'onpaste': 'return false'}),

        error_messages={
            'required': '密码不能为空',
            'max_length': '密码不能大于32位',
            'min_length': '密码不能小于6位',
        }
    )
    r_password = forms.CharField(
        label='确认密码',
        widget=forms.widgets.PasswordInput(attrs={'class': 'password', 'placeholder': '请再次输入密码', 'oncontextmenu': 'return false', 'onpaste': 'return false'}),
        error_messages={
            'required': '确认密码不能为空',
        }
    )
    telephone = forms.CharField(
        label='手机号',
        error_messages={
            'required': '手机不能为空',
        },
        validators=[mobile_validate, ],
        widget=forms.widgets.TextInput(
            attrs={'class': 'phone_number', 'placeholder': '输入手机号码', 'autocomplete': 'off', 'id': 'number'}),
    )

    email = forms.EmailField(
        label='邮箱',
        error_messages={
            'required': '邮箱不能为空',
            'invalid':'邮箱格式不对',
        },
        widget=forms.widgets.TextInput(attrs={'class': 'email', 'placeholder': '输入邮箱地址', 'oncontextmenu': 'return false', 'type': 'email'}),
        # validators=[]
    )


    def clean(self):
        values = self.cleaned_data
        password = values.get('password')
        r_password = values.get('r_password')

        if password == r_password:
            return values
        else:
            self.add_error('r_password','两次输入的密码不一致！')


# 注册功能


def register(request):
    """
    注册功能
    :param request:
    :return:
    """
    if request.method == 'GET':
        register_form_obj = RegisterForm()
        return render(request,'register.html',{'register_form_obj':register_form_obj})

    else:
        register_form_obj = RegisterForm(request.POST)
        #基于form的数据校验
        if register_form_obj.is_valid():
            print(register_form_obj.cleaned_data)
            register_form_obj.cleaned_data.pop('r_password')
            password = register_form_obj.cleaned_data.pop('password')

            # 对密码进行加密
            password = set_md5(password)
            register_form_obj.cleaned_data.update({'password':password})
            models.UserInfo.objects.create(
                **register_form_obj.cleaned_data
            )
            return redirect('login')
        else:
            return render(request,'register.html',{'register_form_obj':register_form_obj})


def home(request):

    return render(request,'saleshtml/home.html')


class CutomerView(View):

    def get(self,request):
        # 当前页  例如 1
        current_request_path = request.path #/customers/?page=3  -- /customers/
        # 公户
        if current_request_path == reverse('customers'):
            tag = '1'
            customer_list = models.Customer.objects.filter(consultant__isnull=True)
        else:
            tag = '2'
            # 私户请求,查询所有的私户
            user_obj = request.user_obj
            customer_list = models.Customer.objects.filter(consultant=user_obj)

        get_data = request.GET.copy()  # 将request.GET对象改成可修改的
        page_num = request.GET.get('page')  # 当前页码
        search_field = request.GET.get('search_field')  # 选择查询的字段,name
        kw = request.GET.get('kw')  # 查询关键字  #思宇

        if kw:
            kw = kw.strip()
            q_obj = Q()
            q_obj.children.append((search_field, kw))
            # q_obj.children.append(Q(qq_contains='111'))
            customer_list = customer_list.filter(q_obj)

        else:
            customer_list = customer_list
        base_url = request.path  # 访问的路径

        customer_count = customer_list.count()

        per_page_num = settings.PER_PAGE_NUM  # 每页显示多少条数据
        page_num_show = settings.PAGE_NUM_SHOW  # 显示的页码数

        page_obj = MyPagenation(page_num, customer_count, base_url, get_data, per_page_num, page_num_show, )

        page_html = page_obj.page_hmtl()

        customer_objs = customer_list.reverse()[page_obj.start_data_num:page_obj.end_data_num]
        return render(request, 'saleshtml/customers.html', {'customer_objs': customer_objs, 'page_html': page_html,'tag':tag})


    def post(self,request):
        action = request.POST.get('action')
        cids = request.POST.getlist('cids')
        if hasattr(self,action):
            customers = models.Customer.objects.filter(pk__in=cids)
            print(customers)
            getattr(self,action)(request,customers)
            return redirect(request.path)
    #公转私
    def reverse_gs(self,request,customers):
        customers.update(consultant_id=request.session.get('user_id'))

    #私转公
    def reverse_sg(self,request,customers):
        customers.update(consultant=None)

# def customers(request):
#     #当前页  例如 1
#     current_request_path = request.path
#     # 公户
#     if current_request_path == reverse('customers'):
#         customer_list = models.Customer.objects.filter(consultant__isnull=True)
#     else:
#         # 私户请求,查询所有的私户
#         user_obj = models.UserInfo.objects.get(id=request.session.get('user_id'))
#         customer_list = models.Customer.objects.filter(consultant=user_obj)
#
#     get_data = request.GET.copy()  #将request.GET对象改成可修改的
#     page_num = request.GET.get('page') #当前页码
#     search_field = request.GET.get('search_field')  #选择查询的字段,name
#     kw = request.GET.get('kw')  #查询关键字  #思宇
#
#     if kw:
#         kw = kw.strip()
#         q_obj = Q()
#         q_obj.children.append((search_field, kw))
#         #q_obj.children.append(Q(qq_contains='111'))
#         customer_list = customer_list.filter(q_obj)
#
#     else:
#         customer_list = customer_list
#     base_url = request.path  #访问的路径
#
#     customer_count = customer_list.count()
#
#     per_page_num = settings.PER_PAGE_NUM  #每页显示多少条数据
#     page_num_show = settings.PAGE_NUM_SHOW  #显示的页码数
#
#     page_obj = MyPagenation(page_num,customer_count,base_url,get_data,per_page_num,page_num_show,)
#
#     page_html = page_obj.page_hmtl()
#
#     customer_objs = customer_list.reverse()[page_obj.start_data_num:page_obj.end_data_num]
#     return render(request,'saleshtml/customers.html',{'customer_objs':customer_objs,'page_html':page_html})


# def mycustomers(request):
#     models.Customer.objects.filter(consultant=models.UserInfo.objects.get(id=request.session.get('user_id')))


class CustomerForm(forms.ModelForm):

    class Meta:
        model = models.Customer
        fields = '__all__'
        error_messages = {
            'qq': {'required': '不能为空'},
            'course': {'required': '不能为空'},

        }

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        from multiselectfield.forms.fields import MultiSelectFormField
        from django.forms.fields import DateField
        for field_name,field in self.fields.items():
            print(type(field))
            if not isinstance(field,MultiSelectFormField):
                field.widget.attrs.update({'class':'form-control'})

            # if isinstance(field,DateField):
            #     field.widget.attrs.update({'type': 'date'})
            # else:
            #     field.widget.attrs.update({'type': 'form-control'})


# def add_customer(request):
#     """
#     添加客户
#     :param request:
#     :return:
#     """
#     if request.method == 'GET':
#         customer_form = CustomerForm()
#         return render(request,'saleshtml/add_customer.html',{'customer_form':customer_form})
#
#     else:
#         customer_form = CustomerForm(request.POST)
#         if customer_form.is_valid():
#             customer_form.save()
#             return redirect('customers')
#         else:
#             return render(request, 'saleshtml/add_customer.html', {'customer_form': customer_form})
#
# def edit_customer(request,cid):
#     """
#     编辑客户
#     :param request:
#     :param cid:   客户记录id
#     :return:
#     """
#     customer_obj = models.Customer.objects.filter(pk=cid).first()
#     if request.method == 'GET':
#         customer_form = CustomerForm(instance=customer_obj)
#         return render(request,'saleshtml/edit_customer.html',{'customer_form':customer_form})
#
#     else:
#         customer_form = CustomerForm(request.POST,instance=customer_obj)
#         if customer_form.is_valid():
#             customer_form.save()
#             return redirect('customers')
#         else:
#             return render(request,'saleshtml/edit_customer.html',{'customer_form':customer_form})


#添加客户和编辑客户

def add_edit_customer(request,cid=None):
    """
    添加客户和编辑客户
    :param request:
    :param cid:   客户记录id
    :return:
    """
    label = '编辑客户' if cid else '添加客户'
    customer_obj = models.Customer.objects.filter(pk=cid).first()
    if request.method == 'GET':
        customer_form = CustomerForm(instance=customer_obj)
        return render(request,'saleshtml/edit_customer.html',{'customer_form':customer_form,'label':label})

    else:
        #http://127.0.0.1:8000/edit_customer/80/?next=/customers/?search_field=qq__contains&kw=111&page=2
        print('>>>>>',request.GET.get('next'))  #/customers/?page=3
        next_url = request.GET.get('next') #"/customers/?page=3"
        #>>>>> /customers/?search_field=qq__contains&kw=111
        customer_form = CustomerForm(request.POST,instance=customer_obj)
        if customer_form.is_valid():
            customer_form.save()

            return redirect('/customers/?search_field=qq__contains&kw=111')
        else:
            return render(request,'saleshtml/edit_customer.html',{'customer_form':customer_form,'label':label})

















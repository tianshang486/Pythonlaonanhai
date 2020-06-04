import re

from django.shortcuts import render,HttpResponse,redirect
from django.core.exceptions import ValidationError
from django import forms
# Create your views here.
from app01 import models

def mobile_validate(value):
    mobile_re = re.compile(r'^13[0-9]{9}')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')  #自定义验证规则的时候，如果不符合你的规则，需要自己发起错误

from django.core.validators import RegexValidator
class LoginForm(forms.Form):
    name = forms.CharField(
        required=True,
        min_length=6,
        label='用户名',
        initial='高杰DSB',
        # validators=[RegexValidator(r'^金瓶梅','没看过金瓶梅，不能通过'),RegexValidator(r'红旭妹妹$','没看过红旭妹妹，不能通过'),],
        # validators=[mobile_validate,],
        help_text='这是输入用户名的地方，不能太短！',
        error_messages={'required':'不能为空！','min_length':'太短了！'},
        # widget=forms.widgets.TextInput(attrs={'class':'form-control'}),
        widget=forms.widgets.TextInput,
    )

    password = forms.CharField(
        min_length=8,
        max_length=10,
        label='密码',
        widget=forms.widgets.PasswordInput(),
    )
    r_password = forms.CharField(
        min_length=8,
        max_length=10,
        label='确认密码',
        widget=forms.widgets.PasswordInput(),
    )

    #局部钩子  clean_字段名称
    def clean_name(self):
        value = self.cleaned_data['name']
        if '大壮' in value:
            raise ValidationError('含有敏感词汇：大壮')
        else:
            return value



    #全局钩子
    def clean(self):
        value = self.cleaned_data

        p1 = value['password']
        p2 = value['r_password']
        if p1 == p2:
            return value
        else:
            # raise ValidationError('两次输入的密码不一致！')
            self.add_error('r_password','两次输入的密码不一致！')
            raise ValidationError('两次输入的密码不一致！')
    # sex = forms.ChoiceField(
    #     label='性别',
    #     initial=3,
    #     choices=((1, "男"), (2, "女"), (3, "保密")),
    #     widget=forms.widgets.RadioSelect(),
    #
    # )
    # #
    # city = forms.ChoiceField(
    #     label='性别',
    #     initial=3,
    #     choices=((1, "北京"), (2, "上海"), (3, "东莞")),
    #     widget=forms.widgets.Select(),
    #
    # )
    # hobby = forms.MultipleChoiceField(
    #     label='爱好',
    #
    #     choices=((1, "抽烟"), (2, "喝酒"), (3, "烫头")),
    #     widget=forms.widgets.CheckboxSelectMultiple,
    #
    # )
    # girls = forms.MultipleChoiceField(
    #     label='爱好',
    #
    #     choices=((1, "红旭妹妹"), (2, "相玺哥哥"), (3, "程根姐姐")),
    #     widget=forms.widgets.SelectMultiple,
    #
    # )
    # #
    # status = forms.ChoiceField(
    #     label='remeber me!!',
    #
    #     choices=(('True', "红旭妹妹"), ('False', "相玺哥哥")),
    #     widget=forms.widgets.CheckboxInput,
    #
    # )
    # #
    # # brithday = forms.CharField(
    # #     widget=forms.widgets.TextInput(attrs={'type':'date'})
    # # )



def register(request):
    form_obj = LoginForm()
    if request.method == 'GET':
        return render(request,'register.html',{'form_obj':form_obj})

    else:
        # request.POST = name:'asdfasdf'
            form_obj = LoginForm(request.POST)
            print(form_obj.fields)
            print(form_obj.is_valid())
            if form_obj.is_valid():
                print(form_obj.cleaned_data) #{'name': '13812312312', 'password': '11111111'}
                return HttpResponse('登录成功')
            else:

                print('xxxxxx')
                print(form_obj.errors)
                return render(request,'register.html',{'form_obj':form_obj})


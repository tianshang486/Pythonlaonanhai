# 昨日内容回顾

## 中间件

自定义中间件

~~~
应用下创建一个文件夹，文件夹下面创建一个xx.py文件
from django.utils.deprecation import MiddlewareMixin
class MD1(MiddlewareMixin):

	def process_request(self,request):
		
		return None
    def process_response(self,request,response)
		
		return response


~~~



白名单

```
from django.urls import reverse
from django.shortcuts import (
    redirect,HttpResponse,render
)

from django.utils.deprecation import MiddlewareMixin

class SessionAuth(MiddlewareMixin):
    
    def process_request(self,request):
        pass
        #白名单
        # print(request.path)
        white_list = [reverse('login'),'/index/']
        if request.path in white_list:
            
            return None
        
        is_login = request.session.get('is_login')

        if is_login == True:

            return None
        else:
            return redirect('login')
```



# 今日内容

中间件的五个方法

~~~
process_request(self,request)
process_view(self, request, view_func, view_args, view_kwargs)
process_template_response(self,request,response)
process_exception(self, request, exception)
process_response(self, request, response)

~~~

process_view:

![img](https://images2018.cnblogs.com/blog/877318/201805/877318-20180523150722556-373788290.png)



process_exception:视图函数出错，会执行

![img](https://images2018.cnblogs.com/blog/877318/201805/877318-20180523152523125-1475347796.png)



process_template_response：

~~~
def index(request):
    print("app01 中的 index视图")
　　#raise ValueError('出错啦') 
    def render():
        print("in index/render")  
        #raise ValueError('出错啦') #至于render函数中报错了，那么会先执行process_template_response方法，然后执行process_exception方法，如果是在render方法外面报错了，那么就不会执行这个process_template_response方法了。
        return HttpResponse("O98K") #返回的将是这个新的对象
    rep = HttpResponse("OK")
    rep.render = render
    return rep

~~~



## form组件

1 生成页面HTML标签

2 校验用户提交的数据合法性

3 保留用户输入的数据



### 生成标签

~~~

from django import forms

def mobile_validate(value):  value是要被校验的数据
    mobile_re = re.compile(r'^13[0-9]{9}')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')  #别忘了raise错误


class MyForm(forms.Form):
     name = forms.CharField(
        required=True,  #默认等于True，内容不能为空
        min_length=6,   #最小长度为6
        label='用户名',  #标识
        initial='高杰DSB', #初始值，默认值
        # validators=[RegexValidator(r'^金瓶梅','没看过金瓶梅，不能通过'),RegexValidator(r'红旭妹妹$','没看过红旭妹妹，不能通过'),], #写自定义校验规则，RegexValidator（正则，错误信息）
        # validators=[mobile_validate,], #写自定义校验规则，RegexValidator（函数名称，）
        help_text='这是输入用户名的地方，不能太短！',
        error_messages={'required':'不能为空！','min_length':'太短了！'},
        # widget=forms.widgets.TextInput(attrs={'class':'form-control'}),
        widget=forms.widgets.TextInput,
    )
	password = forms.CharField(
        min_length=8,
        max_length=10,  #最大长度不能超过10位
        label='密码',
        widget=forms.widgets.PasswordInput(), #密文输入
    )
    
radio单选框：
 	sex = forms.ChoiceField(
        label='性别',
        initial=3, #初始值
        choices=((1, "男"), (2, "女"), (3, "保密")),
        widget=forms.widgets.RadioSelect(),

    )
select下拉单选框
	city = forms.ChoiceField(
        label='性别',
        initial=3,
        choices=((1, "北京"), (2, "上海"), (3, "东莞")),
        widget=forms.widgets.Select(),

    )

checkbox多选框
	hobby = forms.MultipleChoiceField(
        label='爱好',

        choices=((1, "抽烟"), (2, "喝酒"), (3, "烫头")),
        widget=forms.widgets.CheckboxSelectMultiple,

    )
    
select下拉多选框
    girls = forms.MultipleChoiceField(
        label='爱好',

        choices=((1, "红旭妹妹"), (2, "相玺哥哥"), (3, "程根姐姐")),
        widget=forms.widgets.SelectMultiple,

    )

单选checkbox
	status = forms.ChoiceField(
        label='remeber me!!',

        choices=(('True', "红旭妹妹"), ('False', "相玺哥哥")),
        widget=forms.widgets.CheckboxInput,

    )

#给标签加属性
widget=forms.widgets.TextInput(attrs={'class':'c1','type':'date'}),
    

~~~

### 校验内容

~~~

def register(request):
    form_obj = LoginForm()
    if request.method == 'GET':
        return render(request,'register.html',{'form_obj':form_obj})
	
    else:
        # request.POST = name:'asdfasdf'
            form_obj = LoginForm(request.POST) {‘name’:}
            print(form_obj.fields) #拿到所有的form类中的字段
            print(form_obj.is_valid())
            if form_obj.is_valid(): #校验数据 ，全部通过校验，返回True，但凡有一个不对的，就返回False
                print(form_obj.cleaned_data)  #{'name': '13812312312', 'password': '11111111'}
                return HttpResponse('登录成功')
            else:

                print('xxxxxx')
                print(form_obj.errors)
                return render(request,'register.html',{'form_obj':form_obj})


~~~

html文件写法

~~~

{% load static %}
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- 上述3个meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->
  <title>Bootstrap 101 Template</title>
  <!-- Bootstrap -->
  <link href="{% static 'bootstrap-3.3.7-dist/css/bootstrap.min.css' %}" rel="stylesheet">
</head>
<body>
<h1>你好，世界！</h1>

<form action="" method="post" novalidate>
  {% csrf_token %}
{#  {{ form_obj.errors }}#}
{#  用户名： <input type="text" name="username"> #}
{#  密码： <input type="text" name="password"> #}
  <div>
    <label for="">{{ form_obj.name.label }}</label>
    {{ form_obj.name }}
    {{ form_obj.name.help_text }}
{#    {{ form_obj.errors }}#}
    <span style="color: red;font-size: 14px;">{{ form_obj.name.errors.0 }}</span>
  </div>
  <div>
    <label for="">{{ form_obj.password.label }}</label>
    {{ form_obj.password }}
    {{ form_obj.password.errors.0 }}
{#    {{ form_obj.errors }}#}
  </div>
  <div>
    <label for="">{{ form_obj.r_password.label }}</label>
    {{ form_obj.r_password }}
    {{ form_obj.r_password.errors.0 }}
{#    {{ form_obj.errors }}#}
  </div>
{#  <div>#}
{#    <label for="">{{ form_obj.password.label }}</label>#}
{#    {{ form_obj.password }}#}
{#  </div>#}
{#  <div>#}
{#    <label for="">{{ form_obj.sex.label }}</label>#}
{#    {{ form_obj.sex }}#}
{#  </div>#}
{#  <div>#}
{#    <label for="">{{ form_obj.city.label }}</label>#}
{#    {{ form_obj.city }}#}
{#  </div>#}
{#  <div>#}
{#    <label for="">{{ form_obj.hobby.label }}</label>#}
{#    {{ form_obj.hobby }}#}
{#  </div>#}
{#  <div>#}
{#    <label for="">{{ form_obj.girls.label }}</label>#}
{#    {{ form_obj.girls }}#}
{#  </div>#}
{#  <div>#}
{#    <label for="">{{ form_obj.status.label }}</label>#}
{#    {{ form_obj.status }}#}
{#  </div>#}

  <div>
    <label for="">{{ form_obj.brithday.label }}</label>
    {{ form_obj.brithday }}
  </div>

{#  {{ form_obj.as_p }}#}

  <input type="submit">
</form>


</body>
</html>

~~~



### 局部钩子和全局钩子

~~~
在定义的form类中写下面的方法：
#局部钩子  clean_字段名称 ，
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
            self.add_error('r_password','两次输入的密码不一致！') #给某个字段单独添加报错信息
            raise ValidationError('两次输入的密码不一致！')


循环所有字段进行验证，首先完成该字段实例化的时候的属性验证min_length=6，例如：Charfield（min_length=6）,然后通过反射执行该字段的局部钩子，然后进行下一次循环，完成该字段实例化的时候的属性验证min_length=6，例如：Charfield（min_length=6）,然后通过反射执行该字段的局部钩子，循环结束，self.clean_data里面有各个字段的数据，然后执行全局钩子


~~~
















































































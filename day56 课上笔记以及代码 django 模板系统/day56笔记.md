# 昨日内容回顾

## 路由分发

```

from django.conf.urls import url,include
url(r'app01/',include('app01.urls')),

```



## 视图函数

### 请求相关request

```
request.method  请求方法
request.body    post请求原始数据
request.POST
request.GET
request.path  获取路径
request.path_info  
request.get_full_path()  获取路径及参数

request.META 请求头相关信息

```

### 响应相关

```
HttpResponse  
render  
redirect  
```

### FBV和CBV

```

def index(request):
	return render(request,'xx.html')
	
from django.views import View	
class Index(View):
	def dispatch(self,request,*args,**kwargs):
		请求前干点儿事
		ret = super().dispatch(request,*args,**kwargs)
		请求后干点儿事儿
		return ret
	def get(self,request):
		...
    def post(self,request):
    	...

```



### 装饰器

```python
def bge(f):
	def inner(*args,**kwargs):
		前戏
		ret = f(*args,**kwargs)
		收工
		return ret
	return inner

@bge
def index(request):
	return render(request,'xx.html')

from django.utils.decorators import method_decorator

@method_decorator(bge,name='get')
class Index(View):
	@method_decorator(bge)
	def dispatch(self,request,*args,**kwargs):
		请求前干点儿事
		ret = super().dispatch(request,*args,**kwargs)
		请求后干点儿事儿
		return ret
		
	@method_decorator(bge)
	def get(self,request):
		...
    def post(self,request):
    	...

```





# 今日内容

## 模板渲染

```
语法 {{ 变量 }}  {% 逻辑 %}
```

### 变量

```python
示例
html代码:
	<p>{{ num }}</p>
    <p>{{ name }}</p>
    <p>{{ namelist.2 }}</p>
    <p>{{ d1.age }}</p>
    <p>{{ a.kind }}</p>
    <p>{{ a.eat }}</p>
views.py代码
	def index(request):
        num = 100
        name = 'shige'
        name_list = ['大壮','小壮','壮壮']
        d1 = {'name':'大壮','age':73,'hobby':'xuefei+xiangxi'}

        class Animal:
            def __init__(self):
                self.kind = 'dog'
            def eat(self):
                return 'shi'
        a = Animal()

        return render(request,'index.html',{'num':num,'name':name,'namelist':name_list,'d1':d1,'a':a})
		return render(request,'index.html',locals()) 
    	locals() 获取函数内部所有变量的值,并加工成{'变量名':'变量值'....}这样一个字典
```



### 过滤器

#### 内置过滤器

```html

<!-- 过滤器 -->
<!-- 获取数据长度,没参数 -->
<p>{{ name_list|length }}</p>

<!-- 默认值,有参数,如果一个变量是false或者为空，使用给定的默认值。 否则，使用变量的值。-->
<p>{{ xx|default:'啥也没有' }}</p>

<!-- 将值格式化为一个 “人类可读的” 文件尺寸 （例如 '13 KB', '4.1 MB', '102 bytes', 等等） -->
<p>{{ movesize|filesizeformat }}</p>
<!--  切片 -->
<p>{{ name|slice:':3' }}</p>
<!--  时间格式化显示 -->
<p>{{ now|date:'Y-m-d' }}</p>
<!--  字符截断 -->
<p>{{ words|truncatechars:'9' }}</p>

<!--  单词截断 -->
<p>{{ words|truncatewords:'3' }}</p>

<!-- 移除value中所有的与给出的变量相同的字符串 -->
<p>{{ words|cut:'i' }}</p>

<!-- 使用字符串连接列表，{{ list|join:', ' }}，就像Python的str.join(list) -->
<p>{{ name_list|join:'+' }}</p>

<!-- 将 字符串识别成标签-->
<p>{{ tag|safe }}</p>
```



### 标签

#### for循环标签

```
  循环一个字典
  {% for key,value in d1.items %} 
    {{ forloop.counter }}
      <li>{{ key }} -- {{ value }}</li>
  {% endfor %}

```



#### for循环其他方法

```
forloop.counter            当前循环的索引值(从1开始)，forloop是循环器，通过点来使用功能
forloop.counter0           当前循环的索引值（从0开始）
forloop.revcounter         当前循环的倒序索引值（从1开始）
forloop.revcounter0        当前循环的倒序索引值（从0开始）
forloop.first              当前循环是不是第一次循环（布尔值）
forloop.last               当前循环是不是最后一次循环（布尔值）
forloop.parentloop         本层循环的外层循环的对象，再通过上面的几个属性来显示外层循环的计数等
forloop.parentloop.counter
```

```
示例
	{#  {% for key,value in d1.items %}#}
    {#    {{ forloop.counter }}#}
    {#      <li>{{ key }} -- {{ value }}</li>#}
    {#  {% endfor %}#}

    {#    {% for key,value in d1.items %}#}
    {#    {{ forloop.counter0 }}#}
    {#      <li>{{ key }} -- {{ value }}</li>#}
    {#  {% endfor %}#}

    {#    {% for key,value in d1.items %}#}
    {#      {{ forloop.revcounter }}#}
    {#        <li>{{ key }} -- {{ value }}</li>#}
    {#    {% endfor %}#}

    {#      {% for key,value in d1.items %}#}
    {#        {{ forloop.revcounter0 }}#}
    {#          <li>{{ key }} -- {{ value }}</li>#}
    {#      {% endfor %}#}

    {#      {% for key,value in d1.items %}#}
    {#        {{ forloop.first }}#}
    {#          <li>{{ key }} -- {{ value }}</li>#}
    {#      {% endfor %}#}


    <!-- forloop.parentloop示例 -->
    {#<ul>#}
    {#    {% for dd2 in d2 %}#}
    {#      <li>#}
    {#        {% for ddd2 in dd2 %}#}
    {#          {{ forloop.parentloop.counter }}#}
    {#          {{ forloop.counter }}#}
    {#          <a href="">{{ ddd2 }}</a>#}
    {#        {% endfor %}#}
    {##}
    {#      </li>#}
    {#  {% endfor %}#}
    {#</ul>#}

    <!-- empty示例 -->
    {#<ul>#}
    {#   {% for foo in d3 %}#}
    {#       <li>{{ foo }}</li>#}
    {#   {% empty %}#}
    {#     <li>查询的内容啥也没有</li>#}
    {#  {% endfor %}#}
    {##}
    {#</ul>#}
```



#### if标签

```
{% if num > 100 or num < 0 %}
    <p>无效</p>  <!--不满足条件，不会生成这个标签-->
{% elif num > 80 and num < 100 %}
    <p>优秀</p>
{% else %}  <!--也是在if标签结构里面的-->
    <p>凑活吧</p>
{% endif %}

if语句支持 and 、or、==、>、<、!=、<=、>=、in、not in、is、is not判断，注意条件两边都有空格。


1. Django的模板语言不支持连续判断，即不支持以下写法：
{% if a > b > c %}
...
{% endif %}
2. Django的模板语言中属性的优先级大于方法（了解）
def xx(request):
    d = {"a": 1, "b": 2, "c": 3, "items": "100"}
    return render(request, "xx.html", {"data": d})

```



#### with标签

```
{% with total=business.employees.count %}
    {{ total }} <!--只能在with语句体内用-->
{% endwith %}

{% with business.employees.count as total %}
    {{ total }}
{% endwith %}
```



#### csrf_token标签

```
安全认证机制  
	我们以post方式提交表单的时候，会报错，还记得我们在settings里面的中间件配置里面把一个csrf的防御机制给注销了啊，本身不应该注销的，而是应该学会怎么使用它，并且不让自己的操作被forbiden，通过这个东西就能搞定。

	这个标签用于跨站请求伪造保护，

	在页面的form表单里面（注意是在form表单里面）任何位置写上{% csrf_token %}，这个东西模板渲染的时候替换成了<input type="hidden" name="csrfmiddlewaretoken" value="8J4z1wiUEXt0gJSN59dLMnktrXFW0hv7m4d40Mtl37D7vJZfrxLir9L3jSTDjtG8">，隐藏的，这个标签的值是个随机字符串，提交的时候，这个东西也被提交了，首先这个东西是我们后端渲染的时候给页面加上的，那么当你通过我给你的form表单提交数据的时候，你带着这个内容我就认识你，不带着，我就禁止你，因为后台我们django也存着这个东西，和你这个值相同的一个值，可以做对应验证是不是我给你的token，存储这个值的东西我们后面再学，你先知道一下就行了，就像一个我们后台给这个用户的一个通行证，如果你用户没有按照我给你的这个正常的页面来post提交表单数据，或者说你没有先去请求我这个登陆页面，而是直接模拟请求来提交数据，那么我就能知道，你这个请求是非法的，反爬虫或者恶意攻击我的网站，以后将中间件的时候我们在细说这个东西，但是现在你要明白怎么回事，明白为什么django会加这一套防御。
```



#### 模板继承

参考博客 <https://www.cnblogs.com/clschao/articles/10414811.html#part_7>

```
{% extends "base.html" %}

钩子:{% block title %}
		xxx
	{% endblock %}
钩子:{% block title %}
		xxx
	{% endblock title %}
	
钩子:{% block title %}
		{{ block.super }}  #显示模板内容
		xxx
	{% endblock title %}

```

#### 组件

```
{% include 'navbar.html' %}
```






# 昨日内容回顾

## 模板渲染

{{ 变量 }}   {% 逻辑 %}--标签

万能的据点号 .

### 过滤器

```
内置的过滤器
	length  -- {{ value|length }} 获取长度
	default -- 设置默认值
	cut -- 移除元素
	slice -- 切片
	join -- 拼接
	truncateChars -- 截断字符
	truncateWords -- 截断单词
	safe -- 让标签字符串识别成标签 (脚本攻击--xss)
	
	filesizeformat -- 将数字转换成可读的表示
	date -- 时间格式化
	
```



### 标签

```html
for标签   l1 = [11,22,33]  render(request,'xx.html',{'ll':l1})
{% for i in  ll%}
	<a>xx</a>
	
{% endfor %}
{% for k,v in  dd.items  dd.values dd.keys%}
	<a>xx</a>
{% endfor %}

{{ forloop.counter }}
{{ forloop.counter0 }}
{{ forloop.revcounter }}
{{ forloop.revcounter0 }}
{{ forloop.first }}
{{ forloop.last }}
{{ forloop.parentloop }}

empty
{% for i in  ll%}
	<a>xx</a>
{% empty %}
	xxx
{% endfor %}



if 标签
{% if 条件 1 > 2 %}

{% elif 条件 %}
	
{% else %}

{% endif %}


with标签 
{% with 别名=xx.xx.x.xx %}
	{{ 别名 }}
	
{% endwith %}
{% with xx.xx.x.xx as 别名%}
	{{ 别名 }}
	
{% endwith %}


{% csrf_token %}  -- form标签里面,任意位置

```



### 模板继承

```
1 创建模板,添加钩子,可以添加很多
	{% block 钩名 %}
		模板
	{% endblock 钩名 %}

2 其他html文件中要使用它
	开头 {% extends 'Muban.html' %}
	{% block 钩名 %}
		{{ block.super }}
		不同的部分
	{% endblock 钩名 %}
	
```

### 组件

```
zujian.html -- html内容
qita.html -- {% include 'zujian.html' %}

组件是提供某一完整功能的模块，如：编辑器组件，QQ空间提供的关注组件 等。
而插件更倾向封闭某一功能方法的函数。
这两者的区别在 Javascript 里区别很小，组件这个名词用得不多，一般统称插件。
```



# 今日内容

## 自定标签和过滤器

```python
自定义过滤器

1. app应用文件夹中创建一个templatetags文件件,必须是这个名字
2. templatetags文件夹中创建一个 xx.py文件,文件名字随便起

3. 创建自定义过滤器
    from django import template

    register = template.Library()  #register固定的名字,注册器

    # @register.filter
    # def oo(v1,v2):  #不带参数的过滤器
    #     s = v1 + 'xxoo'

    #     return s

    @register.filter
    def oo(v1,v2):  #带参数的过滤器
        s = v1 + v2
        return s
    
4. 使用  html文件中  {% load 文件名 %} 
	{% load xx %}
    {{ values|oo }} -- 无参数
    {{ values|oo:'asdf' }} -- 有参数

5. 注意:参数最多两个


自定义标签
1. app应用文件夹中创建一个templatetags文件件,必须是这个名字
2. templatetags文件夹中创建一个 xx.py文件,文件名字随便起
3. 创建自定义标签
	@register.simple_tag
	def mytag(v1,v2,v3):  
    	s = v1 + '和B哥' + v2 + v3
    	return s

4.使用
	{% load xx %}
	{% mytag s1 '和相玺' '和大壮' %}  
5. #可以传多个参数


```



### inclusion_tag

![img](file:///C:\Users\oldboy\AppData\Roaming\Tencent\Users\1069696250\TIM\WinTemp\RichOle\66K4M9Y~P]F4`L3HNQ}XD%N.png)



```python

1. app应用文件夹中创建一个templatetags文件件,必须是这个名字
2. templatetags文件夹中创建一个 xx.py文件,文件名字随便起
3. 创建自定义inclusion_tag
	@register.inclusion_tag('inclusiontag.html')
    def func(v1):

        return {'oo':v1}
4. func的return数据,传给了inclusiontag.html,作为模板渲染的数据,将inclusiontag.html渲染好之后,作为一个组件,生成到调用这个func的地方
5. 使用
	{% load xx %}
	{% func l1 %}


```



## 静态文件配置

　

　　js、css、img等都叫做静态文件，那么关于django中静态文件的配置，我们就需要在settings配置文件里面写上这写内容：

```
1 在项目中创建一个文件夹,比如叫jingtaiwenjian

# STATIC_URL = '/xxx/' #别名,随便写名字，但是如果你改名字，别忘了前面页面里面如果你是通过/xxx/bootstrap.css的时候，如果这里的别名你改成了/static/的话，你前端页面的路径要改成/static/bootstrap.css。所以我们都是用下面的load static的方式来使用静态文件路径
2 STATIC_URL = '/static/' #别名

3 STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'jingtaiwenjian'), #注意别忘了写逗号,第二个参数就是项目中你存放静态文件的文件夹名称
]
```

　　目录：别名也是一种安全机制，浏览器上通过调试台你能够看到的是别名的名字，这样别人就不能知道你静态文件夹的名字了，不然别人就能通过这个文件夹路径进行攻击。

　　　　![img](https://img2018.cnblogs.com/blog/988061/201902/988061-20190228171000665-346174028.png)

 

 　　前端页面引入静态文件的写法，因为别名也可能会修改，所以使用路径的时候通过load static来找到别名，通过别名映射路径的方式来获取静态文件

　　　　![img](https://img2018.cnblogs.com/blog/988061/201902/988061-20190228171108673-525833512.png)

 

 

### 　　{% static %}

```
{% load static %}
<img src="{% static "images/hi.jpg" %}" alt="Hi!" />
```

　　　　引用JS文件时使用：

```
{% load static %}
<script src="{% static "mytest.js" %}"></script>
```

　　　　某个文件多处被用到可以存为一个变量

```
{% load static %}
{% static "images/hi.jpg" as myphoto %}
<img src="{{ myphoto }}"></img>
```

### 　　{% get_static_prefix %}

```
{% load static %}
<img src="{% get_static_prefix %}images/hi.jpg" alt="Hi!" />
```

　　　　或者

```
{% load static %}
{% get_static_prefix as STATIC_PREFIX %}

<img src="{{ STATIC_PREFIX }}images/hi.jpg" alt="Hi!" />
<img src="{{ STATIC_PREFIX }}images/hi2.jpg" alt="Hello!" />
```





## orm

orm  -- Object Relational Mapping

将类对象 --- sql

类  --  表

对象 -- 行

属性  -- 字段



```python
app01 应用下 的models.py文件中写
	class UserInfo(models.Model):

        id = models.AutoField(primary_key=True)

        name = models.CharField(max_length=16,null=True,blank=True,db_index=True)

        age = models.IntegerField(default=1,unique=True,choices=((1,'男'),(2,'女'),(3,'二椅子')))

        current_date = models.DateField(auto_now=True,auto_now_add=True)

不连接mysql的话,默认连接的是sqlite数据库

配置连接mysql
1 settings.py 文件中找DATABASES这个配置,改为
	# DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.sqlite3',
    #         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #     }
    # }

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST':'127.0.0.1',
            'PORT':3306,
            'NAME':'orm01',
            'USER':'root',
            'PASSWORD':'123',
        }
    }

2 项目文件夹下的init文件中,写上下面两句
	import pymysql
	pymysql.install_as_MySQLdb()

3 执行数据库同步指令
	python manage.py makemigrations
	python manage.py migrate


```










































































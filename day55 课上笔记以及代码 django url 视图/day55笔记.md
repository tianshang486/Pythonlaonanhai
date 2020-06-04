# 昨日内容回顾

## django下载安装

```python
下载:pip install django==1.11.9

创建项目
	django-admin startproject qingqing
	cd qingqing 
启动项目:python manage.py runserver 127.0.0.1:8001
	cd qingqing 
创建app:python manage.py startapp xiaoqing

需要在项目的配置文件settings.py中添加一个app的配置
INSTALL_APPS = [
	
	'xiaoqing', app名称
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 以下两种写法都可以
    'app01.apps.App01Config',
    #'app01',
]

```



## 两个框架模式

```
MVC  
	M:models数据库相关
	V:views 视图逻辑相关
	C:controller控制器 url分发 不同的路径找到不同的视图函数
MTV
	M:models数据库相关
	T:templates模板 ,HTML文件
	V:views 视图逻辑相关
	+ url控制器 不同的路径找到不同的视图函数
MVVM 后面介绍
```



## url配置

```python
urls.py文件中写在urlpatterns = []中
简单的路由
	from app01 import views
	url(r'^index/',views.index),
无名分组
	url(r'^index/(\d+)/(\d+)/',views.index), --- def index(request,n,m)  位置参数
有名分组
	url(r'^index/(?P<year>\d+)/(?P<month>\d+)/',views.index), -- def index(request,year,month) 关键字参数,参数顺序不要求


url(r'^index/$',views.index),
url(r'^index/(?P<num>\d+)/,views.index),
视图函数参数默认值,
	def index(request,num='1'):
		print(num)

```



# 今日内容

## url路由分发之include

```python
项目文件夹下的urls.py文件中的url写法:
    from django.conf.urls import url,include
    from django.contrib import admin
    from app01 import views
    urlpatterns = [
        # url(r'^admin/', admin.site.urls),
        #首页
        url(r'^$', views.base),

        url(r'^app01/', include('app01.urls')),

        url(r'^app02/', include('app02.urls')),

    ]
    
app01下urls.py内容写法
    from django.conf.urls import url
    from django.contrib import admin
    from app01 import views
    urlpatterns = [
        # url(r'^admin/', admin.site.urls),
        url(r'^$', views.app01base),
        url(r'^index/', views.index),
    ]
    
app02下urls.py内容写法   
    from django.conf.urls import url
    from django.contrib import admin
    from app02 import views

    urlpatterns = [
        # url(r'^admin/', admin.site.urls),
        url(r'^$', views.app02base),
        url(r'^home/', views.home),

    ]

```



## 视图

## 请求相关的属性方法(request--HttpRequest对象)

```
def index(request): #http相关请求信息---封装--HttpRequest对象

    if request.method == 'GET':
        print(request.body)  #获取post请求提交过来的原始数据
        print(request.GET)   #获取GET请求提交的数据
        # print(request.META)  # 请求头相关信息,就是一个大字典
        print(request.path) #/index/ 路径
        print(request.path_info) #/index/ 路径
        print(request.get_full_path())  #/index/?username=dazhuang&password=123
        
        return render(request,'index.html')
    else:
        print(request.body)  # b'username=dazhuang'
        print(request.POST) #获取POST请求提交的数据
        return HttpResponse('男宾三位,拿好手牌!')

```

## 响应相关的方法

```python
HttpResponse  --- 回复字符串的时候来使用
render --- 回复一个html页面的时候使用
redirect -- 重定向
	示例:
	def login(request):
        if request.method == 'GET':
            return render(request,'login.html')
        else:
            username = request.POST.get('username')
            password = request.POST.get('password')
            if username == 'taibai' and password == 'dsb':
                # return render(request,'home.html')
                return  redirect('/home/')  #重定向
            else:
                return HttpResponse('滚犊子,赶紧去充钱!!!')

    #首页
    def home(request):
        return render(request,'home.html')

```



## FBV和CBV

```python
FBV -- function based view
def home(request):
    print('home!!!')
    return render(request,'home.html')
```

```python
CBV  -- class based view

views.py
    from django.views import View
    class LoginView(View):
        # 通过请求方法找到自己写的视图类里面对应的方法
        def get(self,request):

            return render(request,'login2.html')
        def post(self,request):
            username = request.POST.get('uname')
            password = request.POST.get('pwd')
            print(username,password)

            return HttpResponse('登录成功!')
            
urls.py
	url(r'^login2/', views.LoginView.as_view()),
```



CBV通过不同的请求方法找到对应的试图类中的方法

关键点,反射

```
    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)  #反射
```

CBV的dispatch方法

```python
from django.views import View
class LoginView(View):
    # GET 
    def dispatch(self, request, *args, **kwargs):
        print('请求来啦')
        ret = super().dispatch(request, *args, **kwargs)
        print('到点了,走人了')
        return ret
    def get(self,request):
        print('get方法执行了')
        return render(request,'login2.html')
    def post(self,request):
        username = request.POST.get('uname')
        password = request.POST.get('pwd')
        print(username,password)
        return HttpResponse('登录成功!')
```

FBV加装饰器

```python
def n1(f):
    def n2(*args,**kwargs):
        print('请求之前')
        ret = f(*args,**kwargs)
        print('请求之后')
        return ret
    return n2
@n1
def home(request):
    print('home!!!')
    return render(request,'home.html')
```



CBV加装饰器

```python
from django.views import View
from django.utils.decorators import method_decorator

def n1(f):
    def n2(*args,**kwargs):
        print('请求之前')
        ret = f(*args,**kwargs)
        print('请求之后')
        return ret
    return n2

# @method_decorator(n1,name='get') #方式三
class LoginView(View):
    # GET
    # @method_decorator(n1)  #方式2 给所有方法加装饰器
    def dispatch(self, request, *args, **kwargs):
        # print('请求来啦')
        ret = super().dispatch(request, *args, **kwargs)
        # print('到点了,走人了')
        return ret

    # @method_decorator(n1)  #方式1
    def get(self,request):
        print('get方法执行了')
        return render(request,'login2.html')
    def post(self,request):
        username = request.POST.get('uname')
        password = request.POST.get('pwd')
        print(username,password)
        return HttpResponse('登录成功!')
```




































































































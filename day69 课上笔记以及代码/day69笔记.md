

# 今日内容总结

csrf  跨站请求伪造

~~~
ajax（{
	
	data:{csrfmiddlewaretoken:$('[name=csrfmiddlewaretoken]').val(),
			// csrfmiddlewaretoken:'{{ csrf_token }}',
		}
}）
ajax（{
	
	url:'/test/',
    type:'post',
    headers:{
    	"X-CSRFToken": $.cookie('csrftoken'),
    },
}）


~~~

jquery操作cookie，文件地址<http://plugins.jquery.com/cookie/>

<https://www.cnblogs.com/clschao/articles/10480029.html>

~~~

<script src="{% static 'jquery.js' %}"></script>
<script src="{% static 'jquery.cookie.js' %}"></script>

~~~

同源机制

~~~
浏览器的一个安全机制，非同源不允许直接互相访问，同源：协议，域名(ip地址)，端口号三项相同才是同源

简单请求和复杂请求
简单请求：
（1) 请求方法是以下三种方法之一：（也就是说如果你的请求方法是什么put、delete等肯定是非简单请求）
    HEAD
    GET
    POST
（2）HTTP的头信息不超出以下几种字段：（如果比这些请求头多，那么一定是非简单请求）
    Accept
    Accept-Language
    Content-Language
    Last-Event-ID
    Content-Type：只限于三个值application/x-www-form-urlencoded、multipart/form-data、text/plain，也就是说，如果你发送的application/json格式的数据，那么肯定是非简单请求，vue的axios默认的请求体信息格式是json的，ajax默认是urlencoded的。

简单请求只发送一次请求


复杂请求(非简单请求) 发送两次请求


* 简单请求和非简单请求的区别？

   简单请求：一次请求
   非简单请求：两次请求，在发送数据之前会先发一次请求用于做“预检”，只有“预检”通过后才再发送一次请求用于数据传输。
* 关于“预检”

- 请求方式：OPTIONS
- “预检”其实做检查，检查如果通过则允许传输数据，检查不通过则不再发送真正想要发送的消息
- 如何“预检”
     => 如果复杂请求是PUT等请求，则服务端需要设置允许某请求，否则“预检”不通过
        Access-Control-Request-Method
     => 如果复杂请求设置了请求头，则服务端需要设置允许某请求头，否则“预检”不通过
        Access-Control-Request-Headers


请求的网站响应内容：
def index(request):
    a = {'name':'chao'}
    ret = JsonResponse(a)
    ret["Access-Control-Allow-Origin"] = "http://127.0.0.1:8000" #让http://127.0.0.1:8000这个网址的所有请求都能通过同源机制获得我给他响应的数据
    ret["Access-Control-Allow-Origin"] = "*"
    ret["Access-Control-Allow-Origin"] = "http://127.0.0.1:8000，http://127.0.0.1:8001，"
    ret["Access-Control-Allow-Headers"] = "content-type" #让所有的请求数据格式都能通过同源机制，
    return ret



~~~



modelform 通过model的属性自动翻译成form的属性，来进行form组件的工作



~~~
from django.core.exceptions import ValidationError
class BookModelForm(forms.ModelForm):
    # title=forms.CharField(max_length=15,min_length=6)
	
    class Meta:
        model = models.Book
        # fields=['title','publishs',]
        fields='__all__'
        # exclude = ['title','xx',]

        labels = {
            'title':'书名',
            'publishDate':'出版日期',
        }
        widgets = {
            'publishDate':forms.widgets.TextInput(attrs={'type':'date'}),
        }
        error_messages = {
            'title':{'required':'不能为空',},
            'publishDate':{'required':'不能为空',}
        }

    # def clean_title(self):
    #     value = self.cleaned_data.get('title')
    #     if '666' in value:
    #         raise ValidationError('光喊6是不行的！！')
    #     else:
    #         return value
    # def clean(self):
    #     ...
	#批量添加标签样式
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class':'form-control'})


~~~
























































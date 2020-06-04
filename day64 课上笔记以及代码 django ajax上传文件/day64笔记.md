# 昨日内容回顾

## 锁和事务

```

select .... for update
models.Book.objects.select_for_update().filter(xx=xx)


全局的

局部的
	1 给视图函数加
	
	from django.db import transaction
	
	@transaction.atomic
	def xx(request):
	
		return...

	2 在上下文中使用
		def xx(request):
			...
			with transaction.atomic():
				...
				
            ...
			return...
```



Ajax

```
特性:
	1.异步请求
	2.局部刷新

	$.ajax({
		url:'/login/',
		type:'post',
		data:{
			username:$('[name=username]').val(),
			password:$('[name=password]').val(),
			csrfmiddlewaretoken:$('[name=csrfmiddlewaretoken]').val(),
			
		},
        success:function(response){
        	var response = JSON.parse(response); #反序列化
			response 视图函数返回值
		}
	
	})
	
```



# 今日内容



## 上传文件

## form表单上传文件

```
<form action="/upload/" method="post" enctype="multipart/form-data"> 
  {% csrf_token %}
  头像: <input type="file" name="head-pic">
  用户名: <input type="text" name="username">
  <input type="submit">
</form>


def upload(request):
    if request.method == 'GET':

        return render(request,'upload.html')
    else:
        print(request.POST)  #拿到的是post请求的数据,但是文件相关数据需要用request.FILES去拿
        print(request.FILES) #<MultiValueDict: {'head-pic': [<InMemoryUploadedFile: 1.png (image/png)>]}>
        file_obj = request.FILES.get('head-pic')
        print(file_obj)
        file_name = file_obj.name


        # f = open('xx.txt','rb')
        # with open('xx.txt','wb') as f2:
        #     for i in f:
        #         f2.write(i)
        import os
        path = os.path.join(settings.BASE_DIR,'statics','img',file_name)
        with open(path,'wb') as f:
            for i in file_obj:
                f.write(i)
			#for chunk in  file_obj.chunks():
            #    f.write(chunk)

        return HttpResponse('ok')


```



## ajax上传文件

```


var formdata = new FormData();
formdata.append('user',$('#username').val())
formdata.append('csrfmiddlewaretoken',$('#csrfmiddlewaretoken').val())
formdata.append('file',$('#file')[0].files[0])
$.ajax({
	url:'/upload/',
	type:'post',
	data:formdata,
	success:function(response){
		response
	
	}

})

def upload(request):
    if request.method == 'GET':

        return render(request,'upload.html')
    else:
        print(request.POST)  #拿到的是post请求的数据,但是文件相关数据需要用request.FILES去拿
        print(request.FILES) #<MultiValueDict: {'head-pic': [<InMemoryUploadedFile: 1.png (image/png)>]}>
        file_obj = request.FILES.get('head-pic')
        print(file_obj)
        file_name = file_obj.name


        # f = open('xx.txt','rb')
        # with open('xx.txt','wb') as f2:
        #     for i in f:
        #         f2.write(i)
        import os
        path = os.path.join(settings.BASE_DIR,'statics','img',file_name)
        with open(path,'wb') as f:
            for i in file_obj:
                f.write(i)
			#for chunk in  file_obj.chunks():
            #    f.write(chunk)

        return HttpResponse('ok')



```



## JsonResponse

```
def index(request):

​	d1 = {'name':'chao'}

​	import json

​	return HttpResponse(json.dumps(d1))  -- success:function(res){ var a = JSON.parse(res) }

​	return HttpResponse(json.dumps(d1),content-type='application/json') --success:function(res){res--自定义对象,不需要自己在反序列化了}

​	return JsonResponse(d1)

​	d1 = [11,22]  #非字典类型的数据都需要加safe=False

​	return JsonResponse(d1,safe=False)
```



获取多对多数据的时候

```
authors = request.POST.getlist('authors')
```



## json序列化时间日期类型的数据的方法

```
import json
from datetime import datetime
from datetime import date

#对含有日期格式数据的json数据进行转换
class JsonCustomEncoder(json.JSONEncoder):
    def default(self, field):
        if isinstance(field,datetime):
            return field.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(field,date):
            return field.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self,field)


d1 = datetime.now()

dd = json.dumps(d1,cls=JsonCustomEncoder)
print(dd)
```




























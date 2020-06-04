# 昨日内容回顾

## 分组

```
annotate

models.Author.objects.annotate(a=Avg('book__price')).values('a')
models.Author.objects.values('id').a=Avg('book__price'))  -- queryset[{'id':1,'a':123}]

```

## F查询

```

models.Book.objects.filter(good__gt=F('comment'))
models.Book.objects.all().update(price=F('price')+20)
```

## Q查询

```
Q()   &  |  ~
models.Book.objects.filter(Q(good__gt=100)|Q(comment__gt=100))
models.Book.objects.filter(Q(good__gt=100)|Q(comment__gt=100)&Q(price__gt=100))
models.Book.objects.filter(Q(Q(good__gt=100)|Q(comment__gt=100))&Q(price__gt=100))
models.Book.objects.filter(~Q(good__gt=100)|Q(comment__gt=100),price__gt=100) 
```

sql_mode

```mysql
only_full_group_by
select * from book;
select publish_id,Avg(price) from book group by publish_id; 
没有 only_full_group_by
select *,avg(price) from book group by publish_id; 
select *,max(price) from book group by publish_id;

```





# 今日内容

## 事务和锁

```

select * from t1 where id=1 for update;
models.T1.objects.select_for_update().fitler(id=1)

事务
1 全局的,就是settings配置文件配置
2 局部
	视图函数
	from django.db import transaction
	@transaction.atomic
	def index(request):
		pass orm...sql..
		return xxx
	上下文逻辑里面加
	def index(request):
		..
		with transaction.atomic():
			pass orm...sql..
		...
		return xxx
	
```



## ajax

```
特性:
	1. 异步请求
	2. 局部刷新
	# ret = requests.post('/login/',data={})  print(ret.content)
	
	$.ajax({
		url:'/login/', #请求路径
 		type:'post' ,   #请求方式
		data:{
			username:$('#username').val(),
			password:$('#password').val(),
			csrfmiddlewaretoken:
			},
			
		success:function(response){
			response  #响应内容
			var resStr = JOSN.parse(respone);
			# {"aa":0,"bb":"/index/"}
			if (resStr['aa'] === 0){
				// alert('xx')
				locaction.href=resStr['bb'];
				location.href='/index/';
			}
			else{
				...
			
			}
			
		
		}
	})

view.py  看代码


```

外部文件导入的方式来写js代码,那么js代码中不能写django的模板语法,因为html文件的加载顺序:url--视图--html模板渲染 --- return给浏览器 -- 浏览器渲染 --- srcipt的src --才去请求js文件 --那么这个js文件的代码此时才加载到你的html文件中 -- 就没有模板渲染的步骤了 -- 就没有办法替换对应的模板语法.



## 


























































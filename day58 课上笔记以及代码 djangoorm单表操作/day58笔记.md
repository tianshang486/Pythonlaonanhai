# 昨日内容回顾

自定义标签和过滤器,inclusion_tag

```

1. app应用文件夹中,创建一个py文件
	from django import template
	
	register = template.Library()
	
	@register.simple_tag
	def fuck(v1):
		return xxx
		
2. html使用
	{% load py文件 %}
	
	{% fuck xx %}	
		
3. 过滤器	
	@register.filter
	def fuck(v1):
		return xxx

	@register.inclusion_tag('tt.html')
	def fuck(v1):
		return {'xxx':xxx}
	

```



## 静态文件配置

```

1. 项目路径下面创建一个staticsfile文件夹
2. settings配置文件中
	STATICFILES_DIRS = [
		os.path.join(BASE_DIR,'staticsfile'),
	]
3. html
	{% load static %}
	
	link	href='{% static "css文件路径" %}'
				 '/staic/css文件路径'
				 '{% get_static_prefix %}css文件路径'

```



## orm

应用的文件夹中的models.py文件中写类

```
class Student(models.Model):
	id = models.AutoField(primary_key = True)
	...

```

数据库同步指令

```
python manage.py makemigrations
ptthon manage.py migrate
```



settings文件中

```
DATABASES = {
	'default':{
		'ENGINE':'...mysql',
		'NAME':'库名',
		'HOST':'127.0.0.1',  
		'PORT':3306,
		'USER':'root',
		'PASSWORD':'123'
	}

}
```

项目的init文件中

```
import pymysql
pymysql.install_as_MySQLdb()

```



# 今日内容

## ORM单表操作

```
类---表
类对象 --- 一行数据
类属性 --- 字段


```

增

```python
创建记录方式1
    student_obj = models.Student(
        name='dazhaung',
        age=23,
    )
    student_obj.save()
创建记录方式2
    new_obj = models.Student.objects.create(name='xiaozhuang2',age=6) #写成 **{'name':'xx'}
    print(new_obj)  #Student object --  model对象
    print(new_obj.name)  #点属性,可以获取对应字段的数据
    print(new_obj.age)

创建方式3 批量创建
    objs_list = []
    for i in range(100,3000000):
        obj = models.Student(
            name='xiangxixxx',
            age = 10,
        )
        objs_list.append(obj)

    models.Student.objects.bulk_create(objs_list)

创建方法4 update_or_create 有就更新,没有就创建
    models.Student.objects.update_or_create(
        name='红旭妹妹2',
        defaults={
            'age':38,
        }
    )

添加日期数据
    import datetime
    current_date = datetime.datetime.now()
    # print(current_date) #2019-07-19 12:19:26.385654
	# 两种方式
    # models.Brithday.objects.create(name='B哥',date=current_date)
    # models.Brithday.objects.create(name='得港10',date='2000-12-08')
    
```

删:

```
 删除  delete  queryset 和model对象都可以调用
    models.Student.objects.get(id=3).delete()  #model对象来调用的delete方法
    models.Student.objects.filter(name='红旭妹妹').delete() #
    models.Student.objects.all().delete() #删除所有
```

改

```
更新 update方法 model对象不能调用更新方法 报错信息'Student' object has no attribute 'update'
    只能queryset调用,如果
    models.Student.objects.get(name='红旭妹妹').update(age=38)
    models.Student.objects.filter(name='红旭妹妹').update(age=38)

```

简单查

```python

查询所有的数据  .all方法 返回的是queryset集合
    all_objs = models.Student.objects.all()
    #<QuerySet [<Student: Student object>, <Student: Student object>, <Student: Student object>]> -- 类似于列表  --  queryset集合
    # for i in all_objs:
    #     print(i.name)
    print(all_objs)

条件查询  .filter方法,返回的也是queryset集合,查询不到内容,不会 报错,返回一个<QuerySet []>空的queryset
    objs = models.Student.objects.filter(id=2)  #找id为2的那条记录
    print(objs) #<QuerySet [<Student: xiaozhuang>]>
    objs = models.Student.objects.filter(name='dazhaung')
    print(objs) #<QuerySet [<Student: dazhaung>]>

条件查询 get方法,返回的是model对象,而且get方法有且必须只有1个结果
    obj = models.Student.objects.get(id=3)  #找id为3的那条记录
    print(obj)  #xiaozhuang2
```



## 查询接口

```python
<1> all():                  查询所有结果，结果是queryset类型
  
<2> filter(**kwargs):       它包含了与所给筛选条件相匹配的对象，结果也是queryset类型 Book.objects.filter(title='linux',price=100) #里面的多个条件用逗号分开，并且这几个条件必须都成立，是and的关系，or关系的我们后面再学，直接在这里写是搞不定or的
	models.Student.objects.filter(id=7,name='大壮哥哥',age=78).update(
        name='大壮禅师',
        age=78
    )
    #打伞形式传参
    models.Student.objects.filter(**{'id':7,'name':'大壮禅师'}).update(age=100)
  	models.Student.objects.all().filter(id=7)  queryset类型可以调用fitler在过滤
  
<3> get(**kwargs):          返回与所给筛选条件相匹配的对象，不是queryset类型，是行记录对象，返回结果有且只有一个，
                            如果符合筛选条件的对象超过一个或者没有都会抛出错误。捕获异常try。  Book.objects.get(id=1)
  
<4> exclude(**kwargs):      排除的意思，它包含了与所给筛选条件不匹配的对象，没有不等于的操作昂，用这个exclude，返回值是queryset类型 Book.objects.exclude(id=6)，返回id不等于6的所有的对象，或者在queryset基础上调用，Book.objects.all().exclude(id=6)
    # exclude(**kwargs): 排除,objects控制器和queryset集合都可以调用,返回结果是queryset类型
    # query = models.Student.objects.exclude(id=1)
    # print(query)
    # query = models.Student.objects.filter(age=38).exclude(id=6)
    # print(query)
 　　　　　　　　　　　　　　　　
<5> order_by(*field):       queryset类型的数据来调用，对查询结果排序,默认是按照id来升序排列的，返回值还是queryset类型
　　　　　　　　　　　　　　　　  models.Book.objects.all().order_by('price','id') #直接写price，默认是按照price升序排列，按照字段降序排列，就写个负号就行了order_by('-price'),order_by('price','id')是多条件排序，按照price进行升序，price相同的数据，按照id进行升序
        
        
<6> reverse():              queryset类型的数据来调用，对查询结果反向排序，返回值还是queryset类型
			# 排序之后反转
  		    # query = models.Student.objects.all().order_by('id').reverse()
    		# print(query)

<7> count():                queryset类型的数据来调用，返回数据库中匹配查询(QuerySet)的对象数量。
  
<8> first():                queryset类型的数据来调用，返回第一条记录 Book.objects.all()[0] = Book.objects.all().first()，得到的都是model对象，不是queryset
  
<9> last():                queryset类型的数据来调用，返回最后一条记录,结果为model对象类型
  
<10> exists():              queryset类型的数据来调用，如果QuerySet包含数据，就返回True，否则返回False
　　　　　　　　　　　　　　     空的queryset类型数据也有布尔值True和False，但是一般不用它来判断数据库里面是不是有数据，如果有大量的数据，你用它来判断，那么就需要查询出所有的数据，效率太差了，用count或者exits
　　　　　　　　　　　　　　　　 例：all_books = models.Book.objects.all().exists() #翻译成的sql是SELECT (1) AS `a` FROM `app01_book` LIMIT 1，就是通过limit 1，取一条来看看是不是有数据

<11> values(*field):        用的比较多，queryset类型的数据来调用，返回一个ValueQuerySet——一个特殊的QuerySet，运行后得到的并不是一系列
                            model的实例化对象，而是一个可迭代的字典序列,只要是返回的queryset类型，就可以继续链式调用queryset类型的其他的查找方法，其他方法也是一样的。
<12> values_list(*field):   它与values()非常相似，它返回的是一个元组序列，values返回的是一个字典序列
 
<13> distinct():            values和values_list得到的queryset类型的数据来调用，从返回结果中剔除重复纪录,结果还是queryset
	query = models.Student.objects.all().values('age').distinct()
    print(query)
	
	
```



### 基于双下划线的模糊查询　

```python
Book.objects.filter(price__in=[100,200,300]) #price值等于这三个里面的任意一个的对象
Book.objects.filter(price__gt=100)  #大于，大于等于是price__gte=100，别写price>100，这种参数不支持
Book.objects.filter(price__lt=100)
Book.objects.filter(price__range=[100,200])  #sql的between and，大于等于100，小于等于200
Book.objects.filter(title__contains="python")  #title值中包含python的
Book.objects.filter(title__icontains="python") #不区分大小写
Book.objects.filter(title__startswith="py") #以什么开头，istartswith  不区分大小写
Book.objects.filter(pub_date__year=2012)

# all_books = models.Book.objects.filter(pub_date__year=2012) #找2012年的所有书籍
    # all_books = models.Book.objects.filter(pub_date__year__gt=2012)#找大于2012年的所有书籍
    all_books = models.Book.objects.filter(pub_date__year=2019,pub_date__month=2)#找2019年月份的所有书籍，如果明明有结果，你却查不出结果，是因为mysql数据库的时区和咱们django的时区不同导致的，了解一下就行了，你需要做的就是将django中的settings配置文件里面的USE_TZ = True改为False，就可以查到结果了，以后这个值就改为False，而且就是因为咱们用的mysql数据库才会有这个问题，其他数据库没有这个问题。
```



























































## 






















































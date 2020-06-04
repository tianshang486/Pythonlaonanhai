# 昨日内容回顾

## orm单表操作

增删改查

增加

```
models.Student(name='yuhong',age=23).save()

models.Student.objects.create(name='yuhong',age=23)

obj_list = []
for i in range(10):
	obj = models.Student(name='yuhong',age=23)
	obj_list.append(obj)

models.Student.objects.bulk_create(obj_list)

models.Student.objects.update_or_create(
	name='xx',
	default = {
		'age':34,
	}
)
```

删

```
models.Student.objects.filter(name='红旭妹妹').delete()
models.Student.objects.get(name='红旭妹妹').delete()
```

改

```
models.Student.objects.filter(name='红旭妹妹').update(age=88)
```

查

```python
.all    models.Student.objects.all() 

.filter models.Student.objects.filter() 

.get    models.Student.objects.get() 

.exclude  models.Student.objects.exclude(name='xx')
		  models.Student.objects.filter().exclude(name='xx') 
.order_by models.Student.objects.filter().order_by('-id','age')

.reverse  models.Student.objects.filter().order_by('-id','age').reverse()

.count   models.Student.objects.filter().count()  

.first() models.Student.objects.filter().first()

.last()

.exists() models.Student.objects.filter('name').exists()

.values() models.Student.objects.filter().values()
		  models.Student.objects.values('name') -- 记住

.values_list() models.Student.objects.filter().values_list() 
			   models.Student.objects.values_list('name')

.distinct()    models.Student.objects.values_list('name').distinct()

```

filter 模糊查询

```
	models.Student.objects.filter(age__gt=50)
	age__lt=50  age__gte=50  age__lte=50
	models.Student.objects.filter(age__in=[50,80,100])
	models.Student.objects.filter(age__range=[50,80])
	models.Student.objects.filter(name__contains='xx')
	models.Student.objects.filter(name__icontains='xx')
	models.Student.objects.filter(name__startswith='xx')
	models.Student.objects.filter(name__istartswith='xx')
	models.Student.objects.filter(name__endswith='xx')
	models.Student.objects.filter(pubdate__year__gt=2018)
	models.Student.objects.filter(pubdate__year__gt=2018,pubdate__month__gt=5)
```





# 今日内容

外部文件操作django的models

```
#外部文件使用django的models,需要配置django环境
import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "singletablehw.settings")
    import django
    django.setup()

    from app01 import models
    import datetime
    obj_list = []
    for i in range(1,10):
        obj = models.Book(
            title='葵花宝典第%s式'%i,
            price=20 + i,
            pub_date='198%s-11-11 00:00:00'%i,
            # pub_date=datetime.datetime.now(),

            publish= '吴老板出版社' if i < 5 else '太白出版社',

        )
        obj_list.append(obj)

    models.Book.objects.bulk_create(obj_list)

```



url别名反向解析

```
    #添加书籍
    url(r'^add_book/', views.add_book,name='abook'), #name='abook'  别名

    # 删除书籍
    url(r'^delete_book/(\d+)/', views.delele_book,name='delete_book'),

视图:
	from django.urls import reverse
	reverse('别名')  reverse('abook') -- /add_book/  #不带参数的
	print(reverse('delete_book',args=(71,))) #/delete_book/71/ 带参数的
模板
	{% url 'abook' %}  无参数的
	{% url 'delete_book' book.id %}  无参数的

```








































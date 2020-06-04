# 昨日内容回顾

## url别名和反向解析

```

	url(r'^index/',views.index,name='index')
	url(r'^index/(\d+)/',views.index,name='index')
	视图
		from django.urls import reverse
		reverse('别名')
		reverse('别名',args=(1,))
	模板
    	{% url '别名' %}
    	{% url '别名' id %}
	
```



外部文件操作models

```
import os
if __name__ == '__main__':
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "singletablehw.settings")
	import django 
	django.setup()
	from app01 import models
	...

```



# 今日内容

三种关系:一对一,一对多,多对多

### 创建表  

```python
一对一
	xx = models.OneToOneField(to='表名',to_field='字段名',on_delete=models.CASCADE)  #删除时的一些级联效果,to_field可以不写,默认是关联到另一张表的主键,on_delete在1.x版本的django中不用写,默认是级联删除的,2.x版本的django要写.
	
一对多
	xx = models.ForeignKey(to='表名',to_field='字段名',on_delete=models.CASCADE)
多对多
	xx = models.ManyToManyField(to='另外一个表名') #这是自动创建第三表
	
示例
	from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
#作者表
class Author(models.Model): #比较常用的信息放到这个表里面
    name=models.CharField( max_length=32)
    age=models.IntegerField()
    # authorDetail=models.OneToOneField(to="AuthorDetail",to_field="nid",on_delete=models.CASCADE)
    authorDetail=models.OneToOneField(to='AuthorDetail')  #一对一到AuthorDetail表  生成为表字段之后,会自动变为authorDetail_id这样有一个名称

    # 外键字段 -- 外键字段名_id

    # foreign+unique

    def __str__(self):
        return self.name

#作者详细信息表
class AuthorDetail(models.Model):
    birthday=models.DateField()
    # telephone=models.BigIntegerField()
    telephone=models.CharField(max_length=32)
    addr=models.CharField( max_length=64)
    def __str__(self):
        return self.addr


#出版社表   和 书籍表 是 一对多的关系
class Publish(models.Model):
    name=models.CharField( max_length=32)
    city=models.CharField( max_length=32)
    email=models.EmailField()  #charfield -- asdfasdf
    def __str__(self):
        return self.name

#书籍表
class Book(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField( max_length=32)
    publishDate=models.DateField()
    price=models.DecimalField(max_digits=5,decimal_places=2)  #decimal(16,2)
    publishs=models.ForeignKey(to="Publish")
    authors=models.ManyToManyField(to='Author',)

    def __str__(self):
        return self.title

#手动创建第三张表,暂时忽略
# class BookToAuthor(models.Model):
#     book_id = models.ForeignKey(to='Book')
#     author_id = models.ForeignKey(to='Author')
#     # xx = models.CharField(max_length=12)


```



增删改查

增

```

#1 增
    #1.1 一对一增加
    # new_author_detail = models.AuthorDetail.objects.create(
    #     birthday='1979-08-08',
    #     telephone='138383838',
    #     addr='黑龙江哈尔滨'
    # )
    # obj = models.AuthorDetail.objects.filter(addr='山西临汾').first()

    #方式1
    # models.Author.objects.create(
    #     name='王涛',
    #     age='40',
    #     authorDetail=new_author_detail,
    # )
    # 方式2  常用
    # models.Author.objects.create(
    #     name='王涛',
    #     age='40',
    #     authorDetail_id=obj.id,
    # )

    # 一对多
    #方式1
    # obj = models.Publish.objects.get(id=2)
    # models.Book.objects.create(
    #     title = '李帅的床头故事',
    #     publishDate='2019-07-22',
    #     price=3,
    #     # publishs=models.Publish.objects.get(id=1),
    #     publishs=obj,
    #
    # )
    # 方式2 常用
    # models.Book.objects.create(
    #     title='李帅的床头故事2',
    #     publishDate='2019-07-21',
    #     price=3.5,
    #     # publishs=models.Publish.objects.get(id=1),
    #     publishs_id=obj.id
    #
    # )

    # 多对多
    # 方式1   常用
    # book_obj = models.Book.objects.get(nid=1)
    # book_obj.authors.add(*[1,2])
    # 方式2
    # author1 = models.Author.objects.get(id=1)
    # author2 = models.Author.objects.get(id=3)
    # book_obj = models.Book.objects.get(nid=5)
    # book_obj.authors.add(*[author1,author2])
```



删

```
一对一和一对多的删除和单表删除是一样的
# 一对一  表一外键关联到表二,表一删除,不影响表2,表2删除会影响表1
    # models.AuthorDetail.objects.get(id=2).delete()
    # models.Author.objects.get(id=3).delete()

    # 一对多
    # models.Publish.objects.get(id=1).delete()
    # models.Book.objects.get(nid=1).delete()

    # 多对多关系删除
    # book_obj = models.Book.objects.get(nid=6)
    # book_obj.authors.remove(6)
    # book_obj.authors.remove(*[5,6])
    # book_obj.authors.clear()
    # book_obj.authors.add(*[1,])
    # book_obj.authors.set('1')
    # book_obj.authors.set(['5','6']) #删除然后更新

```

更新

```
    # 更新
    # 一对一
    # models.Author.objects.filter(id=5).update(
    #     name='崔老师',
    #     age=16,
    #     # authorDetail=models.AuthorDetail.objects.get(id=5),
    #     authorDetail_id=4,
    # )
    #一对多
    # models.Book.objects.filter(pk=4).update(
    #     title='B哥的往事2',
    #     # publishs=models.Publish.objects.get(id=3),
    #     publishs_id=3,
    # )
    
    #一对多
    models.Publish.objects.filter(pk=2).update(
        id=4, # 没有级联更新,报错!!
    )
```










































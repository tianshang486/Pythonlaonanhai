# 昨日内容回顾

创建

```

class Author(models.Model): #比较常用的信息放到这个表里面
    name=models.CharField( max_length=32)
    age=models.IntegerField()
   					  authorDetail=models.OneToOneField(to="AuthorDetail",to_field="nid",on_delete=models.CASCADE)
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

```



增删改查

增加

```
一对一
models.Author.objects.create(name='xx',age=18,authorDetail=mdoels.AuthorDetail.Objects.get(id=1))
models.Author.objects.create(name='xx',age=18,authorDetail_id=2)

一对多
models.Book.objects.create(xx=xx,publishs=mdoels.Publish.Objects.get(id=1))
models.Book.objects.create(xx=xx,publishs_id=2)

多对多
book_obj = models.Book.objects.get(id=1)
book_obj.authors.add(*[author_obj1,author_obj2,..])
book_obj.authors.add(*[1,2,3...])
```

删除

```
一对一
models.Author.objects.filter(id=1).delete()
一对多
models.Book.objects.filter(id=1).delete()
多对多
book_obj = models.Book.objects.get(id=1)
book_obj.authors.remove(1,2,3,4)
book_obj.authors.remove(*[1,2,...])

book_obj.authors.clear()

book_obj.authors.set(['1','2',...]) :clear -- add

```



改

```
一对一
models.Author.objects.filter(id=1).update(
	authorDetail=mdoels.AuthorDetail.Objects.get(id=1)
)
models.Author.objects.filter(id=1).update(
	authorDetail_id=2,
)
一对多
models.Book.objects.filter(id=1).update(
	publishs=mdoels.Publish.Objects.get(id=1)
)
models.Book.objects.filter(id=1).update(
	publishs_id=2,
)

多对多
book_obj.authors.set(['1','2',...]) :clear -- add

```



# 今日内容

## 查询

### 基于对象的跨表查询 -- 类似于子查询

正向查询和反向查询

关系属性(字段)写在哪个类(表)里面,从当前类(表)的数据去查询它关联类(表)的数据叫做正向查询,反之叫做反向查询

```
#查询
    # 一对一
        # 正向查询
        #1 查询崔老师的电话号
    # author_obj = models.Author.objects.filter(name='崔老师').first()
    # # print(author_obj.authorDetail) #辽宁峨眉山
    # # print(author_obj.authorDetail.telephone) #444
    #     #2 反向查询
    #     #2 查询一下这个444电话号是谁的.
    # author_detail_obj = models.AuthorDetail.objects.get(telephone='444')
    # print(author_detail_obj.author) #崔老师
    # print(author_detail_obj.author.name) #崔老师


    '''        正向查询:Authorobj.authorDetail,对象.关联属性名称
        Author----------------------------------->AuthorDetail
              <-----------------------------------
              反向查询:AuthorDetailobj.author  ,对象.小写类名
    '''

    # 一对多
    # 查询一下李帅的床头故事这本书的出版社是哪个
    # 正向查询
    book_obj = models.Book.objects.get(title='李帅的床头故事')
    print(book_obj.publishs) #B哥出版社
    print(book_obj.publishs.name) #B哥出版社

    # B哥出版社出版社出版了哪些书
    # 反向查询
    pub_obj = models.Publish.objects.get(name='B哥出版社')
    print(pub_obj.book_set.all()) #<QuerySet [<Book: 李帅的床头故事>, <Book: 李帅的床头故事2>]>

    '''   正向查询 book_obj.publishs  对象.属性
    Book ---------------------------------------------> Publish
        <----------------------------------------------
          反向查询 publish_obj.book_set.all()  对象.表名小写_set
    '''

    # 多对多
    # 李帅的床头故事这本书是谁写的
    # 正向查询
    book_obj = models.Book.objects.get(title='李帅的床头故事')
    print(book_obj.authors.all())
    # 高杰写了哪些书
    author_obj = models.Author.objects.get(name='高杰')
    print(author_obj.book_set.all())

    '''       正向查询 book_obj.authors.all()  对象.属性
        Book ---------------------------------------------> Author
            <----------------------------------------------
              反向查询 author_obj.book_set.all()  对象.表名小写_set
    '''




```



### 基于双下划綫的跨表查询 -- 连表 join

正向查询和反向查询

```
#查询
    # 一对一
    # 1. 查询崔老师的电话号
    # 方式1  正向查询
    # obj = models.Author.objects.filter(name='崔老师').values('authorDetail__telephone')
    # print(obj) #<QuerySet [{'authorDetail__telephone': '444'}]>
    # 方式2  反向查询
    # obj = models.AuthorDetail.objects.filter(author__name='崔老师').values('telephone','author__age')
    # print(obj) #<QuerySet [{'telephone': '444'}]>
    # 2. 哪个老师的电话是444
    # 正向
    # obj = models.Author.objects.filter(authorDetail__telephone='444').values('name')
    # print(obj)
    # 反向
    # obj = models.AuthorDetail.objects.filter(telephone='444').values('author__name')
    # print(obj)

    # 一对多
    # 查询一下李帅的床头故事这本书的出版社是哪个
    # obj = models.Book.objects.filter(title='李帅的床头故事').values('publishs__name')
    # print(obj) #<QuerySet [{'publishs__name': 'B哥出版社'}]>

    # obj = models.Publish.objects.filter(book__title='李帅的床头故事').values('name')
    # obj = models.Publish.objects.filter(xx__title='李帅的床头故事').values('name')
    # print(obj)

    # B哥出版社出版社出版了哪些书
    # obj = models.Publish.objects.filter(name='B哥出版社').values('book__title')
    # print(obj) #<QuerySet [{'book__title': '李帅的床头故事'}, {'book__title': '李帅的床头故事2'}]>

    # obj = models.Book.objects.filter(publishs__name='B哥出版社').values('title')
    # print(obj) #<QuerySet [{'title': '李帅的床头故事'}, {'title': '李帅的床头故事2'}]>

    # 李帅的床头故事这本书是谁写的
    # obj = models.Book.objects.filter(title='李帅的床头故事').values('authors__name')
    # print(obj)
    # obj = models.Author.objects.filter(book__title='李帅的床头故事').values('name')
    # print(obj) #<QuerySet [{'name': '高杰'}, {'name': '崔老师'}]>

    #高杰写了哪些书
    # obj = models.Book.objects.filter(authors__name='高杰').values('title')
    # print(obj)
    # obj = models.Author.objects.filter(name='高杰').values('book__title')
    # print(obj)

    #进阶的
    # B哥出版社 出版的书的名称以及作者的名字
    # obj = models.Book.objects.filter(publishs__name='B哥出版社').values('title','authors__name')
    # print(obj)
    #<QuerySet [{'title': '李帅的床头故事', 'authors__name': '高杰'}, {'title': '李帅的床头故事', 'authors__name': '崔老师'}, {'title': '李帅的床头故事2', 'authors__name': '崔老师'}, {'title': '李帅的床头故事2', 'authors__name': '王涛'}]>
    '''
    SELECT app01_book.title,app01_author.name from app01_publish INNER JOIN app01_book on app01_publish.id=app01_book.publishs_id
	INNER JOIN app01_book_authors on app01_book.nid = app01_book_authors.book_id  INNER JOIN app01_author
		ON app01_author.id = app01_book_authors.author_id where app01_publish.name='B哥出版社';
    :param request:
    :return:
    '''

    # obj = models.Publish.objects.filter(name='B哥出版社').values('book__title','book__authors__name')
    # print(obj)

    # obj = models.Author.objects.filter(book__publishs__name='B哥出版社').values('name','book__title')
    # print(obj)

    # authorDetail author book publish
    # 手机号以4开头的作者出版过的所有书籍名称以及出版社名称
    # ret = models.AuthorDetail.objects.filter(telephone__startswith='4').values('author__book__title','author__book__publishs__name')
    # print(ret)
    #QuerySet [{'author__book__title': '李帅的床头故事', 'author__book__publishs__name': 'B哥出版社'}, {'author__book__title': '李帅的床头故事2', 'author__book__publishs__name': 'B哥出版社'}]>


    #查询一下B哥出版社出版了哪些书
    # obj = models.Publish.objects.filter(name='B哥出版社').first()
    # print(obj.xx.all())
```

聚合

```

    from django.db.models import Avg,Max,Min,Sum,Count

    # 计算所有图书的平均价格
    # obj = models.Book.objects.all().aggregate(a=Avg('price'),m=Max('price')) #aggregate()是QuerySet 的一个终止子句,得到的是个字典.
    # print(obj['m'] - 2) #{'price__avg': 2.833333}

```



# 今日内容回顾

## 分组

```
annotate

# models.Publish.objects.annotate(a=Avg('book__price')).values('a')

# models.Book.objects.values('publish_id','id').annotate(a=Avg('price')) {'pulish_id':1,'a':11.11}

```

F查询和Q查询

```
from django.db.models import F,Q

F  针对自己单表中字段的比较和处理
models.Book.objects.filter(good__gt=F('comment')*2)
models.Book.objects.all().update(price=F('price')+1)

Q    &  |  非~
filter(Q(xx=11)|Q(ss=22)&Q(oo=33))
filter(Q(Q(xx=11)|Q(ss=22))&Q(oo=33))  &优先级高
filter(Q(Q(xx=11)|Q(ss=22))&Q(oo=33),name='dd')  
```

执行原生sql(了解)

```
models.Publish.objects.raw('原生sql')

from django.db import connection
cursor = connection.cursor()
cursor.excute(sql,[1,])
cursor.fetchall()
```

展示sql的

```
models.Book.objects.filter(good__gt=F('comment')*2)
from django.db import connection
print(connection.queries)

```








































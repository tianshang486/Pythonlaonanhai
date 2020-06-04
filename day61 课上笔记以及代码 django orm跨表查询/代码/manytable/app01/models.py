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
    publishs=models.ForeignKey(to="Publish",related_name='xx')

    authors=models.ManyToManyField(to='Author')

    def __str__(self):
        return self.title

# class BookToAuthor(models.Model):
#     book_id = models.ForeignKey(to='Book')
#     author_id = models.ForeignKey(to='Author')
#     # xx = models.CharField(max_length=12)









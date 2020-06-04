from django.shortcuts import render,HttpResponse
from app01 import models
# Create your views here.

def query(request):
    #查询
    # 一对一
    # 1. 查询崔老师的电话号
    # 方式1  正向查询
    # obj = models.Author.objects.filter(name='崔老师').values('authorDetail__telephone')
    # print(obj) #<QuerySet [{'authorDetail__telephone': '444'}]>
    #方式2  反向查询
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
    from django.db.models import Avg,Max,Min,Sum,Count

    # 计算所有图书的平均价格
    # obj = models.Book.objects.all().aggregate(a=Avg('price'),m=Max('price'))
    # print(obj['m'] - 2) #{'price__avg': 2.833333}



    return HttpResponse('ok')






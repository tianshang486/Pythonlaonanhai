from django.shortcuts import render,HttpResponse,redirect
from app01 import models
from django.urls import reverse

# Create your views here.

# def query(request):
#
#     # objs = models.Book.objects.filter(publish='太白出版社',price__gt=200)
#     # objs = models.Book.objects.filter(pub_date__year__lt=1985,title__startswith='w')
#     #价格为220,240,250的书籍名称以及出版社名称
#     # objs = models.Book.objects.filter(price__in=[220,240,250]).values('title','publish')
#
#     objs = models.Book.objects.filter(publish='太白出版社').values('price').order_by('price').distinct()
#     print(objs)
#
#     return HttpResponse('ok')


def books(request):
    all_objs = models.Book.objects.all()
    # print(reverse('books')) # -- /books/
    print(reverse('delete_book',args=(71,))) #/delete_book/71/
    return render(request,'books.html',{'all_objs':all_objs})


def add_book(request):
    if request.method == 'GET':
        return render(request,'add_book.html')

    else:
        print(request.POST)
        #写入数据库
        title = request.POST.get('book_title')
        price = request.POST.get('book_price')
        pub_date = request.POST.get('book_pub_date')
        publish = request.POST.get('book_publish')
        print(pub_date,type(pub_date))

        models.Book.objects.create(
            title=title,
            price=price,
            pub_date=pub_date,
            publish=publish
        )

        # return redirect('/books/')
        return redirect(reverse('books')) #别名反向解析 reverse('别名')


def delele_book(request,book_id):
    models.Book.objects.filter(id=book_id).delete()
    return redirect(reverse('books'))


def edit_book(request,book_id):
    # edit_obj = models.Book.objects.filter(id=book_id).first()

    if request.method == 'GET':
        try:
            edit_obj = models.Book.objects.get(id=book_id)
        except Exception:
            return HttpResponse('别瞎几把改!!')
        # return render(request, 'edit_book.html', {'edit_obj': edit_obj)
        return render(request, 'edit_book.html', {'edit_obj': edit_obj,'book_id':book_id})
    else:

        title = request.POST.get('book_title')
        price = request.POST.get('book_price')
        pub_date = request.POST.get('book_pub_date')
        publish = request.POST.get('book_publish')

        models.Book.objects.filter(id=book_id).update(
            title=title,
            price=price,
            pub_date=pub_date,
            publish=publish,
        )

        # return redirect(reverse('books'))
        return redirect('books')



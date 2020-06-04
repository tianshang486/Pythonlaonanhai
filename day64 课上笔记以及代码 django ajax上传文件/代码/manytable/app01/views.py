from django.shortcuts import render,HttpResponse,redirect
from app01 import models
# Create your views here.
from django.db.models import Avg,Max,Min,Sum,Count,F,Q


# def query(request):
#
#
#     return HttpResponse('ok')


def showbooks(request):

    all_books = models.Book.objects.all()

    return render(request,'showbooks.html',{'all_books':all_books})

def addbooks(request):
    if request.method == 'GET':
        publish_objs = models.Publish.objects.all()
        authors_objs = models.Author.objects.all()
        return render(request,'add_book.html',{'publish_objs':publish_objs,'authors_objs':authors_objs})

    else:
        # print(request.POST)

        authors = request.POST.getlist('authors')
        # print(authors)
        all_data = request.POST.dict()
        # print(all_data)

        del all_data['csrfmiddlewaretoken']
        del all_data['authors']
        print(all_data)
        # title = request.POST.get('book_title')
        # price = request.POST.get('book_price')
        # pubdate = request.POST.get('book_pub_date')
        # publishs = request.POST.get('publishs')
        # # authors = request.POST.get('authors')
        # authors = request.POST.getlist('authors')
        print(all_data)
        new_book_obj = models.Book.objects.create(
            **all_data
        )
        new_book_obj.authors.add(*authors)

        # print(title)
        # print(price)
        # print(pubdate)
        # print(publishs)
        # print(authors)
        return redirect('showbooks')


def editbooks(request,book_id):
    book_obj = models.Book.objects.filter(pk=book_id)
    if request.method == 'GET':
        book_obj = book_obj.first()
        publish_objs = models.Publish.objects.all()
        authors_objs = models.Author.objects.all()

        return render(request,'edit_book.html',{'book_obj':book_obj,'publish_objs':publish_objs,'authors_objs':authors_objs})

    else:
        authors = request.POST.getlist('authors')
        all_data = request.POST.dict()
        del all_data['csrfmiddlewaretoken']
        del all_data['authors']
        print(all_data)
        book_obj.update(**all_data)
        book_obj.first().authors.set(authors)
        return redirect('showbooks')


def deletebooks(request,book_id):
    models.Book.objects.filter(pk=book_id).delete()
    return redirect('showbooks')





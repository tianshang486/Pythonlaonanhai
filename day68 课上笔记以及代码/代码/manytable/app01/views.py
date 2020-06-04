from django.shortcuts import render,HttpResponse,redirect
from app01 import models
# Create your views here.
from django.db.models import Avg,Max,Min,Sum,Count,F,Q
from django import forms

class BookForm(forms.Form):

    title = forms.CharField(
        label='书名',
        max_length=32,
    )
    publishDate = forms.DateField(
        label='出版日期',
        widget=forms.widgets.TextInput(attrs={'type':'date'}),
    )

    price = forms.DecimalField(
        label='价格',
        max_digits=5,
        decimal_places=2
    )  # decimal(16,2)

    # publishs = models.ForeignKey(to="Publish")
    # publishs = forms.ChoiceField(
    #     label='出版社',
    #     choices=[
    #         (1,'清华出版社'),
    #     #         (2,'22期出版社'),
    #     #         (3,'北大出版社'),
    #     #     ],
    #     widget=forms.widgets.Select(),
    #
    # )

    publishs = forms.ModelChoiceField(
        label='出版社',
        queryset=models.Publish.objects.all(),
    )

    authors = forms.ModelMultipleChoiceField(
        label='作者',
        queryset=models.Author.objects.all(),

    )

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class':'form-control'})

def showbooks(request):

    all_books = models.Book.objects.all()

    return render(request,'showbooks.html',{'all_books':all_books})


def addbooks(request):
    if request.method == 'GET':
        book_form_obj = BookForm()
        publish_objs = models.Publish.objects.all()
        authors_objs = models.Author.objects.all()
        return render(request,'add_book.html',{'publish_objs':publish_objs,'authors_objs':authors_objs,'book_form_obj':book_form_obj})

    else:
        book_form_obj = BookForm(request.POST)

        if book_form_obj.is_valid():
            print(book_form_obj.cleaned_data)
            authors = book_form_obj.cleaned_data.pop('authors')
            new_book = models.Book.objects.create(
                **book_form_obj.cleaned_data
            )
            new_book.authors.add(*authors)
            return redirect('showbooks')
            #{'title': '太白的诱惑', 'publishDate': datetime.date(2019, 8, 3), 'price': Decimal('3'), 'publishs': <Publish: B哥出版社>, 'authors': <QuerySet [<Author: 高杰>, <Author: 崔老师>]>}
        else:
            return render(request, 'add_book.html',{'book_form_obj': book_form_obj})
        # # authors = request.POST.getlist('authors')
        # all_data = request.POST.dict()
        #
        # del all_data['csrfmiddlewaretoken']
        # del all_data['authors']
        # print(all_data)
        #
        # new_book_obj = models.Book.objects.create(
        #     **all_data
        # )
        # new_book_obj.authors.add(*authors)

        # return redirect('showbooks')



def editbooks(request,book_id):
    book_obj = models.Book.objects.filter(pk=book_id)
    if request.method == 'GET':
        # book_obj = book_obj.first()
        # publish_objs = models.Publish.objects.all()
        # authors_objs = models.Author.objects.all()

        book_form_obj = BookForm(instance=book_obj.values())

        return render(request,'edit_book.html',{'book_form_obj':book_form_obj})

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



def login(request):

    return render(request,'login.html')

def register(request):

    return render(request,'register.html')


from django.shortcuts import render,HttpResponse,redirect
from app01 import models
# Create your views here.
from django.db.models import Avg,Max,Min,Sum,Count,F,Q
from django import forms

class BookForm(forms.Form):
    # {'title':'xxx'}
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
    )

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

from django.core.exceptions import ValidationError
class BookModelForm(forms.ModelForm):
    # title=forms.CharField(max_length=15,min_length=6)

    class Meta:
        model = models.Book
        # fields=['title',]
        fields='__all__'
        # exclude = ['title',]

        labels = {
            'title':'书名',
            'publishDate':'出版日期',
        }
        widgets = {
            'publishDate':forms.widgets.TextInput(attrs={'type':'date'}),
        }
        error_messages = {
            'title':{'required':'不能为空',},
            'publishDate':{'required':'不能为空',}
        }

    # def clean_title(self):
    #     value = self.cleaned_data.get('title')
    #     if '666' in value:
    #         raise ValidationError('光喊6是不行的！！')
    #     else:
    #         return value
    # def clean(self):
    #     ...

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class':'form-control'})


def addbooks(request):
    if request.method == 'GET':
        book_model_form = BookModelForm()
        return render(request,'add_book.html',{'book_model_form':book_model_form})

    else:
        book_model_form = BookModelForm(request.POST)
        # book_form_obj = BookForm()

        if book_model_form.is_valid():

            # print(book_model_form.cleaned_data)
            # authors = book_form_obj.cleaned_data.pop('authors')
            # new_book = models.Book.objects.create(
            #     **book_form_obj.cleaned_data
            # )
            # new_book.authors.add(*authors)
            book_model_form.save()

            print(book_model_form.cleaned_data)
            return redirect('showbooks')
        else:
            print(book_model_form.errors)
            return render(request, 'add_book.html',{'book_model_form': book_model_form})
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

# @ensure_csrf_cookie
def showbooks(request):

    all_books = models.Book.objects.all()

    return render(request,'showbooks.html',{'all_books':all_books})

def editbooks(request,book_id):
    book_obj = models.Book.objects.filter(pk=book_id)
    book_obj = book_obj.first()
    if request.method == 'GET':

        # publish_objs = models.Publish.objects.all()
        # authors_objs = models.Author.objects.all()

        # book_form_obj = BookForm(book_obj.values()[0]) #麻烦  queryset([{'title':'xx1'}])
        book_model_form = BookModelForm(instance=book_obj)

        return render(request,'edit_book.html',{'book_model_form':book_model_form})

    else:
        # authors = request.POST.getlist('authors')
        # all_data = request.POST.dict()
        # del all_data['csrfmiddlewaretoken']
        # del all_data['authors']
        # print(all_data)
        # book_obj.update(**all_data)
        # book_obj.first().authors.set(authors)
        book_model_form = BookModelForm(request.POST,instance=book_obj) #
        if book_model_form.is_valid():

            book_model_form.save()  #--create  #instance=book_obj  --update
            return redirect('showbooks')
        else:
            return render(request, 'edit_book.html', {'book_model_form': book_model_form})


def deletebooks(request,book_id):
    models.Book.objects.filter(pk=book_id).delete()
    return redirect('showbooks')



def login(request):

    return render(request,'login.html')

def register(request):

    return render(request,'register.html')


from django.views.decorators.csrf import ensure_csrf_cookie

# @ensure_csrf_cookie  #强制给请求对应的响应添加csrftoken这个cookie键值对
def test(request):
    if request.method == 'GET':
        return render(request,'test.html')

    else:
        return HttpResponse('ok')



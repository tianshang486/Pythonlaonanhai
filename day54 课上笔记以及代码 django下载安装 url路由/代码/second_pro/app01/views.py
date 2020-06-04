from django.shortcuts import render,HttpResponse
# Create your views here.

def index(request):
    print(request.method) #'POST' 'GET'
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        # print(request.GET)
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'dazhuang' and password == '123':
            return HttpResponse('登录成功!')
        else:
            return HttpResponse('登录失败!')

#
def year_books(request,year):
    print('>>>>',year)

    # return render(request,'books.html')
    return HttpResponse(year)

# def year_month_books(request,year,month):
#     print(year,month)
#
#     # return render(request,'books.html')
#     return HttpResponse(year+month)
def year_month_books(request,month,year):
    print(year,month)

    # return render(request,'books.html')
    return HttpResponse(year+month)


def books(request,num='10'):
    print(num)
    return HttpResponse(num)

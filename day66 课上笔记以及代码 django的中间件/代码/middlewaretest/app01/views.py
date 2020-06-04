from django.shortcuts import render,HttpResponse,redirect

# Create your views here.


def login(request):

    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('uname')
        password = request.POST.get('pwd')

        if username == 'bge' and password == '666':
            request.session['is_login'] = True
            request.session['username'] = 'chao'
            return  redirect('home')
        else:
            return redirect('login')

def func(f):
    def func1(request,*args,**kwargs):
        is_login = request.session.get('is_login')
        if is_login == True:
            ret = f(request, *args, **kwargs)
            return ret
        else:
            return redirect('login')
    return func1

# @func
def home(request):

    return render(request,'home.html')

# @func
def index(request):
    print('视图函数index')
    def render():
        print('这是render')
        return HttpResponse('这还是render')
    # raise ValueError('index 出错了！！！')
    ret = HttpResponse('index')
    ret.render = render
    return ret
# render(request, 'index.html')

# @func
def logout(request):
    request.session.flush()  #退出就这么一句话
    return redirect('login')







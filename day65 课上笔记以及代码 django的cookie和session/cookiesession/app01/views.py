from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def wraper(f):

    def inner(request,*args,**kwargs):
        is_login = request.COOKIES.get('is_login')
        if is_login == 'True':
            ret = f(request,*args,**kwargs)
            return ret
        else:
            return redirect('login')

    return inner
#
#
# def login(request):
#
#     if request.method == 'GET':
#         return render(request, 'login.html')
#     else:
#         username = request.POST.get('uname')
#         password = request.POST.get('pwd')
#
#         if username == 'bge' and password == '666':
#             ret = redirect('home')
#             ret.set_cookie('is_login',True,10)
#             # ret.delete_cookie('is_login')
#             return ret
#         else:
#             return redirect('login')

# def index(request):
#     ret = HttpResponse('ok')
#     ret.set_cookie('k1','v1')
#     return ret

# def index(request):
#     is_login = request.COOKIES.get('is_login')
#     print(is_login,type(is_login))
#     if is_login == 'True':
#         return render(request,'index.html')
#     else:
#         return redirect('login')

# @wraper
# def index(request):
#     return render(request,'index.html')
#
#
# @wraper
# def home(request):
#     return render(request,'home.html')

# def home(request):
#     print(request.COOKIES)
#     is_loign = request.COOKIES.get('is_login')
#     if is_loign == 'True':
#         return render(request,'home.html')
#     else:
#         return redirect('login')









###################session#############################
def login(request):

    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('uname')
        password = request.POST.get('pwd')

        if username == 'bge' and password == '666':
            # ret = redirect('home')
            # ret.set_cookie('is_login',True)
            # ret.set_cookie('username','chao')
            # ret.set_cookie('sex','male')
            # return ret
            # from django.conf import settings
            # from django.conf import global_settings
            # settings.SESSION_COOKIE_NAME
            request.session['is_login'] = True
            request.session['username'] = 'chao'
            # 1 生成了session_id : 随机字符串Zdfasdf
            # 2 在cookie里面加上了一个键值对  session_id:Zdfasdf
            # 3 将用户的数据进行了加密,并保存到django-session表里面,
            '''session_key   session_data
              asdfasdf      用户数据加密后的字符串
           '''
            return  redirect('home')

        else:
            return redirect('login')


def home(request):
    print(request.session)
    # is_login =
    # is_login = request.session['is_login']
    is_login = request.session.get('is_login')
    # is_login = request.session['username']
    '''
        1 从cookie里面拿出了session_id:xxx这个随机字符串
        2 去django-session表里面查询到对应的数据
        3 反解加密的用户数据,并获取用户需要的数据

    '''


    print(is_login,type(is_login))  #True
    if is_login == True:

        return render(request,'home.html')
    else:
        return redirect('login')


def logout(request):
    request.session.flush()  #退出就这么一句话
    return redirect('login')





from django.shortcuts import render,HttpResponse,redirect

# Create your views here.



def index(request): #http相关请求信息---封装--HttpRequest对象
    if request.method == 'GET':
        print(request.body)
        print(request.GET)  #给请求提交的数据
        # print(request.META)  # 请求头相关信息
        print(request.path) #/index/ 路径
        print(request.path_info) #/index/ 路径
        print(request.get_full_path())  #/index/?username=dazhuang&password=123
        print(request.body)
        return render(request,'index.html')
    else:

        print(request.body)  # b'username=dazhuang'

        print(request.POST)

        return HttpResponse('男宾三位,拿好手牌!')



def login(request):
    if request.method == 'GET':
        return render(request,'login.html')

    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'taibai' and password == 'dsb':
            # return render(request,'home.html')
            return  redirect('/home/')  #重定向
        else:
            return HttpResponse('滚犊子,赶紧去充钱!!!')

#首页

def n1(f):
    def n2(*args,**kwargs):
        print('请求之前')
        ret = f(*args,**kwargs)
        print('请求之后')
        return ret
    return n2
@n1
def home(request):
    print('home!!!')
    return render(request,'home.html')



from django.views import View
from django.utils.decorators import method_decorator

# @method_decorator(n1,name='get') #方式三
class LoginView(View):
    # GET
    # @method_decorator(n1)  #方式2 给所有方法加装饰器
    def dispatch(self, request, *args, **kwargs):
        # print('请求来啦')
        ret = super().dispatch(request, *args, **kwargs)
        # print('到点了,走人了')
        return ret

    # @method_decorator(n1)  #方式1
    def get(self,request):
        print('get方法执行了')
        return render(request,'login2.html')
    def post(self,request):
        username = request.POST.get('uname')
        password = request.POST.get('pwd')
        print(username,password)
        return HttpResponse('登录成功!')
















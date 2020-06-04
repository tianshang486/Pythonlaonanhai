1. ## 今日内容大纲

   1. 90。自我。
   2.  调整自己，适当听取一些其他人的意见。
   3. 承受压力的能力一定要有所提高。

2. ## 昨天内容回顾以及作业讲解

   1. 匿名函数：一句话函数。 多于内置函数，列表推导式结合。

   2. 内置函数： *** 加key的。min，max，sorted，map，reduce，filter

   3. 闭包：

      1. 内层函数对外层函数非全局变量的使用。
      2. 一定要存在嵌套函数中。
      3. 作用：保证数据安全。自由变量不会再内存中消失，而且全局还引用不到。

      

3. ## 今日内容

   1. 开放封闭原则：

      ```
      装饰器：装饰，装修，房子就可以住，如果装修，不影响你住，而且体验更加，让你生活中增加了很多功能：洗澡，看电视，沙发。
      器：工具。
      开放封闭原则：
      开放：对代码的拓展开放的， 更新地图，加新枪，等等。
      封闭：对源码的修改是封闭的。闪躲用q。就是一个功能，一个函数。 别人赤手空拳打你，用机枪扫你，扔雷.....这个功能不会改变。
      
      装饰器：完全遵循开放封闭原则。
      装饰器： 在不改变原函数的代码以及调用方式的前提下，为其增加新的功能。
      装饰器就是一个函数。
      ```

   2. 装饰器的初识：

      + 版本一： 大壮 写一些代码测试一下index函数的执行效率。

      ```
      
      import time
      # def index():
      #     '''有很多代码.....'''
      #     time.sleep(2) # 模拟的网络延迟或者代码效率
      #     print('欢迎登录博客园首页')
      #
      # def dariy():
      #     '''有很多代码.....'''
      #     time.sleep(3) # 模拟的网络延迟或者代码效率
      #     print('欢迎登录日记页面')
      
      # print(time.time())  # 格林威治时间。
      # print(111)
      # time.sleep(3)
      # print(222)
      # 版本一有问题： 如果测试别人的代码，必须重新赋值粘贴。
      # start_time = time.time()
      # index()
      # end_time = time.time()
      # print(end_time-start_time)
      #
      # start_time = time.time()
      # dariy()
      # end_time = time.time()
      # print(end_time-start_time)
      #
      #
      # start_time = time.time()
      # # dariy()
      # end_time = time.time()
      # print(end_time-start_time)
      
      
      ```

      + 版本二：利用函数，解决代码重复使用的问题

        ```
        import time
        def index():
            '''有很多代码.....'''
            time.sleep(2) # 模拟的网络延迟或者代码效率
            print('欢迎登录博客园首页')
        # index()
        def dariy():
            '''有很多代码.....'''
            time.sleep(3) # 模拟的网络延迟或者代码效率
            print('欢迎登录日记页面')
        
        def timmer(f):  # f= index
            start_time = time.time()
            f()  # index()
            end_time = time.time()
            print(f'测试本函数的执行效率{end_time-start_time}')
        timmer(index)
        
        版本二还是有问题： 原来index函数源码没有变化，给原函数添加了一个新的功能测试原函数的执行效率的功能。
        满足开放封闭原则么？原函数的调用方式改变了。
        
        
        ```

      + 版本三：不能改变原函数的调用方式。

        ```
        # import time
        # def index():
        #     '''有很多代码.....'''
        #     time.sleep(2) # 模拟的网络延迟或者代码效率
        #     print('欢迎登录博客园首页')
        #
        # def timmer(f):  # f = index  (funciton index123)
        #     def inner():  # inner :(funciton inner123)
        #         start_time = time.time()
        #         f()  # index() (funciton index123)
        #         end_time = time.time()
        #         print(f'测试本函数的执行效率{end_time-start_time}')
        #     return inner  # (funciton inner123)
        # timmer(index)  # index()
        # ret = timmer(index)  # inner
        # ret()  # inner()
        # index = timmer(index)  # inner (funciton inner123)
        # index()  # inner()
        # def func():
        #     print('in func')
        #
        # def func1():
        #     print('in func1')
        #
        # # func()
        # # func1()
        # func()
        # func = 666
        # func(0)
        
        ```

      + 版本四：具体研究

        ```
        import time
        def index():
            '''有很多代码.....'''
            time.sleep(2) # 模拟的网络延迟或者代码效率
            print('欢迎登录博客园首页')
        
        def timmer(f):
            f = index
            # f = <function index at 0x0000023BA3E8A268>
            def inner():
                start_time = time.time()
                f()
                end_time = time.time()
                print(f'测试本函数的执行效率{end_time-start_time}')
            return inner
        
        index = timmer(index)
        index()
        ```

      + 版本五：python做了一个优化；提出了一个语法糖的概念。 标准版的装饰器

        ```
        import time
        # timmer装饰器
        def timmer(f):
            def inner():
                start_time = time.time()
                f()
                end_time = time.time()
                print(f'测试本函数的执行效率{end_time-start_time}')
            return inner
        
        # @timmer # index = timmer(index)
        def index():
            '''有很多代码.....'''
            time.sleep(0.6) # 模拟的网络延迟或者代码效率
            print('欢迎登录博客园首页')
            return 666
        ret = index()
        print(ret)
        
        def dariy():
            '''有很多代码.....'''
            time.sleep(3) # 模拟的网络延迟或者代码效率
            print('欢迎登录日记页面')
        dariy()
        # index = timmer(index)
        # index()
        # dariy = timmer(dariy)  @timmer
        dariy()
        
        
        ```

      + 版本六：被装饰函数带返回值

        ```
        
        import time
        # timmer装饰器
        def timmer(f):
            # f = index
            def inner():
                start_time = time.time()
                # print(f'这是个f():{f()}!!!') # index()
                r = f()
                end_time = time.time()
                print(f'测试本函数的执行效率{end_time-start_time}')
                return r
            return inner
        
        @timmer # index = timmer(index)
        def index():
            '''有很多代码.....'''
            time.sleep(0.6) # 模拟的网络延迟或者代码效率
            print('欢迎登录博客园首页')
            return 666
        # 加上装饰器不应该改变原函数的返回值，所以666 应该返回给我下面的ret，
        # 但是下面的这个ret实际接收的是inner函数的返回值，而666返回给的是装饰器里面的
        # f() 也就是 r,我们现在要解决的问题就是将r给inner的返回值。
        ret = index()  # inner()
        print(ret)
        
        ```

      + 版本七：被装饰函数带参数

        ```
        import time
        # timmer装饰器
        def timmer(f):
            # f = index
            def inner(*args,**kwargs):
                #  函数的定义：* 聚合  args = ('李舒淇',18)
                start_time = time.time()
                # print(f'这是个f():{f()}!!!') # index()
                r = f(*args,**kwargs)
                # 函数的执行：* 打散：f(*args) --> f(*('李舒淇',18))  --> f('李舒淇',18)
                end_time = time.time()
                print(f'测试本函数的执行效率{end_time-start_time}')
                return r
            return inner
        
        @timmer # index = timmer(index)
        def index(name):
            '''有很多代码.....'''
            time.sleep(0.6) # 模拟的网络延迟或者代码效率
            print(f'欢迎{name}登录博客园首页')
            return 666
        index('纳钦')  # inner('纳钦')
        
        @timmer
        def dariy(name,age):
            '''有很多代码.....'''
            time.sleep(0.5) # 模拟的网络延迟或者代码效率
            print(f'欢迎{age}岁{name}登录日记页面')
        dariy('李舒淇',18)  # inner('李舒淇',18)
        
        ```

        ```
        标准版的装饰器；
        
        def wrapper(f):
            def inner(*args,**kwargs):
                '''添加额外的功能：执行被装饰函数之前的操作'''
                ret = f(*args,**kwargs)
                ''''添加额外的功能：执行被装饰函数之后的操作'''
                return ret
            return inner
        
        ```

   3. 装饰器的应用

      ```
      # 装饰器的应用：登录认证
      # 这周的周末作业：模拟博客园登录的作业。装饰器的认证功能。
      
      
      
      def login():
          pass
      
      
      def register():
          pass
      
      
      status_dict = {
          'username': None,
          'status': False,
      }
      
      def auth(f):
          '''
          你的装饰器完成：访问被装饰函数之前，写一个三次登录认证的功能。
          登录成功：让其访问被装饰得函数，登录没有成功，不让访问。
          :param f:
          :return:
          '''
          def inner(*args,**kwargs):
              '''访问函数之前的操作，功能'''
              if status_dict['status']:
                  ret = f(*args,**kwargs)
                  '''访问函数之后的操作，功能'''
                  return ret
              else:
                  username = input('请输入用户名').strip()
                  password = input('请输入密码').strip()
                  if username == 'taibai' and password == '123':
                      print('登录成功')
                      status_dict['username'] = username
                      status_dict['status'] = True
                      ret = f(*args, **kwargs)
                      return ret
                  else:
                      print('登录失败')
          return inner
      @auth  # article = auth(article)
      def article():
          print('欢迎访问文章页面')
      @auth
      def comment():
          print('欢迎访问评论页面')
      @auth
      def dariy():
          print('欢迎访问日记页面')
      
      article()  # inner()
      comment()  #inner()
      dariy()
      ```

      

4. ## 今日总结

5. ## 预习内容

预习内容我会以md文件发到群里。


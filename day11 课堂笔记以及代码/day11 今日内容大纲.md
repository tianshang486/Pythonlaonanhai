1. ## 今日内容大纲

   1. global nonlocal
   2. 函数名的运用
   3. 新特性：格式化输出
   4. 迭代器：
      + 可迭代对象
      + 获取对象的方法
      + 判断一个对象是否是可迭代对象
      + 小结
      + 迭代器
      + 迭代器的定义
      + 判断一个对象是否是迭代器
      + 迭代器的取值
      + 可迭代对象如何转化成迭代器
      + while循环模拟for循环机制
      + 小结
      + 可迭代对象与迭代器的对比

2. ## 昨日内容回顾以及作业讲解

   1. 函数的参数：

      1. 实参角度：位置参数，关键字参数，混合参数。
      2. 形参角度：位置参数，默认参数，仅限关键字参数，万能参数。
      3. 形参角度参数顺序：位置参数，*args, 默认参数,仅限关键字参数，**kwargs.

   2. *的魔性用法：

      + 函数的定义时：代表聚合。
      + 函数的调用时：代表打散。

   3. python中存在三个空间：

      + 内置名称空间：存储的内置函数：print,input.......
      + 全局名称空间：py文件，存放的是py文件（除去函数，类内部的）的变量，函数名与函数的内存地址的关系。
      + 局部名称空间：存放的函数内部的变量与值的对应关系。

   4. 加载顺序：内置名称空间，全局名称空间, 局部名称空间（执行函数时）。

   5. 取值顺序：就近原则。LEGB.

      1. 局部作用域只能引用全局变量，不能修改。

         ```
         name = 'alex'
         def func():
         	name = name + 'sb'
         ```

   6. 作用域：

      + 全局作用域：内置名称空间 + 全局名称空间。
      + 局部作用域：局部名称空间。

   7. 函数的嵌套

   8. globals() locals()

      

   

   

3. ## 今日内容

   1. global nonlocal

      + 补充：

        默认参数的陷阱

        ```python
        # 默认参数的陷阱：
        # def func(name,sex='男'):
        #     print(name)
        #     print(sex)
        # func('alex')
        
        # 陷阱只针对于默认参数是可变的数据类型：
        # def func(name,alist=[]):
        #     alist.append(name)
        #     return alist
        #
        # ret1 = func('alex')
        # print(ret1,id(ret1))  # ['alex']
        # ret2 = func('太白金星')
        # print(ret2,id(ret2))  # ['太白金星']
        
        # 如果你的默认参数指向的是可变的数据类型，那么你无论调用多少次这个默认参数，都是同一个。
        
        # def func(a, list=[]):
        #     list.append(a)
        #     return list
        # print(func(10,))  # [10,]
        # print(func(20,[]))  # [20,]
        # print(func(100,))  # [10,100]
        # l1 = []
        # l1.append(10)
        # print(l1)
        # l2 = []
        # l2.append(20)
        # print(l2)
        # l1.append(100)
        # print(l1)
        #
        # def func(a, list= []):
        #     list.append(a)
        #     return list
        # ret1 = func(10,)  # ret = [10,]
        # ret2 = func(20,[])  # [20,]
        # ret3 = func(100,)  # ret3 = [10,100]
        # print(ret1)  # [10,]  [10,100]
        # print(ret2)  # 20,]  [20,]
        # print(ret3)  # [10,100]  [10,100]
        
        ```

        局部作用域的坑：

        ```python
        # 默认参数的陷阱：
        # def func(name,sex='男'):
        #     print(name)
        #     print(sex)
        # func('alex')
        
        # 陷阱只针对于默认参数是可变的数据类型：
        # def func(name,alist=[]):
        #     alist.append(name)
        #     return alist
        #
        # ret1 = func('alex')
        # print(ret1,id(ret1))  # ['alex']
        # ret2 = func('太白金星')
        # print(ret2,id(ret2))  # ['太白金星']
        
        # 如果你的默认参数指向的是可变的数据类型，那么你无论调用多少次这个默认参数，都是同一个。
        
        # def func(a, list=[]):
        #     list.append(a)
        #     return list
        # print(func(10,))  # [10,]
        # print(func(20,[]))  # [20,]
        # print(func(100,))  # [10,100]
        # l1 = []
        # l1.append(10)
        # print(l1)
        # l2 = []
        # l2.append(20)
        # print(l2)
        # l1.append(100)
        # print(l1)
        #
        # def func(a, list= []):
        #     list.append(a)
        #     return list
        # ret1 = func(10,)  # ret = [10,]
        # ret2 = func(20,[])  # [20,]
        # ret3 = func(100,)  # ret3 = [10,100]
        # print(ret1)  # [10,]  [10,100]
        # print(ret2)  # 20,]  [20,]
        # print(ret3)  # [10,100]  [10,100]
        
        ```

        global nonlocal

        ```python
        global
        1, 在局部作用域声明一个全局变量。
        name = 'alex'
        
        def func():
            global name
            name = '太白金星'
            # print(name)
        func()
        print(name)
        
        
        def func():
            global name
            name = '太白金星'
        # print(name)
        print(globals())
        func()
        # print(name)
        print(globals())
        
        2. 修改一个全局变量
        count = 1
        def func():
            # print(count)
            global count
            count += 1
        print(count)
        func()
        print(count)
        
        
        nonlocal
        
        1. 不能够操作全局变量。
        count = 1
        def func():
            nonlocal count
            count += 1
        func()
        2. 局部作用域：内层函数对外层函数的局部变量进行修改。
        
        def wrapper():
            count = 1
            def inner():
                nonlocal count
                count += 1
            print(count)
            inner()
            print(count)
        wrapper()
        ```

        

   2. 函数名的运用

      ```python
      # def func():
      #     print(666)
      #
      # # func()
      # # 1. 函数名指向的是函数的内存地址。
      # # 函数名 + ()就可以执行次函数。
      # # a = 1
      # # a()
      # # func()
      # # a = {'name': 'alex'}
      # # b = {'age' : 18}
      # # a = 1
      # # b = 2
      # # print(a + b)
      # print(func,type(func))  # <function func at 0x000001BA864E1D08>
      # func()
      
      # 2, 函数名就是变量。
      # def func():
      #     print(666)
      
      # a = 2
      # b = a
      # c = b
      # print(c)
      # f = func
      # f1 = f
      # f2 = f1
      # f()
      # func()
      # f1()
      # f2()
      #
      # def func():
      #     print('in func')
      #
      # def func1():
      #     print('in func1')
      #
      # func1 = func
      # func1()
      # a = 1
      # b = 2
      # a = b
      # print(a)
      
      # 3. 函数名可以作为容器类数据类型的元素
      
      # def func1():
      #     print('in func1')
      #
      # def func2():
      #     print('in func2')
      #
      # def func3():
      #     print('in func3')
      # # a = 1
      # # b = 2
      # # c = 3
      # # l1 = [a,b,c]
      # # print(l1)
      # l1 = [func1,func2,func3]
      # for i in l1:
      #     i()
      
      # 4. 函数名可以作为函数的参数
      
      # def func(a):
      #     print(a)
      #     print('in func')
      # b = 3
      # func(b)
      # print(func)
      
      # def func():
      #     print('in func')
      #
      # def func1(x):
      #     x()  # func()
      #     print('in func1')
      #
      # func1(func)
      
      # 5. 函数名可以作为函数的返回值
      def func():
          print('in func')
      
      def func1(x): # x = func
          print('in func1')
          return x
      
      ret = func1(func)  # func
      ret()  # func()
      
      ```

      

   3. 新特性：格式化输出

      ```python
      # %s format
      # name = '太白'
      # age = 18
      # msg = '我叫%s,今年%s' %(name,age)
      # msg1 = '我叫{},今年{}'.format(name,age)
      
      # 新特性：格式化输出
      # name = '太白'
      # age = 18
      # msg = f'我叫{name},今年{age}'
      # print(msg)
      
      # 可以加表达式
      # dic = {'name':'alex','age': 73}
      # msg = f'我叫{dic["name"]},今年{dic["age"]}'
      # print(msg)
      
      # count = 7
      # print(f'最终结果：{count**2}')
      # name = 'barry'
      # msg = f'我的名字是{name.upper()}'
      # print(msg)
      
      # 结合函数写：
      def _sum(a,b):
          return a + b
      
      msg = f'最终的结果是：{_sum(10,20)}'
      print(msg)
      # ! , : { } ;这些标点不能出现在{} 这里面。
      
      ```

      优点：

      1. 结构更加简化。

      2. 可以结合表达式，函数进行使用。

      3. 效率提升很多。

         

   4. 迭代器：

      - 可迭代对象

        字面意思：对象？python中一切皆对象。一个实实在在存在的值，对象。

        可迭代？：更新迭代。重复的，循环的一个过程，更新迭代每次都有新的内容，

        可以进行循环更新的一个实实在在值。

        专业角度：可迭代对象？ 内部含有`'__iter__'`方法的对象，可迭代对象。

        目前学过的可迭代对象？str list tuple dict set range 文件句柄

      - 获取对象的所有方法并且以字符串的形式表现：dir()

      - 判断一个对象是否是可迭代对象

        ```
        s1 = 'fjdskl'
        # l1 = [1,2,3]
        # # print(dir(s1))
        # print(dir((l1)))
        # print('__iter__' in dir(s1))
        # print('__iter__' in dir(range(10)))
        ```

      - 小结

        - 字面意思：可以进行循环更新的一个实实在在值。

        - 专业角度： 内部含有`'__iter__'`方法的对象，可迭代对象。

        - 判断一个对象是不是可迭代对象： `'__iter__'`  in dir(对象)

        - str list tuple dict set range 

        - 优点：

          1. 存储的数据直接能显示，比较直观。
          2. 拥有的方法比较多，操作方便。

        - 缺点：

          1. 占用内存。

          2. 不能直接通过for循环，不能直接取值（索引，key）。

             

      - 迭代器

      - 迭代器的定义

        - 字面意思：更新迭代，器：工具：可更新迭代的工具。
        - 专业角度：内部含有`'__iter__'`方法并且含有`'__next__'`方法的对象就是迭代器。
        - 可以判断是否是迭代器：`'__iter__'` and `'__next__'` 在不在dir(对象)

      - 判断一个对象是否是迭代器  

        ```python
        with open('文件1',encoding='utf-8',mode='w') as f1:
            print(('__iter__' in dir(f1)) and ('__next__' in dir(f1)))
        ```

        

      - 迭代器的取值  

        ```python
        s1 = 'fjdag'
        obj = iter(s1)  # s1.__iter__()
        # print(obj)
        # print(next(obj)) # print(obj.__next__())
        # print(next(obj)) # print(obj.__next__())
        # print(next(obj)) # print(obj.__next__())
        # print(next(obj)) # print(obj.__next__())
        # print(next(obj)) # print(obj.__next__())
        # print(next(obj)) # print(obj.__next__())
        
        # l1 = [11,22,33,44,55,66]
        # obj = iter(l1)
        # print(next(obj))
        # print(next(obj))
        # print(next(obj))
        # print(next(obj))
        # print(next(obj))
        # print(next(obj))
        
        
        ```

        

      - 可迭代对象如何转化成迭代器

        `iter([1,2,3])`

      - while循环模拟for循环机制

        ```python
        l1 = [11,22,33,44,55,66,77,88,99,1111,1133,15652]
        # 将可迭代对象转化成迭代器。
        obj = iter(l1)
        while 1:
            try:
                print(next(obj))
            except StopIteration:
                break
        ```

        

      - 小结

        + 字面意思：更新迭代，器：工具：可更新迭代的工具。
        + 专业角度：内部含有`'__iter__'`方法并且含有`'__next__'`方法的对象就是迭代器。
        + 优点：
          1. 节省内存。
          2. 惰性机制，next一次，取一个值。
        + 缺点：
          + 速度慢。
          + 不走回头路。

      - 可迭代对象与迭代器的对比
        -  可迭代对象是一个操作方法比较多，比较直观，存储数据相对少（几百万个对象，8G内存是可以承受的）的一个数据集。
        - 当你侧重于对于数据可以灵活处理，并且内存空间足够，将数据集设置为可迭代对象是明确的选择。
        - 是一个非常节省内存，可以记录取值位置，可以直接通过循环+next方法取值，但是不直观，操作方法比较单一的数据集。
        - 当你的数据量过大，大到足以撑爆你的内存或者你以节省内存为首选因素时，将数据集设置为迭代器是一个不错的选择。

4. ## 今日总结

   1. 默认参数的坑，作用域的坑  ***
   2. 格式化输出 ***
   3. 函数名的应用。***
   4. 对比：迭代器是什么？ 迭代器的优缺点。可迭代对象转化成迭代器。next取值.  ***

5. ## 明日内容

6. 
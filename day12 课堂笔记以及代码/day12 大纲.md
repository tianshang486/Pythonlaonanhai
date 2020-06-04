1. 今日内容大纲

   1. 毒鸡汤课

      坚持努力。

   2. 生成器

      + yield
      + yield return
      + yield from

   3. 生成器表达式，列表推导式

   4. 内置函数 I

      

2. 昨日内容回顾作业讲解

   1. 可迭代对象：
      + 可以更新迭代的实实在在值。
      + 内部含有`'__iter__'`方法的。
      + str list tuple dict set range 
      + 优点：操作方法多，操作灵活，直观，
      + 缺点：占用内存。
   2. 迭代器：
      + 可以更新迭代的一个工具（数据结构）。
      + 内部含有`'__iter__'``且含有__next__方法的`的。
      + 文件句柄。
      + 优点：节省内存。惰性机制。
      + 缺点：不直观，速度相对慢，操作方法单一，不走回头。

   3. 格式化输出。
   4. 函数名的应用。
   5. 默认参数可变的数据类型坑。作用域的坑。

   

3. 今日内容

   + 生成器

     + 生成器：python社区，生成器与迭代器看成是一种。生成器的本质就是迭代器。唯一的区别：生成器是我们自己用python代码构建的数据结构。迭代器都是提供的，或者转化得来的。
       + 获取生成器的三种方式：
         + 生成器函数。
         + 生成器表达式。
         + python内部提供的一些。
     + 生成器函数获得生成器：

     ```python
     函数
     def func():
         print(111)
         print(222)
         return 3
     ret = func()
     print(ret)
     
     生成器函数
     def func():
         print(111)
         print(222)
         yield 3
         a = 1
         b = 2
         c = a + b
         print(c)
         yield 4
     ret = func()
     # print(ret)
     print(next(ret))
     print(next(ret))
     print(next(ret))
     一个next 对应一个yield
     
     ```

     + yield return

       return：函数中只存在一个return结束函数，并且给函数的执行者返回值。
       yield：只要函数中有yield那么它就是生成器函数而不是函数了。生成器函数中可以存在多个yield，yield不会结束生成器函数，一个yield对应一个next。

     + 吃包子练习题：

       ```python
       def func():
           l1 = []
           for i in range(1,5001):
               l1.append(f'{i}号包子')
           return l1
       ret = func()
       print(ret)
       
       def gen_func():
           for i in range(1,5001):
               yield f'{i}号包子'
       ret = gen_func()
       # [3号包子.]
       for i in range(200):
           print(next(ret))
       
       for i in range(200):
           print(next(ret))
       
       ```

     + yield from

       ```python
       
       def func():
           l1 = [1, 2, 3, 4, 5]
           yield l1
       ret = func()
       print(next(ret))
       
       
       
       def func():
           l1 = [1, 2, 3, 4, 5]
           yield from l1
           '''
           yield 1
           yield 2
           yield 3
           yield 4
           yield 5
           '''
           将l1这个列表变成了迭代器返回。
       ret = func()
       print(next(ret))
       print(next(ret))
       print(next(ret))
       print(next(ret))
       print(next(ret))
       
       ```

       

   + 生成器表达式，列表推导式

     + 用一行代码构建一个比较复杂有规律的列表。

     + 列表推导式：

       + 循环模式：[变量(加工后的变量) for  变量  in  iterable]
       + 筛选模式：[变量(加工后的变量) for  变量  in  iterable if 条件]

     + 循环模式讲解

       练习题：

       

   + 内置函数 I

4. 今日总结

   1. 生成器：***
   2. 生成器函数 yield 
   3. yield与return 区别。yield from
   4. 列表推导式，生成器表达式。 ***
   5. 内置函数：今天讲的内置函数，了解。

5. 

6. 预习内容

   1. lambda表达式。
   2. 内置函数 II.
   3. 闭包。
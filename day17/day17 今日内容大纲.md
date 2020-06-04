1. ## 今日内容大纲

   第一次班委会总结:

   + 微调座位.	

   + 开展运维兴趣班.
   + 培养独立思考问题的能力.
     + 遇到难题 选做题:先思考20分钟左右.关键节点问问思路.
     + 

   1. 自定义模块
   2. 模块是什么?
   3. 为什么要有模块?
      + 什么是脚本?
   4. 模块的分类
   5. import的使用
      + 第一次导入模块执行三件事
      + 被导入模块有独立的名称空间
      + 为模块起别名
      + 导入多个模块
   6. from ... import ...
      + from ... import ...的使用
      + from ... import ... 与import对比
      + 一行导入多个
      + from ... import *
      + 模块循环导入的问题
      + py文件的两种功能
      + 模块的搜索路径
   7. json pickle 模块
   8. hashlib模块

2. ## 具体内容

   1. 自定义模块

   2. 模块是什么?

      抖音: 20万行代码全部放在一个py文件中?

      为什么不行? 

      	1. 代码太多,读取代码耗时太长.
       	2. 代码不容易维护.

      所以我们怎么样?

      一个py文件拆分100文件,100个py文件又有相似相同的功能.冗余. 此时你要将100个py文件中相似相同的函数提取出来, input 功能,print()功能, time.time() os.path.....放在一个文件,当你想用这个功能拿来即用.类似于这个py文件: 常用的相似的功能集合.模块.

      模块就是一个py文件常用的相似的功能集合.

   3. 为什么要有模块?

      + 拿来主义,提高开发效率.
      + 便于管理维护.

      - 什么是脚本?
        - 脚本就是py文件.长期保存代码的文件.

   4. 模块的分类

      1. 内置模块200种左右.Python解释器自带的模块,time os sys hashlib等等.

      2. 第三方模块6000种.一些大牛大神写的,非常好用的. 

         pip install 需要这个指令安装的模块,Beautiful_soup,request,Django,flask 等等.

      3. 自定义模块,自己写的一个py文件.

   5. import的使用

      import 模块 先要怎么样?

      import tbjx  执行一次tbjx这个模块里面的所有代码,

      第一次引用tbjx这个模块,会将这个模块里面的所有代码加载到内存,只要你的程序没有结束,接下来你在引用多少次,它会先从内存中寻找有没有此模块,如果已经加载到内存,就不在重复加载.

      - 第一次导入模块执行三件事  `***`

        - 1. 在内存中创建一个以tbjx命名的名称空间.

          2. 执行此名称空间所有的可执行代码(将tbjx.py文件中所有的变量与值的对应关系加载到这个名称空间).

          3. 通过tbjx. 的方式引用模块里面的代码.

             ```python
             import tbjx
             print(tbjx.name)
             tbjx.read1()
             
             ```

             ![1558409649013](C:\Users\oldboy\AppData\Roaming\Typora\typora-user-images\1558409649013.png)

      - 被导入模块有独立的名称空间   `***`

        ```python
        import tbjx
        # name = 'alex'
        # print(name)
        # print(tbjx.name)
        
        #
        # def read1():
        #     print(666)
        # tbjx.read1()
        #
        
        # name = '日天'
        # tbjx.change()
        # print(name)  # 日天
        # print(tbjx.name)  # barry
        ```

        ![1558409673492](C:\Users\oldboy\AppData\Roaming\Typora\typora-user-images\1558409673492.png)

        ![1558409693895](C:\Users\oldboy\AppData\Roaming\Typora\typora-user-images\1558409693895.png)

      - 为模块起别名  ` **`

        - 1 简单,便捷.

          ```python 
          # import hfjksdahdsafkd as sm
          # print(sm.name)
          ```

          

        - 2,有利于代码的简化.

          ```python
          # 原始写法
          # result = input('请输入')
          # if result == 'mysql':
          #     import mysql1
          #     mysql1.mysql()
          # elif result == 'oracle':
          #     import oracle1
          #     oracle1.oracle()
          # list.index()
          # str.index()
          # tuple.index()
          # 起别名
          # result = input('请输入')
          # if result == 'mysql':
          #     import mysql1 as sm
          # elif result == 'oracle':
          #     import oracle1 as sm
          # ''' 后面还有很多'''
          # sm.db()  # 统一接口,归一化思想
          ```

          

      - 导入多个模块

        ```python
        import time, os, sys  # 这样写不好
        # 应该向以下这种写法:
        import time
        import os
        import sys
        ```

        

   6. from ... import ...

      - from ... import ...的使用

        ```python
        # from tbjx import name
        # from tbjx import read1
        # from tbjx import read2
        # print(name)
        # print(globals())
        # read1()
        ```

        

      - from ... import ... 与import对比  `***`

        1.  from.. import 用起来更方便

           ```python
           from tbjx import name
           print(name)
           ```

           

        2.  from...import 容易与本文件的名字产生冲突.

           ```python
           # 1, 容易产生冲突,后者将前者覆盖
           # name = 'alex'
           # from tbjx import name
           # print(name)
           
           ```

        3. 当前位置直接使用read1和read2,执行时，仍然以tbjx.py文件全局名称空间  `***`

           ```python
           # from tbjx import read1
           #
           # def read1():
           #     print(666)
           
           # name = '大壮'
           # read1()
           # print(globals())
           
           
           from tbjx import change
           name = 'Alex'
           print(name)  # 'Alex'
           change()  # 'barry'
           from tbjx import name
           print(name)
           
           
           ```

           

      - 一行导入多个

        ```python
        from tbjx import name,read1,read2  # 这样不好
        from tbjx import name
        from tbjx import read1
        ```

        

      - from ... import *

      - 模块循环导入的问题

        

      - py文件的两种功能

        py文件的两个功能:

        1. 自己用 脚本
        2. 被别人引用 模块使用

        

      - 模块的搜索路径  ` ***`

      - import sm

        1. 它会先从内存中寻找有没有已经存在的以sm命名的名称空间.
        2. 它会从内置的模块中找. time,sys,os,等等.
        3. 他从sys.path中寻找.

   7. json pickle 模块


   序列化模块: 将一种数据结构(list,tuple,dict ....)转化成特殊的序列.

   为什么存在序列化?

   数据  ----> bytes

   只有字符串类型和bytes可以互换.

   dict,list..... -------> str <--------> bytes  

   数据存储在文件中,str(bytes类型)形式存储,比如字典.

   数据通过网络传输(bytes类型),str 不能还原回去.

   特殊的字符串:序列化.

   序列化模块:

    json模块 ： （**重点**）

   1. 不同语言都遵循的一种数据转化格式，即不同语言都使用的特殊字符串。（比如Python的一个列表[1, 2, 3]利用json转化成特殊的字符串，然后在编码成bytes发送给php的开发者，php的开发者就可以解码成特殊的字符串，然后在反解成原数组(列表): [1, 2, 3]）
   2. json序列化只支持部分Python数据结构：dict,list, tuple,str,int, float,True,False,None

     

   ​    pickle模块：

   1. 只能是Python语言遵循的一种数据转化格式，只能在python语言中使用。
   2. 支持Python所有的数据类型包括实例化对象。

   

   json: 将数据结构转化成特殊的字符串.并且可以反转回去.

   两对四种方法.

   网络传输:

   dumps loads

   

   

   8. hashlib模块

      包含很多的加密算法. MD5, sha1 sha256 sha512......

      用途:

      1. 密码加密.不能以明文的形式存储密码.密文的形式.
      2. 文件的校验.

      

      用法:

      1. 将bytes类型字节 转化成 固定长度的16进制数字组成的字符串.

      2. 不同的bytes利用相同的算法(MD5)转化成的结果一定不同.

      3. 相同的bytes利用相同的算法(MD5)转化成的结果一定相同.

      4. hashlib算法不可逆(MD5中国王晓云破解了).

         

      

   





1. ## 今日总结

   1. import 三件事, import的名字如果调用? 模块名.的方式调用.

   2. from ... import ... 容易产生冲突,独立的空间.

   3. `__name__`问题

   4. 模块的搜索路径

      内存 内置 sys.path

   5. 序列化模块: 
      1. json最最常用(两对四个方法就行)  一定要掌握
      2. pickle(两对四个方法就行)  尽量掌握

   6. hashlib
      1. 密码的加密 ,文件的校验

2. ## 预习内容
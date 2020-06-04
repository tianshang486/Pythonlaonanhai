今日内容大纲：

1. cpu 内存 硬盘 操作系统

   ​	cpu:计算机的运算和计算中心,相当于人类大脑.飞机
   ​	内存：暂时存储数据，临时加载数据应用程序，4G，8G,16G，32G
   ​			速度快，高铁，断电即消失。造价很高
   ​	硬盘：磁盘，长期存储数据。D盘，E盘，文件，片儿，音频等等。500G，1T。
   ​			汽车，造价相对低。
   ​	操作系统：一个软件，连接计算机的硬件与所有软件之间的一个软件。

2. python的发展与应用

3. python的历史

   ​	Python崇尚优美、清晰、简单，

   ​	python2x，python3x源码区别：

   ​	python2x:  

   ​		C，java，大牛： 重复代码多，冗余，代码不规范。

   ​	python3x: 源码规范，清晰，简单。

4. python的编程语言分类（**重点**）

   ​	if 3 > 2:

   ​	编译型：

   ​		将代码一次性全部编译成二进制，然后再执行。

   ​		优点：执行效率高。

   ​		缺点：开发效率低，不能跨平台。

   ​		代表语言：C

   ​	解释型：

   ​		逐行解释成二进制，逐行运行。

   ​		优点：开发效率高，可以跨平台。

   ​		缺点：执行效率低。

   ​		代表语言：python。

   

5. python的优缺点

6. python的种类

   + Cpython：官方推荐解释器。可以转化成C语言能识别的字节码。
   + Jpython: 可以转化成Java语言能识别的字节码。
   + Ironpython：可以转化成.net语言能识别的字节码
   + pypy: 动态编译。

7. 安装python解释器流程：

   1. 官网查找版本

      ![1556331110757](C:\Users\oldboy\AppData\Roaming\Typora\typora-user-images\1556331110757.png)

   2.  选择版本

      ![1556331217364](C:\Users\oldboy\AppData\Roaming\Typora\typora-user-images\1556331217364.png)

   3. ![1556331309571](C:\Users\oldboy\AppData\Roaming\Typora\typora-user-images\1556331309571.png)

   4. ![1556331333795](C:\Users\oldboy\AppData\Roaming\Typora\typora-user-images\1556331333795.png)

   5. ![1556331389970](C:\Users\oldboy\AppData\Roaming\Typora\typora-user-images\1556331389970.png)

   6. ![1556331442709](C:\Users\oldboy\AppData\Roaming\Typora\typora-user-images\1556331442709.png)

   7. ![1556331526244](C:\Users\oldboy\AppData\Roaming\Typora\typora-user-images\1556331526244.png)

   8. ![1556331726369](C:\Users\oldboy\AppData\Roaming\Typora\typora-user-images\1556331726369.png)

   9. 手动添加环境变量

      ![1556331797490](C:\Users\oldboy\AppData\Roaming\Typora\typora-user-images\1556331797490.png)

   10. ![1556331813409](C:\Users\oldboy\AppData\Roaming\Typora\typora-user-images\1556331813409.png)

   11. ![1556331927445](C:\Users\oldboy\AppData\Roaming\Typora\typora-user-images\1556331927445.png)
   12. ![1556331996321](C:\Users\oldboy\AppData\Roaming\Typora\typora-user-images\1556331996321.png)

8. 运行第一个python代码。

   1. ![1556333109426](C:\Users\oldboy\AppData\Roaming\Typora\typora-user-images\1556333109426.png)
   2. 

9. 变量 (**重点**)

    1. ![1556334246127](C:\Users\oldboy\AppData\Roaming\Typora\typora-user-images\1556334246127.png)

    why：

    ​	

    ```python
    print(1+2+3+4+5)
    
    print((1+2+3+4+5)*3/2)
    
    print((((1+2+3+4+5)*3/2)+100)/24)
    
    x = 1+2+3+4+5
    y = x*3/2
    z = (y + 100) / 24
    print(x,y,z)
    
    x8 = 100  # True
    b__ = 12  # True
    4g = 32  # False
    _ = 11  # True
    *r = 12  # False
    r3t4 = 10  # True
    t_ = 66  # True
    
    # 变量的小高级：
    age1 = 18
    age2 = age1
    age3 = age2
    age2 = 12
    # print(age1,age2,age3)  # 18 12 18 
    
    ```

    

    

    what：x y z 变量：代指一些内容、

    how：

    + 变量全部由数字，字母下划线任意组合。
    + 不能以数字开头。 
    + 不能是python的关键字。
      + ['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']
    + 要具有描述性。name= '太白金星' sex
    + 不能使用中文。
    + 不能过长。
    + 推荐
      + 驼峰体：AgeOfOldboy = 73
      + 下划线：age_of_oldboy = 73
      + ![1556335785418](C:\Users\oldboy\AppData\Roaming\Typora\typora-user-images\1556335785418.png)

    

    

    

    where：

    ​	代指一些复杂过长的数据。

    content = 'sfkdsjalfjdslfksdjkfhsdajkfhsdjkfshdfsdkfhsdkfjsldakfjsdaflsdafjshdafjkdsfhkjsdlf

    fskdfhsdkfhsdkjfhsdkjfhskdfhsdkjfhsdkfkhsdflsafksjdfhskdajfhskdjfhskda'

    

10. 常量

    why :生活中一直不变的：π，身份证号码，历史发生的时间

    what: 常量：一直不变的量。python中没有真正的常量，为了应和其他语言的口味，全部大写的变量称之为常量。

    how： 将变量全部大写，放在文件的最上面。

    where： 设置一些不变的量 ：身份证号，id，

    ​	BIRTH_OF_CHINA = 1949

    ```python
    # 常量
    # 约定俗成不能改变
    NAME = '太白'
    # print(NAME)
    ```

    

11. 注释（**重点**）

     why：文言文中对一些晦涩难懂的成语或者经典的出处 解释说明。便于你理解。

     ​	便于你理解对方的代码，自己的代码。

     what： 注释

     how： 

     ​	单行注释： # 

     ​	多行注释： '''被注释内容'''  """被注释内容"""

     where:

     ​	难以理解的代码后面，加注释。

     ​	函数，类，文件都需要注释，解释说明。

12. 基础数据类型初识（**重点**）

     why: 

     ​	人类接触一些信息会做一些比较精准的划分。数字，汉字，英文......

     ​	100, '中国' 机器是很傻的你要是不给他区分，他是分辨不出来的。

     ​	我们告诉计算机： 

     ​		100 ，102 ，就是数字（int），  + - * / ....

     ​		'中国'，'hello' ，'萨瓦迪卡'  文字，：记录信息，描述信息等等。

     ​		[1, 2, 3, '中国']  列表，他能做他相应的一些操作即可。

     ​		.......  python的基础数据类型。

     ​	int(整型): 1 ，2， 123， ....

        + - * / . 运算

     + ```python
       i = 100
       i1 = 2
       i2 = i*i1
       print(i2)
       ```

       

     ​	str： 凡是用引号引起来的数据就称之为字符串。

     ​	'', "", ''' '''  """ """

     ```python
     # str:
     s1 = 'day01'
     s2 = "Python22期"
     s2 = '''Python22期'''
     
     # 单双引号可以配合使用
     
     # content = 'I am taibai, 18 year old'
     # content = "I'm taibai, 18 year old"
     
     # 三引号：换行的字符串
     msg = '''
     今天我想写首小诗，
     歌颂我的同桌，
     你看他那乌黑的短发，
     好像一只炸毛鸡。
     '''
     # print(msg)
     
     # str 可以否加减乘除? + *
     # str + str  *** 字符串的拼接
     s1 = 'alex'
     s2 = 'sb'
     # print(s1 + s2)
     
     
     # str * int
     # s1 = '坚强'
     # print(s1*8)
     ```

     

     ​	bool ：True False

     ​	判断变量指向的是什么数据类型？ type()

     ```pyton
     # bool : True False
     # print(2 > 1)
     # print(3 < 1)
     # print(True)
     # print('True')
     
     # s1 = '100'
     # s2 = 100
     # print(s1,type(s1))
     # print(s2,type(s2))
     ```

     

13. 用户交互input

    why:	网页上，app 输入账号与密码。

    what： 用户交互input

    how：

    ```python
    # input: 出来的全部都是字符串类型。
    username = input('请输入用户名：')
    password = input('请输入密码：')
    print(username,type(username))
    print(password,type(password))
    ```

    

14. 流程控制语句if

    why:  生活中选择，回家，n条路，你走那条路，取决于心情。

    what: if。

    how：

    + 基本结构：

    + ```
      if 条件:
          结果
          
      # c: if{条件}{结果}
      ```

    1.  单独if

       ```python
       print(111)
       if 2 < 1:
           print(666)
           print(333)
       print(222)
       ```

       

    2. if else 二选一

       ```python 
       s1 = '100'
       i1 = int(s1)
       print(i1,type(l1))
       
       age = input('请输入年龄：')
       if int(age) > 18:
           print('恭喜你，成年了')
       else:
           print('小屁孩儿')
       
       ```

    3. if elif elif .... 多选一

       ```python
       num = int(input('猜点数：'))
       
       if num == 1:
           print('晚上请你吃饭')
       elif num == 3:
           print('一起溜达')
       elif num == 2:
           print('请你大宝剑')
       ```

       

    4. if elif elif .... else 多选一

       ```python
       num = int(input('猜点数：'))
       
       if num == 1:
           print('晚上请你吃饭')
       	
       elif num == 3:
           print('一起溜达')
       	
       elif num == 2:
           print('请你大宝剑')
       else:
           print('太笨了....')
       
       print('组合')
       ```

       

    5. 嵌套的if

       ```python
       
       username = input('请输入用户名：')
       password = input('请输入密码：')
       code = 'qwer'
       your_code = input('请输入验证码：')
       
       if your_code == code:
           if username == 'taibai' and password == '123':
       	    print('登录成功')
           else:
       	    print('账号或者密码错误')
       else:
           print('验证码错误')
       ```



明日讲课：<https://www.cnblogs.com/jin-xin/p/9076242.html>

明日讲课内容这篇博客：<https://www.cnblogs.com/jin-xin/articles/10563881.html>  

​	



每天的计划：

​	默写。

1. 上午讲课：
   + 跟着老师的思路走，说。
   + 自己也要做好截图
   + 不懂就要问。
   + 有人用笔纸记录，因人而异我不建议。
   + 课间：敲代码，讨论题，出去浪。

2. 下午：
   1. 不要看视频。（理论性的内容多，而且是重点，学习相对比较落后了，或者是真的忘了，可以看）
   2. 整理今天的内容，笔记。
      + 参考老师的，有自己的见解，整理一份 md文件。
      + 将老师上午的所有的代码带着脑子敲2~3遍。 （晚上7点之前一定要完成）
   3. 写作业。
      1. 基础练习题必须做完。
      2. 选做题：尝试做。
      3. 面试题：简单的必须做，难的尝试做，第二天必须会做。
   4. 半个小时预习。
   5. 打字慢的同学：金山打字通，练习打字英文字半个小时。160~180字符每分钟。

每周：思维导图（待续）。

每周一个大作业：打分的。






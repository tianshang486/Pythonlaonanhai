1. ## 今日内容大纲

2. ## 昨日内容回顾作业讲解

   + 装饰器：完美的呈现了开放封闭原则。装饰器的本质：闭包。

   + ```python
     def wrapper(f):
     	def inner(*args,**kwargs):
     		"""执行被装饰函数之前的操作"""
     		ret = f(*args,**kwargs)
     		"""执行被装饰函数之后的操作"""
     		return ret
         return inner
     ```

     

3. ## 今日内容

# 自定义模块：

什么是模块：本质就是.py文件，封装语句的最小单位。

自定义模块：实际上就是定义.py,其中可以包含：变量定义，可执行语句，for循环，函数定义等等，他们统称模块的成员。



# 模块的运行方式：

- 脚本方式：直接用解释器执行。或者PyCharm中右键运行。
- 模块方式：被其他的模块导入。为导入它的模块提供资源（变量，函数定义，类定义等）。



# `__name__`属性的使用：

在脚本方式运行时，`__name__`是固定的字符串：`__main__`

在以模块方式被导入时，`__name__`就是本模块的名字。

在自定义模块中对`__name__`进行判断，决定是否执行可执行语句：开发阶段，就执行，使用阶段就不执行。



# 系统导入模块的路径

- 内存中：如果之前成功导入过某个模块，直接使用已经存在的模块
- 内置路径中：安装路径下：Lib
- PYTHONPATH:import时寻找模块的路径。
- sys.path：是一个路径的列表。

如果上面都找不到，就报错。

通过动态修改sys.path的方式将自定义模块添加到sys.path中。

os.path.dirname():获取某个路径的父路径。通常用于获取当前模块的相对路径

```python
import sys
import os
sys.path.append(os.path.dirname(__file__) + '/aa')
```



# 导入模块的多种方式：

- import xxx:导入一个模块的所有成员
- import aaa,bbb:一次性导入多个模块的成员。不推荐这种写法，分开写。
- from xxx import a:从某个模块中导入指定的成员。
- from xxx import a,b,c:从某个模块中导入多个成员。
- from xxx import *:从模块中导入所有成员。



# import xxx 和 from xxx import * 的区别

第一种方式在使用其中成员时，必须使用模块名作为前缀。不容易产生命名冲突。

第二种方式在使用其中成员时，不用使用模块名作为前缀，直接使用成员名即可。但是容易产生命名冲突。在后定义的成员生效（把前面的覆盖了。）



# 怎么解决名称冲突的问题

- 改用import xxx这种方式导入。
- 自己避免使用同名
- 使用别名解决冲突



# 使用别名：alias

给成员起别名，避免名称冲突。

from my_module import age as a

给模块起别名，目的简化书写。

import my_module as m





# from xxx import * 控制成员被导入

默认情况下，所有的成员都会被导入。

`__all__`是一个列表，用于表示本模块可以被外界使用的成员。元素是成员名的字符串。

注意：

`__all__`只是对from xxx import *这种导入方式生效。其余的方式都不生效。



# 相对导入

针对某个项目中的不同模块之间进行导入，称为相对导入。

只有一种格式：

from 相对路径 import xxx

相对路径：包含了点号的一个相对路径。

. 表示的是当前的路径。

..表示的是父路径。

...表示的是父路径的父路径。



```python
# 相对导入同项目下的模块
# from ..z import zz            # 容易向外界暴露zz模块
from ..z.zz import *
```



```python
# 不使用相对导入的方式，导入本项目中的模块
# 通过当前文件的路径找到z的路径
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)) + '/z')
from zz import *
```







# 常用模块：random

此模块提供了和随机数获取相关的方法：

- random.random():获取[0.0,1.0)范围内的浮点数
- random.randint(a,b):获取[a,b]范围内的一个整数
- random.uniform(a,b):获取[a,b)范围内的浮点数
- random.shuffle(x):把参数指定的数据中的元素打乱。参数必须是一个可变的数据类型。
- random.sample(x,k):从x中随机抽取k个数据，组成一个列表返回。









1. ## 今日总结

2. ## 预习内容
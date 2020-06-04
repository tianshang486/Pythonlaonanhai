## 1 今日内容大纲

+ 列表的初识
+ 列表的索引切片
+ 列表的增删改查
+ 列表的嵌套
+ 元组的初识（了解）
+ 元组的简单应用（了解）
+ range

## 2 昨日内容回顾以及作业讲解

+ int str bool 
+ str：s1 = '太白123abc'
  + 索引：
    + s1[0] 
    + s1[-1]
    + s1[:3]
    + s1[:5:2]
    + s1[-1:-4:-1]
    + s1[-1:-6:-2]
  + 常用操作方法：
    + upper lower 
    + startswith endswith
    + split 分割：str---->list
      + 默认按照空格。
      + 可以指定分隔符。
    + strip：默认去除字符串两边的空格，换行符，制表符。
    + isdecimal isalpha  isalnum
    + format 格式化输出
    + count某个元素出现的次数
    + join 连接
    + replace 
    + len() 获取数据的元素个数。
  + for循环

## 3 具体内容

 1. **如何学习python**

    确实非常困难。如何解压？如何学习。

    python，语言，中文，英语。

    华尔街英语：母式英语。

    中国人教的英语：在国外很难生存。

    听说读写练。

    ​	input 							output

    ​	听									写（练）

    ​	读                                    说

    

    2岁的孩子：

​			听，							     说    											纠正

​	

​		你们现在的比例：
​				听：3.5 + 2 +  1 = 6.5        练：2~3.								纠正：0.5

​		120行 *120:14400 

​		1.  上午要认真听！！！

​		2. 下午不要听视频，抓紧时间放在练习代码上，写作业，代码251行。

​		3. 讨论（下周开始）。



2. **列表的初识**

   + why：int bool str：'123 True 太白'
     + str： 存储少量的数据。
     + str：切片还是对其进行任何操作，获取的内容全都是str类型。存储的数据单一。

   + what：list
     + l1 = [100, 'alex',True,[1, 2, 3]] 承载任意数据类型，存储大量的数据。
     + python常用的容器型数据类型。list 列表，其他语言：Java: 数组。
     + 列表是有序的，可索引，切片（步长）。

3.  **索引，切片，步长。**

   ```python
   li = [100, '太白', True, [1, 2, 3]]
   # 索引
   # print(li[0], type(li[0]))
   # print(li[1],type(li[1]))
   # print(li[-1])
   
   # 切片 （顾头不顾腚）
   # print(li[:2])
   ```

   相关练习题：

   ```python
   li = [1, 3, 2, "a", 4, "b", 5,"c"]
   通过对li列表的切片形成新的列表l1,l1 = [1,3,2]
   通过对li列表的切片形成新的列表l2,l2 = ["a",4,"b"]
   通过对li列表的切片形成新的列表l4,l4 = [3,"a","b"]
   通过对li列表的切片形成新的列表l6,l6 = ["b","a",3]
   ```

4. 列表的增删改查

   ```python
   # 列表的创建
   # 方式一
   # l1 = [1, 2, 'Alex']
   
   # 方式二
   # l1 = list()
   # l1 = list('fhdsjkafsdafhsdfhsdaf')
   # print(l1)
   
   # 方式三：列表推导式 后面讲
   
   # 增删改查
   l1 = ['太白', '女神', 'xiao','吴老师', '闫龙']
   # 增：
   # append:追加
   # l1.append('xx')
   # print(l1.append('xx'))  # 不能打印它
   # print(l1)
   
   # 举例：
   # l1 = ['太白', '女神', '吴老师', 'xiao', '闫龙']
   # while 1:
   #     name = input('请输入新员工姓名：(Q或者q退出程序)')
   #     if name.upper() == 'Q': break
   #     l1.append(name)
   # print(l1)
   
   # insert 插入
   # l1.insert(2,'wusir')
   # print(l1)
   #extend 迭代着追加
   # l1.extend('abcd')
   # l1.extend(['alex',])
   # l1.extend(['alex', 1, 3])
   # print(l1)
   
   # 删
   # pop 按照索引位置删除
   # l1.pop(-2)  # 按照索引删除 （返回的是删除的元素）
   # print(l1.pop(-2))
   # l1.pop()  # 默认删除最后一个
   # print(l1)
   
   # remove  指定元素删除,如果有重名元素，默认删除从左数第一个
   # l1.remove('xiao')
   # print(l1)
   
   # clear(了解)
   # l1.clear() # 清空
   # print(l1)
   
   # del
       # 按照索引删除
   # del l1[-1]
   # print(l1)
       # 按照切片(步长)删除
   # del l1[::2]
   # print(l1)
   
   # 改
   # 按照索引改值
   # l1[0] = '男神'
   # 按照切片改（了解）
   # l1[2:] = 'fsdafsdafsdfdsfsadfdsfdsgsfdag'
   # print(l1)
   # 按照切片（步长）（了解）
   # l1[::2] = 'abc'
   # l1[::2] = 'abcd'
   # print(l1)
   
   # 查：
   # 索引，切片（步长）
   # for i in l1:
   #     print(i)
   ```

5. 列表的嵌套

   ```python
   l1 = [1, 2, 'taibai', [1, 'alex', 3,]]
   # 1, 将l1中的'taibai'变成大写并放回原处。
   # 2，给小列表[1,'alex',3,]追加一个元素,'老男孩教育'。
   # 3，将列表中的'alex'通过字符串拼接的方式在列表中变成'alexsb'
   ```



6. 元组(**了解**)
   + 只读列表。存大量的数据，可以索引，切片（步长），  (100, '太白', True, [1, 2, 3])

7. range： 类似于列表，自定制数字范围的数字列表



## 4 今日总结

1. 列表的所有的方法全部都要记住，背过（除去了解的）append insert extend pop remove del clear  。

2. 列表的嵌套一定要会。

3. range.与for循环结合。

   

## 5 节后预习内容

​	1. 字典。


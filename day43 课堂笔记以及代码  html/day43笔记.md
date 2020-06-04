## 域名解析

```python
域名 -- ip地址 -- 192.168.1.10

https://192.168.1.10:80  -- www.jd.com  -- DNS解析 {'www.jd.com':'192.168.1.10',}
```

## 请求和响应

```
请求:浏览器socket客户端给服务端发信息
响应:服务端socket给客户端回信息
```



## 标签

Html标签:超文本标记语言,就是标记用的.

```html
必须是封闭的
<meta >
<h1></h1>  
标签属性  id='xx' asdfasfd='xxx'
<h1 id='xx' asdfasfd='xxx'>  

```

## 标签分类

```html

两类:
	内敛标签(行内标签):不独占一行,内敛标签只能嵌套内敛标签    b\i\u\s\button\span\img\a
	块级标签(行外标签):自己独占一行,可以嵌套内敛标签和某些块级标签   \h1-h6\br\hr\p\div
	p标签:不能嵌套p标签,也不能嵌套块级标签
```

## head标签中的标签

```html
<title></title>	定义网页标题

<meta/>	定义网页原信息\配置信息(了解)
```

## body标签中的基本标签

```html
<b>加粗</b>
<i>斜体</i>
<u>下划线</u>
<s>删除</s>

<p>段落标签</p> #独占一个段落

<h1>标题1</h1>
<h2>标题2</h2>
<h3>标题3</h3>
<h4>标题4</h4>
<h5>标题5</h5>
<h6>标题6</h6>

<!--换行-->
<br>

<!--水平线\分割线-->
<hr> 
```



img标签

```
图片标签
属性 src='图片路径'  网络地址的绝对路径\本地相对路径
示例:
	<img src="1.jpg" alt="这是个美女,请稍等.." title="美女" width="200" height="200">
```

a标签  超链接标签

```html
属性
href:超链接的地址
target:是否新建窗口
target="_self"  当前窗口打开某个路径对应的html页面
target="_blank" 新建窗口打开某个路径对应的html页面
示例:
	<a href="https://www.baidu.com" target="_blank">百度</a>
```

列表标签

```html
无序列表:    
<ul type="none">
        <li>太白</li>
        <li>alexdsb</li>
        <li>景女神</li>
    </ul>
有序列表:
    <ol type="a" start="2">
        <li>大壮</li>
        <li>B哥</li>
        <li>灭霸</li>
        <li>雪飞</li>
    </ol>
```

标题列表标签

```html
<dl>
  <dt>标题1</dt>
  <dd>内容1</dd>
  <dt>标题2</dt>
  <dd>内容1</dd>
  <dd>内容2</dd>
</dl>
```



特殊字符

```
空格:&nbsp;
小于号:&lt;
大于号:&gt;
&符号:&amp;
...
```



表格标签(重点)

```html
table
	cellpadding:文字和内边框的距离
	cellspacing:内边框和外边框的距离
	border:边框宽度

<table border="1" cellpadding="10" cellspacing="20">
        <thead>
            <tr>
                <th>姓名</th>
                <th>年龄</th>
                <th>爱好</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>B哥</td>
                <td>40</td>
                <td>炒鸡蛋</td>
            </tr>
            <tr>
                <td>大壮</td>
                <td>38</td>
                <td>抽烟喝酒烫头</td>
            </tr>
            <tr>
                <td>雪飞</td>
                <td>18</td>
                <td>大壮</td>
            </tr>
        </tbody>
    </table>
```



## form标签  表单标签和input标签  用户输入或者选择使用的标签

```html
    action:指定数据提交路径
    input标签:
    	type属性:控制输入框的样式的
    	name属性:分组,携带数据的key   key:value
    	value:选择框提交数据的时的值,输入框的默认值
    input type属性的值:
    	text	单行输入文本	<input type=text" />
		password	密码输入框（不显示明文）	<input type="password"  />
		date	日期输入框	<input type="date" />
		checkbox	复选框	<input type="checkbox" checked="checked" name='x' />
		radio	单选框	<input type="radio" name='x' />
		submit	提交按钮	<input type="submit" value="提交" /> #发送浏览器上输入标签中的内容，配合form表单使用，页面会刷新
		reset	重置按钮	<input type="reset" value="重置"  />  #页面不会刷新，将所有输入的内容清空
		button	普通按钮	<input type="button" value="普通按钮"  />
		hidden	隐藏输入框	<input type="hidden"  />
		file	文本选择框	<input type="file"  /> （等学了form表单之后再学这个）
    	
    	
    <form action="http://127.0.0.1:8001">

            用户名:<input type="text" name="username" value="dazhuang">
            密码:<input type="password" name="password" value="111">

            <input type="radio" name="sex" value="1">男
            <input type="radio" name="sex" value="2">女

            <input type="checkbox" name="hobby" value="a"> 喝酒
            <input type="checkbox" name="hobby" value="b"> 抽烟
            <input type="checkbox" name="hobby" value="c"> 烫头
            <input type="submit">
            <hr>
        	<input type="date">
        	<input type="button" value="普通按钮">
        	<input type="reset">
        	<input type="hidden">
        	<input type="file">
    </form>
    
    form表单触发提交数据的操作,必须写在form表单标签里面,写在外面就是普通的按钮
    	<input type="submit">
    	<button>提交按钮</button>
   
input标签的其他属性
	checked默认选中
	 <input type="radio" name="sex" value="2" checked>女   #简写方式,当属性名和属性值相同时可简写
     <input type="checkbox" name="hobby" value="a"> 喝酒
     <input type="checkbox" name="hobby" value="b" checked="checked"> 抽烟
     <input type="checkbox" name="hobby" value="c" checked="checked"> 烫头

	readonly  只读 针对的是输入框  text password
	disabled  不允许操作  所有的input都可以设置
设置了readonly的标签,它的数据可以被提交到后台,设置了disabled的数据,是不能提交到后台的

```

## select标签 下拉选择框

```html
单选
	<select name="city">
            <option value="1">北京</option>
            <option value="2" selected>上海</option>
            <option value="3">深圳</option>
    </select>
多选:multiple
	<select name="city" multiple>
            <option value="1">北京</option>
            <option value="2" selected>上海</option>
            <option value="3">深圳</option>
   </select>

```



## label标签

标识标签的功能的

```html
方式1:for:执行对哪个标签进行标识
效果:点击label标签中的文字,就能让标识的标签获得光标
<label for="username">用户名</label>
<input id="username" type="text" name="username" value="dazhuang">
方式2:
        <label>
            密码:<input type="password" name="password" value="111" disabled>
        </label>
```



## textarea多行文本

```html
<textarea name="memo" id="memo" cols="30" rows="10">
  默认内容
</textarea>
name：名称
rows：行数  #相当于文本框高度设置
cols：列数   #相当于文本框长度设置
disabled：禁用
```








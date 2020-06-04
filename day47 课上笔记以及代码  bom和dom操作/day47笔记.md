# 昨日内容回顾

## js代码引入

```js
方式1:
    <script>

        // alert('澳门皇家赌场上线啦!!!')

        var a1 = 100;

    </script>

方式2:
	<script src='js文件路径'></script>

```

# 变量声明

```
var a = 10;
```

# 基础数据类型

## 数值类型 Number

```
整数,浮点数,NaN
```

## 字符串

```
var s1 = 'hello';
var s2 = 'world';
var ss = s1+s2
```

### 字符串的常用方法

```js
var s = 'hello';
var s2 = 'world';
s.length  长度
s.trim()  移除两端空白  s.trimLeft()  s.trimRight()
s.concat()  字符串拼接  s.concat(s2)
s.indexOf() 通过元素找索引 s.indexOf('e')
s.charAt(n) 通过索引找元素  s.charAt(1) -- 'e'
s.slice()  切片  s.slice(1,3)
s.split()  分隔  s.split('e',2) -- ['h','llo']
s.toLowerCase()  全部变小写
s.toUpperCase()  全部变大写

```

## 布尔值

```
var a = true;
var b = false;
空的数据类型也是false,'',0,NaN,null,undefined..
```

## null和undefined

```
null  空值,一般用来清空一个变量值来用
undefined  var a; 声明了变量,还没有赋值,此时这个变量值为undefined
```

## 类型转化

```
parseInt('111')
parseFloat('1.11')
```

# 复杂数据类型

## 数组

```
var a = [11,22,33];
var a = new Array([11,22,33]);
typeof a;  --- object类型

```

### 数组常用方法

```
a[1]  -- 1是索引,索引取值
a.length  -- 数组长度
a.push()  尾部追加 a.push('aa') 
a.pop()   尾部删除
a.unshift() 头部追加 a.unshift('aa') 
a.shift() 头部删除
a.sort()  排序
	function sortNumber(a,b){ return a - b; } 升序  a.sort(sortNumber)
a.slice()  切片
a.splice()  删除元素  a.splice(索引,删除几个,新值)  a.splice(1,2,'aa','bb')
a.reverse()  反转 -- 原数组上反转
a.join('+')  元素拼接
a.concat() 
	var b = ['aa','bb']
	a.concat(b)  -- 类似python的extend

```

## 自定义对象

```
var a = {'name':'chao',age:18}
a.name\a['name']  取值

for (var i in a){
	console.log(i,a[i])
}
```



# 运算符

## 算数运算符

```js
+ - * / % ++ --   a++ 和 ++a的区别,a++ 先执行后面的逻辑,在执行加一操作.++a相反
				  a-- --a都是减一操作
```

## 比较运算符

```js
> >= < <= != !== == ===
```

## 逻辑运算符

```js
&&  ||  !  与 或 非
```

## 赋值运算符

```js
+= -= *= /=
```

## 流程控制

### if

```
var a = 10;
if (a>5){
	console.log(11)
}
else{
	...
}

多条件判断
if (a>5){
	console.log(11)
}
else if (a===5){
	...
}
else{
	...
}

```

### switch 切换

```js
var a = 10;
switch (a){
	case 10:
		...
		break;
    case 11:
    	...
    	break;
    default:
    	do something!
}


switch (a){
	case 10:
		console.log('bbbb')  case 10成立的话,执行case 10后面的内容,和case 10: case 11:两个条件共同要执行的那段代码,条件成立一个就行
    case 11:
    	console.log('aaaa')
    	break;
    default:
    	console.log('do something!')
}

```

### while

```
var a = 0;
while (a<10){
	console.log(a);
	a++;
}
```

### 三元运算符

```
var a = 1;
var b = 2;
var c = a > b ? a : b;
```

### for

```js
for (var i=0;i<10;i++){
	console.log(i);
}
var d = [11,22,33];
循环遍历数组
方式1
for (var i in d){   // i是索引,python中的 for i in [11,22,33]:print(i) i都是元素
	console.log(i,d[i]);  
}
方式2
for (var i=0;i<d.length;i++){
	console.log(i,d[i]);
}

循环遍历自定义对象
var a = {'name':'dazhuang',age:18}
for (var i in a){
	console.log(i,a[i]);
}

```



# 函数

```js
function f1(){
	console.log('红旭!');
}
function f1(a,b){
	console.log('红旭!');
	return '红旭妹妹!'
}
f1(1,2) 执行

匿名函数
var sum = function(a,..){
	console.log('红旭妹妹想唱歌!')
};
sum(1,...)

自执行函数
(function (a,..){...})(1,...)

```

## 作用域

```
函数变量,从自己那一层逐层往外找
```

## 闭包

```js
function outer(){
	var o = 10;
	function inner(){
		console.log(o);
	}
	return inner;
}
var ret = outer();
ret()
```

## 面向对象

```
function Person(a,b){
	this.a = a;  this--python 的 self
	this.b = b;
}
Person.prototype.f1 = function (c,d){return c+d;}

var p = new Person('aa','bb')

p.a -- 'aa'
p.f1(1,2)

```

## Date对象

```
var d = new Date(); 当前时间日期对象
d.toLocaleString(); -- 2019/7/4  上午9:32
var d = new Date('2019/7/2 12:00');
d.toLocaleString(); -- 2019/7/2  中午12:00
```

#### date对象的常用方法

```
d.getDate() -- 4
d.getDay() ---4
//getMonth ()               获取月（0-11,0表示1月,依次类推）
//getFullYear ()            获取完整年份
//getHours ()               获取小时
//getMinutes ()             获取分钟
//getSeconds ()             获取秒
//getMilliseconds ()        获取毫秒
//getTime ()                返回累计毫秒数(从1970/1/1午夜),时间戳
```



## json对象

```
序列化
var d = {'xx':'xx'};
var dStr = JSON.stringify(d) -- '{"xx":"xx"}'

反序列化
var d = '{"xx":"xx"}';
var dd = JSON.parse(d) -- {"xx":"xx"}
```

正则RegExp

```
var s = 'hello';
var s2 = 'alex a';
var a = /^a/;
var a = new RegExp("^a")
a.test(s) -- false
a.test(s2) -- true
a.test() -- 不写参数,里面默认放一个"undefined"字符串

s2.match(/a/g)  --['a','a']
s2.split(/a/g)  字符分隔  
s2.replace(/a/gi,'sss');
s2.search(/a/) -- 找索引位置

```

## Math内置模块

```js
Math.abs(-1) -- 1
exp(x)      返回 e 的指数。
floor(x)    小数部分进行直接舍去。
log(x)      返回数的自然对数（底为e）。
max(x,y)    返回 x 和 y 中的最高值。
min(x,y)    返回 x 和 y 中的最低值。
pow(x,y)    返回 x 的 y 次幂。
random()    返回 0 ~ 1 之间的随机数。
round(x)    把数四舍五入为最接近的整数。
sin(x)      返回数的正弦。
sqrt(x)     返回数的平方根。
tan(x)      返回角的正切。
```



# 今日内容

## BOM 浏览器对象模型

### window对象的子对象中的location

```
location.href   获取当前url:"https://www.cnblogs.com/clschao/articles/10092991.html"
location.href="URL" // 跳转到指定页面
	示例:location.href = 'http://www.baidu.com';直接跳转到百度
location.reload() 重新加载页面,就是刷新一下页面
```

### 计时器相关(计时器是异步的)

### 	setTimeout 计时器,一段时间之后做某些事情

```
setTimeout('confirm("你好");',3000);  #3秒之后执行前面的js代码
setTimeout(confirm('xxx'),3000);  #如果写的不是字符串,会直接执行
setTimeout(function(){confirm('xxx')},3000);  #最好写成函数

var a = setTimeout(function(){console.log('xxx')},3000);  #a是浏览器来记录计时器的一个随机数字
clearTimeout(a)  #清除计时器,通过这个数字可以清除
```

### 	setInterval 计时器,每隔一段时间做某些事情

```
var a = setInterval(function(){console.log('xxx')},3000);  
clearInterval(a);
```



# DOM

## 选择器

### 	直接查找

```
document.getElementById           根据ID获取一个标签
document.getElementsByClassName   根据class属性获取（可以获取多个元素，所以返回的是一个数组）
document.getElementsByTagName     根据标签名获取标签合集
示例:
	<div class="c1" id="d1">
    	待到将军归来日,朕与将军解战袍!
	</div>

	<div class="c1" id="d2">
    	日照香炉生紫烟,遥看瀑布挂前川!
	</div>
	
	var a = document.getElementById('d1');  # 获取id属性值为d1的标签  拿到的直接是标签对象
	var a = document.getElementsByClassName('c1'); #获取class值为c1的所有标签  拿到的是数组
	var a = document.getElementsByTagName('div');  #获取所有div标签  拿到的是数组
	
	
```

### 	间接查找

```
var a = document.getElementById('d1');
a.parentElement; #获取a这个标签的父级标签.
children                 所有子标签
firstElementChild        第一个子标签元素
lastElementChild         最后一个子标签元素
nextElementSibling       下一个兄弟标签元素
previousElementSibling   上一个兄弟标签元素

```



## 节点操作

```js
创建节点(创建标签) 
	var a = document.createElement('标签名称'); 
	示例,创建a标签
		var a = document.createElement('a');
	var dd = document.getElementById('dd'); 找到div标签
	
添加节点
	#添加节点,添加到了最后
	dd.appendChild(a);将创建的a标签添加到dd这个div标签里面的最后.

	#在某个节点前面添加节点
	父级标签.insertBefore(新标签,某个儿子标签)
	示例
		var dd = document.getElementById('dd');  #找到父级标签
		var a = document.createElement('a');   #创建一个新的a标签
		var d2 = dd.children[1];  #找到父级标签下的某个儿子标签
		dd.insertBefore(a,d2);   #将a标签插入到上面这个儿子标签的前面.
删除节点
	dd.removeChild(d2);  父级标签中删除子标签
        
替换节点
	var dd = document.getElementById('dd');  #找到父级标签
	var a = document.createElement('a');  #创建a标签
	a.innerText = '百度';  
	var d1 = dd.children[0];  #找到要被替换的子标签
	dd.replaceChild(a,d1);  #替换
    
```



## 文本操作

```
d1.innerText; 查看

设置:
	d1.innerText = "<a href=''>百度</a>";  
	d1.innerHTML = "<a href=''>百度</a>";  能够识别标签
```



## 属性操作

```
var divEle = document.getElementById("d1");
divEle.setAttribute("age","18")  #比较规范的写法
divEle.getAttribute("age")
divEle.removeAttribute("age")

// 自带的属性还可以直接.属性名来获取和设置，如果是你自定义的属性，是不能通过.来获取属性值的
imgEle.src
imgEle.src="..."
```



## 值操作

```
var inp = document.getElementById('username');
inp.value;  #查看值
inp.value = 'taibai'; #设置值

选择框:
	<select name="city" id="city">
        <option value="1">上海</option>
        <option value="2">北京</option>
        <option value="3">深圳</option>
    </select>
	
	var inp = document.getElementById('city');
	inp.value;  #查看值
	inp.value = '1';  #设置值
	
```



## class的操作

```
var d = document.getElementById('oo'); 
d.classList;  #获得这个标签的class属性的所有的值
d.classList.add('xx2');  #添加class值
d.classList.remove('xx2'); #删除class值
d.classList.contains('xx2');  #判断是否有某个class值,有返回true,没有返回false
d.classList.toggle('xx2');  #有就删除,没有就增加
```

## css操作

```
var d = document.getElementById('oo');
d.style.backgroundColor = 'deeppink';  有横杠的css属性,写法要去掉横杠,并且横杠后面的单词首字母大写
d.style.height = '1000px'
```

## 事件

绑定事件的方式有两种

方式1:

```
<div id="d1" class="c1" onclick="f1();"></div>

<script>
    function f1() {
        var d = document.getElementById('d1');
        d.style.backgroundColor = 'yellow';
    }

</script>
```

方式2

```
	<div id="d1" class="c1"></div>

    var d = document.getElementById('d1');
    d.onclick = function () {
        d.style.backgroundColor = 'yellow';
    }

```



### 事件里面的this

绑定方式1:

```
this表示当前标签对象
<div id="d1" class="c1" onclick="f1(this);"></div>
function f1(ths) {
        // var d = document.getElementById('d1');
        // d.style.backgroundColor = 'yellow';
        ths.style.backgroundColor = 'yellow';

        var d = document.getElementById('d2');
        d.style.backgroundColor = 'yellow';
    }
```

方式2:

```
    <div id="d1" class="c1"></div>
    
    var d = document.getElementById('d1');
    d.onclick = function () {
        this.style.backgroundColor = 'yellow';
        // d.style.backgroundColor = 'yellow'; //this表示当前标签对象
    }

```

onblur和onfocus事件

```
 var inp = document.getElementById('username');
    inp.onfocus = function () {
        var d = document.getElementById('d1');
        d.style.backgroundColor = 'pink';
    };
    // onblur 失去光标时触发的事件

    inp.onblur = function () {
        var d = document.getElementById('d1');
        d.style.backgroundColor = 'green';
    };
```

onchange事件,域内容发生变化时触发

```
<select name="" id="jishi">
    <option value="1">太白</option>
    <option value="2">alex</option>
    <option value="3">沛齐</option>

</select>

// onchange事件，内容发生变化时触发的事件
    var s = document.getElementById('jishi');
    s.onchange = function () {
    	//this.options  select标签的所有的option标签
    	//this.selectedIndex被选中的标签在所有标签中的索引值
        console.log(this.options[this.selectedIndex].innerText + '搓的舒服');
    }
    
    
用户名:<input type="text" id="username">    

    //input标签绑定onchange事件
    var inp = document.getElementById('username');
    inp.onchange = function () {
        console.log(this.value);  
    };    
```






















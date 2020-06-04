# 昨日内容回顾

## 边框

```css
border-style:solid;
border-width:1px;
border-color:red;
简写:
border:1px dotted red;

单独
border-top-style:solid;
简写
border-top:1px dotted red;

边框圆角
border-radius:50%
```

## display

```css
display的值:
none:隐藏标签,不占空间 ---  visibility:hidden;隐藏标签,占用空间
inline:将标签做成内敛样式
block:将标签做成块级样式
inline-block:同时具备两种标签的一些特点,能够设置高度宽度,并且不独占一行

```



## 盒子模型

```
content 内容  
padding 内边距  内容与边框之间的距离  padding:10px 20px;上下 左右  padding:1px 20px 30px 40px;上右下左
border 边框
margin 外边距 与其他标签之间的距离
```

## float浮动

```css
布局用的,设置了浮动的标签会脱离正常文档流,会造成父级标签塌陷的问题
float:left;
float:right;

解决塌陷:
	1.父级标签设置行高
	2.伪元素选择器清除浮动
		.clearfix:after{
			content:'';
			display:block;
			clear:both;
		}
		父级标签class='clearfix'

```

## overflow溢出

```
overflow:auto; 出现滚动条
overflow:hidden; 隐藏内容
```

## position定位

```
position:static.  默认就是它
position:relative;相对定位,保留原来位置的空间,相对自己原来的位置移动
position:absolute;绝对定位,不保留原来位置的空间,按照父级标签或者祖先标签中有设置了position为相对定位的标签,如果有,按照他的位置移动,如果没有按照body移动
position:fixed; 固定定位.根据浏览器窗口位置来定位
```

## z-index控制层级

```
z-index的值谁大谁在上面
```

## 透明度opacity

```
opacity标签透明度
rgba(255,0,0,0.3) 单独设置的某个属性的透明度
```

## 锚点

```
设置
	<a name='top'>顶部<a/>
	<div id='top'>顶部</div>
触发点:
	<a href='#top'></a>
```



# 今日内容

## js引入

```
方式1:
	<script>
		// js代码
    	alert('澳门皇家赌场上线啦!!!')
	</script>
方式2:外部文件引入 xx.js文件
	<script src="js文件路径"></script>
	
```

## 注释

```
// 这是单行注释

/*
这是
多行注释
*/
```

结束符

```
结束符 JavaScript中的语句要以分号（;）为结束符。也就是说和缩进没关系了
```

## 声明变量var

```
var a = 10;
声明变量时可以先不赋值
var a;此时a的值为undefined  
```

js动态类型语言



## 基础数据类型

### 数值类型 Number

```javascript
var a = 10;
undefined
typeof a;
"number"
var b = 1.11;
undefined
typeof b;
"number"
查看数据类型用 typeof a;

var c = 123e5;  // 12300000
var d = 123e-5;  // 0.00123

```



### 字符类型 String

```
var a = 'alexdsb'
	a
		"alexdsb"
	typeof a;
		"string"
var a = "Hello"
var b = "world;
var c = a + b;   //字符串拼接
console.log(c);  // 得到Helloworld
```

### 类型转换

```js
parseInt("123")  // 返回123
parseInt("ABC")  // 返回NaN,NaN属性是代表非数字值的特殊值。该属性用于指示某个值不是数字。
parseFloat("123.456")  // 返回123.456

示例:
var a = 'a123';
var b = parseInt(a);

	b
		NaN
	typeof b;
		"number"
		
var b = '1.11';
parseFloat(b)
		1.11        
```



### 字符串常用方法

```
1  .length属性,查看字符串长度
示例
	var a = 'hello';
	a.length; // 5
2  .trim() 移除空白
示例
	var a = '  hello  ';
	a.trim(); //"hello"
3  .trimLeft()  .trimRight()
4  .charAt(n) 返回索引为n的那个字符
5  .concat()  字符串拼接
	示例
		var a = 'hello';
		var b = 'world';
		a.concat(b)  //"helloworld"
6  .indexOf()  通过元素找索引
	示例
		a
			"hello"
		a.indexOf('e')
		
		start参数,索引起始位置
		a.indexOf('l',3)
		
		找不到返回-1
			a.indexOf('e',3)  -1
7  .slice() 切片
	var a = 'hello';
	a.slice(2,4)  顾头不钴锭
8   .toLowerCase() #全部变小写	 
	.toUpperCase()  #全部变大写
	示例:
		var b = 'HH';
		b.toLowerCase();
		
9  .split 字符串分隔,第二个参数是返回多少个数据
	示例
	var a = "hello"
	a.split('e') //(2) ["h", "llo"]
	a.split('e',1) //["h"]  	
	
```

### 布尔值

```
var a = true;
var b = false;

""(空字符串)、0、null、undefined、NaN都是false。

```

### null和undefined

```
　null和undefined
	null表示值是空，一般在需要指定或清空一个变量时才会使用，如 name=null;
	undefined表示当声明一个变量但未初始化时，该变量的默认值是undefined。还有就是函数无明确的返回值时，	返回的也是undefined。
　　　　null表示变量的值是空，undefined则表示只声明了变量，但还没有赋值。
```



### 对象类型 object

```
JavaScript 中的所有事物都是对象：字符串、数值、数组、函数...此外，JavaScript 允许自定义对象。
比如声明一个字符串对象
	var a = new String('bb')

```

## 复杂数据类型或者引用数据类型

### 数组 Array

```
创建数组:
var a = [11,22,33];
var b = new Array([22,33])
typeof a;  //object类型
```

#### 数组常用方法和属性

```
1 索引取值
	var a = [123, "ABC"]; 
	console.log(a[1]);  // 输出"ABC"

2 .length  a.length //2

3. .push() 尾部追加  .pop()尾部删除
	示例
		var a = [11,22,33]
		a.push('123'); //[11, 22, 33, "123"]
		a.pop();  //"123"
		a  --  [11, 22, 33]
4 .unshift(ele)头部追加  .shift()头部删除
	var a = [11,22,33]

	a  //(3) [11, 22, 33]
		a.unshift('aa');
	a
		(4) ["aa", 11, 22, 33]
	a.shift();
		"aa"
	a
		(3) [11, 22, 33]

5  .sort排序
	var a = [11,4,84,73];

	a.sort()
		(4) [11, 4, 73, 84]
	function sortNumber(a,b){
    	return a - b;
	}

	a.sort(sortNumber)
		(4) [4, 11, 73, 84]
	function sortNumber(a,b){
    	return b - a
	}
	a.sort(sortNumber)
		(4) [84, 73, 11, 4]
		
	解释:
		如果想按照其他标准进行排序，就需要提供比较函数，也就是自己提供一个函数提供排序规则，该函数要比较两个值，然后返回一个用于说明这两个值的相对顺序的数字。比较函数应该具有两个参数 a 和 b，其返回值如下：

　　　　　　若 a 小于 b，在排序后的数组中 a 应该出现在 b 之前，则返回一个小于 0 的值。
　　　　　　若 a 等于 b，则返回 0。
　　　　　　若 a 大于 b，则返回一个大于 0 的值。

6  .splice() 删除元素   var a = [84, 73, 11, 4];  a.splice(1,2,'aa','bb','cc');


```

### 自定义对象  {}

```
var a = {"name": "Alex", "age": 18};
var d = {'name':'chao',age:18}; 键可以不加引号
console.log(a.name);
console.log(a["age"]);
for循环遍历自定义对象
var a = {"name": "Alex", "age": 18};
for (var i in a){
  console.log(i, a[i]);
}


```



## 运算符

### 算数运算符

```
+ - * / % ++ --  i++,是i自加1，i--是i自减1   i++的这个加1操作优先级低，先执行逻辑，然后再自加1，而++i，这个加1操作优先级高，先自加1，然后再执行代码后面的逻辑
```

### 比较运算符

```
> >= < <= != == === !==   ==是弱等于(不比较数据类型)    ===强等于 强等于会比较数据类型
```

### 逻辑运算符

```
&& || !  #and，or，非（取反）!null返回true
```

### 赋值运算符

```
= += -= *= /=  #n += 1其实就是n = n + 1
```



## 流程控制

### if -else if -else

```
var a = 10;
if (a > 5){   
  console.log("a > 5");
}else if (a < 5) {
  console.log("a < 5");
}else {
  console.log("a = 5");
}

```

### switch 切换

```
var a = 10;
undefined
switch (a){    //switch (a++){}
    case 9:
		console.log('999');
	break;
    case 10:
		console.log('101010');
	break;
    case 11:
		console.log('111111');
	break;
}

加上default示例:

    var a = 20;

    switch (a){
        case 9:
            console.log('999');
        break;
        case 10:
            console.log('101010');
        break;
        case 11:
            console.log('111111');
        break;
        default :  //上面的条件都不成立的时候,走default
            console.log('啥也不对!!')

    }



```



# 问题

```
var a = 10;

    switch (a){
        case 9:
            console.log('999');
        break;
        case 10:
            console.log('101010');
        // break;
        case 11:
            console.log('111111');
        break;
        default :
            console.log('啥也不对!!')

    }
```



### for循环

```
for (var i=0;i<10;i++) {  
  console.log(i);
}

循环数组：
var l2 = ['aa','bb','dd','cc']
方式1
for (var i in l2){
   console.log(i,l2[i]);
}
方式2
for (var i=0;i<l2.length;i++){
　　console.log(i,l2[i])
}

循环自定义对象：
var d = {aa:'xxx',bb:'ss',name:'小明'};
for (var i in d){
    console.log(i,d[i],d.i)  #注意循环自定义对象的时候，打印键对应的值，只能是对象[键]来取值，不能使用对象.键来取值。
}

```

### while循环

```
var i = 0;
while (i < 10) {
  console.log(i);
  i++;
}
```

### 三元运算符

```
var a = 1;
var b = 2;
var c = a > b ? a : b //如果a>b这个条件成立，就把冒号前面的值给c，否则把冒号后面的值给c   //python中的：a = x if x>y else y
```



## 函数

```
// 普通函数定义
function f1() {
  console.log("Hello world!");
}

// 带参数的函数
function f2(a, b) {
  console.log(arguments);  // 内置的arguments对象
  console.log(arguments.length);
  console.log(a, b);
}

// 带返回值的函数
function sum(a, b){
  return a + b;  //在js中，如果你想返回多个值是不行的，比如return a ，b；只能给你返回最后一个值，如果就想返回多个值，你可以用数组包裹起来 return [a,b]；
}
sum(1, 2);  // 调用函数  sum(1,2,3,4,5)参数给多了，也不会报错，还是执行前两个参数的和，sum(1)，少参数或者没参数也不报错，不过返回值就会是NAN

// 匿名函数方式，多和其他函数配合使用，后面我们就会用到了
var sum = function(a, b){  //在es6中，使用var，可能会飘黄，是因为在es6中，建议你使用let来定义变量，不过不影响你使用
  return a + b;  
}
sum(1, 2);

// 立即执行函数，页面加载到这里，这个函数就直接执行了，不需要被调用执行
(function(a, b){
  return a + b;
})(1, 2);  //python中写可以这么写：ret=(lambda x,y:x+y)(10,20) 然后print(ret)
```



### 函数的全局变量和局部变量

```
局部变量：

　　　　　　在JavaScript函数内部声明的变量（使用 var）是局部变量，所以只能在函数内部访问它（该变量的作用域是函数内部）。只要函数运行完毕，本地变量就会被删除。

　　　　全局变量：

　　　　　　在函数外声明的变量是全局变量，网页上的所有脚本和函数都能访问它。

　　　　变量生存周期：

　　　　　　JavaScript变量的生命期从它们被声明的时间开始。

　　　　　　局部变量会在函数运行以后被删除。

　　　　　　全局变量会在页面关闭后被删除。
```

### 作用域

```
首先在函数内部查找变量，找不到则到外层函数查找，逐步找到最外层。
```

### 闭包

```
var city = "BeiJing";
function f(){
    var city = "ShangHai";
    function inner(){
        console.log(city);
    }
    return inner;
}
var ret = f();
```



## 面向对象

es5封装方式

```
function Person(name){
	this.name = name;
}
var p = new Person('taibai');
p.name

"taibai"
Person.prototype.sum = function(a,b){return a+b;}
ƒ (a,b){return a+b;}

p.sum(2,3);

```



## Date对象

```
var d1 = new Date(); //获取当前时间
console.log(d1.toLocaleString());  //当前时间日期的字符串表示
//方法2：参数为日期字符串
var d2 = new Date("2004/3/20 11:12");
console.log(d2.toLocaleString());
var d3 = new Date("04/03/20 11:12");  #月/日/年(可以写成04/03/2020)
console.log(d3.toLocaleString());
//方法3：参数为毫秒数，了解一下就行
var d3 = new Date(5000);  
console.log(d3.toLocaleString());
console.log(d3.toUTCString());  
 
//方法4：参数为年月日小时分钟秒毫秒
var d4 = new Date(2004,2,20,11,12,0,300);
console.log(d4.toLocaleString());  //毫秒并不直接显示
```

### date对象的其他方法

```
var d = new Date(); 
//getDate()                 获取日
//getDay ()                 获取星期 ，数字表示（0-6），周日数字是0
//getMonth ()               获取月（0-11,0表示1月,依次类推）
//getFullYear ()            获取完整年份
//getHours ()               获取小时
//getMinutes ()             获取分钟
//getSeconds ()             获取秒
//getMilliseconds ()        获取毫秒
//getTime ()                返回累计毫秒数(从1970/1/1午夜),时间戳
```

## json

```
var str1 = '{"name": "chao", "age": 18}';
var obj1 = {"name": "chao", "age": 18};
// JSON字符串转换成对象  反序列化
var obj = JSON.parse(str1); 
// 对象转换成JSON字符串  序列化
var str = JSON.stringify(obj1);
```



## RegExp正则对象

```
创建正则对象的方法
	var reg1 = new RegExp("^[a-zA-Z][a-zA-Z0-9_]{5,11}$");
简写方式:
	var reg2 = /^[a-zA-Z][a-zA-Z0-9_]{5,11}$/;

test方法.测试某个字符串是否符合正则规则
	var s = 'hello'
	reg1.test(s)  符合返回True,不符合返回false
	
	一个坑:
		reg1.test() 里面什么也不写,会默认放一个"undefined"字符串
		reg1.test("undefined") 



```



其他正则方法

```js
var s2 = "hello world";

s2.match(/o/g);         // ["o", "o"]             查找字符串中 符合正则 的内容 ，/o/g后面这个g的意思是匹配所有的o,
s2.search(/h/g);        // 0                      查找字符串中符合正则表达式的内容位置，返回第一个配到的元素的索引位置，加不加g效果相同
s2.split(/o/g);         // ["hell", " w", "rld"]  按照正则表达式对字符串进行切割，得到一个新值，原数据不变
s2.replace(/o/g, "s");  // "hells wsrld"          对字符串按照正则进行替换

var s1 = "name:Alex age:18";

s1.replace(/a/, "哈哈哈");      // "n哈哈哈me:Alex age:18"
s1.replace(/a/g, "哈哈哈");     // "n哈哈哈me:Alex 哈哈哈ge:18"      全局匹配
s1.replace(/a/gi, "哈哈哈");    // "n哈哈哈me:哈哈哈lex 哈哈哈ge:18"  不区分大小写

坑:
	var reg = /a/g;
	var s = 'alex a sb';
	reg.test(s); //true
	reg.lastIndex; // 1
	reg.test(s); //true
	reg.lastIndex; // 6
	reg.test(s); //false
	
	reg.lastIndex = 0;重新赋值,让其归零
```

## Math计算模块

```js
Math.abs(x)      返回数的绝对值。
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




















































































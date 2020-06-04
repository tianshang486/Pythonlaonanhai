# 昨日内容回顾

## BOM

```
window对象
location.href;获取当前窗口的url
location.href = 'http://www.xiaohuar.com';  #跳转到指定网址
location.reload() 刷新页面

计时器
var a = setTimeOut(function(){...},毫秒);  一段时间后做某些事情
clearTimeOut(a)
var a = setInterval(function(){},毫秒);
clearInterval(a);

```



## DOM

### 选择器

```
直接查找:
	document.getElementById('d1')
	document.getElementsByClassName('c1')
	document.getElementsByTagName('标签名')
间接查找
	var a = document.getElementById('d1');
	a.parentElement
	a.children
	firstElementChild
	lastElementChild
	nextElementSibling
	previousElementSibling
```



### 节点操作

```
创建节点
	var a = document.createElement('标签名');
添加节点
	父级节点.appendChild(a);
	父级节点.insertBefore(a,某个儿子节点)
删除节点
	父级节点.removeChild(某个节点)
替换
	父级节点.replaceChild(新节点,被替换的那个节点)
	
```

### 文本操作

```
innerText  
innerHtml  识别标签

innerText='xx'.
innerHtml='xx'
```

### 属性操作

```
设置属性 setAttribute(属性,值)
查看属性 getAttribute(属性)
删除属性 removeAttribute(属性)

标签子带属性
标签对象.属性;
标签对象.属性 = 'xxx'
```

### 值操作

```
input select textarea
标签.value;
标签.value = 'xx';

select标签.value
select标签.value = option标签的value属性的值   这个标签就被选中了
```

### class操作

```
获取class的值
标签对象.classList;
标签对象.classList.add('值')
标签对象.classList.remove('值')
标签对象.classList.contains('值')
标签对象.classList.toggle('值')
```

### css操作

```
标签对象.style.css属性 = '值'
background-color  --- backgroundColor
```

### 事件

```js
方式1:
    <div id='d1' onclick="f1();"></div>
    <script>
        function f1(){
            var d = getElementById('d1');
        }

    </script>
方式2:
	<div id='d1'></div>
	<script>
        var d = getElementById('d1');
        d.onclick = function(){}
    </script>

onclick
onfocus
onblur
onchange
```

# 今日内容

jQuery

```

```



## jQuery引入

```
下载链接：[jQuery官网](https://jquery.com/)，首先需要下载这个jQuery的文件，然后在HTML文件中引入这个文件，就可以使用这个文件中帮我们提供的jquery的接口了。
```



## jquery对象和dom对象

```
jquery找到的标签对象称为 -- jquery对象
原生js找到的标签对象称为 -- dom对象
dom对象只能使用dom对象的方法,不能使用jquery对象的方法
jquery对象也是,它不能使用dom对象的方法

dom对象和jquery对象互相转换:
	jquery对象转dom对象 -- jquery对象[0]  示例:$('#d1')[0]
	dom对象转jquery对象 -- $(dom对象)
```



## jQuery选择器

### 基本选择器

```js
jQuery('#d1')  -- $('#d1')
基本选择器（同css）
　　　　　　id选择器：

	$("#id")  #不管找什么标签，用什么选择器，都必须要写$("")，引号里面再写选择器，通过jQuery找到的标签对象就是一个jQuery对象，用原生JS找到的标签对象叫做DOM对象，看我们上面的jQuery对象部分的内容
　　　　　　标签选择器：

	$("tagName")  $('div')
　　　　　　class选择器：

	$(".className")  
　　　　　　配合使用：

	$("div.c1")  // 找到有c1 class类的div标签
　　　　　　所有元素选择器：

	$("*")
　　　　　　组合选择器：

	$("#id, .className, tagName")

	选择器找到的可能是多个标签,会放到数组里面,但还是jquery对象,能够直接使用jquery的方法,意思是找到的所有标签进行统一设置,如果要单独设置选中的所有标签中的某个标签,可以通过索引取值的方式找到,然后注意,通过索引取值拿到的标签,是个dom对象


```

### 基本筛选器

```
<ul>
    <li>蔡世楠</li>
    <li>尤利阳</li>
    <li id="l3">张雷</li>
    <li>申凯琦</li>
    <li id="l5">程德浩</li>
    <li>罗新宇</li>
    <li>曾凡星</li>
</ul>

:first  -- 示例:$('li:first') // 第一个
:last // 最后一个
:eq(index)// 索引等于index的那个元素
:even // 匹配所有索引值为偶数的元素，从 0 开始计数
:odd // 匹配所有索引值为奇数的元素，从 0 开始计数
:gt(index)// 匹配所有大于给定索引值的元素
:lt(index)// 匹配所有小于给定索引值的元素
:not(元素选择器)// 移除所有满足not条件的标签
:has(元素选择器)// --$('li:has(.c1)')  找到后代中含有满足has里面选择器的那个标签
:not(:has(.c1)) -- $('li:not(:has(.c1))') 排除后代中含有满足has里面选择器的那个标签
```



### 属性选择器

```js
[attribute]
[attribute=value]// 属性等于
[attribute!=value]// 属性不等于

// 示例,多用于input标签
<input type="text">
<input type="password">
<input type="checkbox">
$("input[type='checkbox']");// 取到checkbox类型的input标签
$("input[type!='text']");// 取到类型不是text的input标签
```



### **表单筛选器**

```
找到的是type属性为这个值的input标签中
:text
:password
:file
:radio
:checkbox
:submit
:reset
:button
```

### 表单对象属性筛选器

```
:enabled   #可用的标签
:disabled  #不可用的标签
:checked   #选中的input标签
:selected  #选中的option标签
```

### 筛选器方法

```js
下一个:
    $('#l3').next();  找到下一个兄弟标签
    $('#l3').nextAll(); 找到下面所有的兄弟标签
    $('#l3').nextUntil('#l5');#直到找到id为l5的标签就结束查找，不包含它
上一个
	$("#id").prev()
	$("#id").prevAll()
	$("#id").prevUntil("#i2")
父亲元素
    $("#id").parent()
    $("#id").parents()  // 查找当前元素的所有的父辈元素（爷爷辈、祖先辈都找到）
    $("#id").parentsUntil('body') // 查找当前元素的所有的父辈元素，直到遇到匹配的那个元素为止，这里直到body标签，不包含body标签，基本选择器都可以放到这里面使用。

儿子和兄弟元素
$('ul').children(); 
$('ul').children('#l3');  #找到符合后面这个选择器的儿子标签

$('#l5').siblings();
$('#l5').siblings('#l3'); #找到符合后面这个选择器的兄弟标签


find
	$('ul').find('#l3')  -- 类似于  $('ul #l3')
filter过滤
	$('li').filter('#l3');


.first() // 获取匹配的第一个元素
.last() // 获取匹配的最后一个元素
.not()  // 从匹配元素的集合中删除与指定表达式匹配的元素  $('li').not('#l3');
.has()  // 保留包含特定后代的元素，去掉那些不含有指定后代的元素。
.eq()  // 索引值等于指定值的元素
```



# 作业讲解

## 作业1代码:

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="x-ua-compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>定时器</title>

</head>
<body>

<input type="text" id="timer">
<button id="start">开始</button>
<button id="end">结束</button>


<script>
    var timetag;
    // 1 获取当前时间
    function f1() {
        var showTime = new Date();
        var showLocaleTime = showTime.toLocaleString();
        var inpEle = document.getElementById('timer');
        inpEle.value = showLocaleTime;
    }
    // 2 把时间放进去
    //     2.1 找到strat开始按钮,绑定点击事件
    var startBtn = document.getElementById('start');
    startBtn.onclick = function () {
        //2.2 找到input标签,并将值放到input标签里面
        f1();
        if (timetag === undefined){
            timetag = setInterval(f1,1000);
        }
    };
    // 3 停止时间
    var endBtn = document.getElementById('end');
    endBtn.onclick = function () {
        clearInterval(timetag);
        timetag = undefined;
    }


</script>

</body>
</html>
```

## 作业2代码:

```
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="x-ua-compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>select联动</title>
</head>
<body>

<select id="province">
  <option>请选择省:</option>

</select>

<select id="city">
  <option>请选择市:</option>
</select>

<script>
    var data = {"河北省": ["廊坊", "邯郸"], "北京": ["朝阳区", "海淀区"], "山东": ["威海市", "烟台市"]};

    // 1 将省份的数据放到省份的下拉框里面
    //1.1 找到省份下拉框
    var proSelect = document.getElementById('province');
    // 1.2 创建option标签

    //1.3  将数据放到option标签中,并将option标签放到省份下拉框里面
    for (var province in data){
        var proOption = document.createElement('option');
        proOption.innerText = province;
        proSelect.appendChild(proOption);
    }

    //2 选择省份,将被选择的省份的市都放到市的那个下拉框里面
    var citySelect = document.getElementById('city');
    proSelect.onchange = function () {
        citySelect.innerText = '';
        var proText = this.options[this.selectedIndex].innerText;
        var cityData = data[proText];
        for (var cityindex in cityData){
            var cityOption = document.createElement('option');
            cityOption.innerText = cityData[cityindex];
            citySelect.appendChild(cityOption);

        }
    }


</script>

</body>
</html>
```






























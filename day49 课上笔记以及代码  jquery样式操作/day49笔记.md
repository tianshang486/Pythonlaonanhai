# 昨日内容回顾

## jQuery

### jQuery引入

```
<script src="jquery.js"></script>
<script>jquery代码+js</script>
```

### jQuery选择器

#### 基础选择器

```
$('#id值')
$('.类值')
$('div')
$('*')
$('div,p')
```

#### 层级选择器

```
$('div p')
$('div.p')
$('div+p')
$('div>a')
$('div~a')
```

#### 基本筛选器

```
:first
:last
:eq(索引)
:odd 索引为奇数的
:even 索引为偶数的
:gt(索引) 大于某个索引的那些元素
:lt(索引) 小于指定索引的
:not('选择器')  排错满足这个选择器的那些标签
:has('选择器')  找到后代中有满足这个选择器的标签
```

#### 属性选择器

```
[属性名]
[属性名=属性值]
[属性名!=属性值]
input[type=text]
```

#### 表单筛选器

```
:text  input type=text 的input标签
:password
...
```

#### 表单对象属性筛选器

```
:enabled
:disabled
:checked
:selected
```

#### 筛选器方法

```
下一个:
	.next()
	.nextAll()
	.nextUntil('选择器')
上一个
	.prev()
	.prevAll()
	.prenUntil('选择器')
父级
	.parent()
	.parents()
	.parentsUntil('选择器')

儿子和兄弟
	.children()  所有的儿子
	.children('选择器')
	
	.siblings()  所有兄弟标签
	.siblings('选择器')
filter过滤
	$('div').filter('选择器')  
find() 找后代的
	$('div').find('#d1')
	
.first()
.last()
...
```



# 今日内容

## 标签操作

### 样式操作

#### 样式类操作

```
addClass();// 添加指定的CSS类名。
removeClass();// 移除指定的CSS类名。
hasClass();// 判断样式存不存在
toggleClass();// 切换CSS类名，如果有就移除，如果没有就添加。
```

```js
示例代码
	$('.c1').addClass('c2');
	$('.c1').addClass('c2');
	$('.c1').hasClass('c2');
	$('.c1').toggleClass('c2');
```

#### css样式

```
原生js
	标签.style.color = 'red';
jquery
	$('.c1').css('background-color','red');  
	同时设置多个css样式
	$('.c1').css({'background-color':'yellow','width':'200px'})
```

#### 位置操作

```
查看位置
$('.c2').position();  //查看相对位置 
	{top: 20, left: 20}
$('.c2').offset();    //查看距离窗口左上角的绝对位置
	{top: 28, left: 28}
设置位置
	$('.c2').offset({'top':'20','left':'40'});
	
```



jQuery绑定点击事件的写法

```
    原生js绑定点击事件
    // $('.c1')[0].onclick = function () {
    //     this.style.backgroundColor = 'green';
    // }
jquery绑定点击事件
    $('.c1').click(function () {
        $(this).css('background-color','green');
    })
```

点击事件和滚动事件的示例代码

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .c1{
            background-color: red;
            height: 100px;
            width: 100px;
        }
        .c2{
            background-color: green;
            height: 1000px;
            width: 100px;
        }
        .c3{
            background-color: blue;
            height: 1000px;
            width: 100px;
        }
        .s1{
            position: fixed;
            left:20px;
            bottom: 20px;
            height: 40px;
            width: 80px;
            background-color: purple;
            line-height: 40px;
            text-align: center;

        }
        .s1 a{
            color: white;
            font-size: 14px;
            text-decoration: none;
        }
        .hide{
            display: none;
        }


    </style>
</head>
<body>
<!--<a name="top">这里是顶部</a>-->
<!--<a>这里是顶部</a>-->
<span>顶部位置</span>
<div class="c1"></div>

<button class="change-postion">走你</button>

<div class="c2"></div>
<div class="c3"></div>

<span class="s1 hide">
    <!--<a href="#top">返回顶部</a>-->
    <span>返回顶部</span>

</span>


<script src="jquery.js"></script>
<script>
	//点击事件来改变标签位置
    $('.change-postion').click(function () {
        $('.c1').offset({top:200,left:200});
    });
    
	//滚动事件,监听滚动距离来显示或者隐藏标签
    $(window).scroll(function () {
        console.log($(window).scrollTop());
        if ($(window).scrollTop() >=200){
            $('.s1').removeClass('hide');
        }else {
            $('.s1').addClass('hide');
        }
    });
    
	// 回到顶部,scrollTop设置值
    $('.s1').click(function () {
        $(window).scrollTop(0);
    })

</script>

</body>
</html>
```

#### 尺寸

```
$('.c1').height();  //content 高度
$('.c1').width();   //content 宽度
$('.c1').innerHeight();//content高度+padding高度
$('.c1').innerWidth(); //content宽度+padding宽度
$('.c1').outerHeight();//content高度+padding高度 + border高度
$('.c1').outerWidth();//content宽度+padding宽度+ border宽度


示例:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .c1{
            width: 100px;
            height: 100px;
            border: 2px solid red;
            background-color: green;
            padding: 20px 30px;
        }
    </style>
</head>
<body>
<div class="c1"></div>

<script src="jquery.js"></script>
</body>
</html>
```



### 文本操作

```
html()//取得第一个匹配元素的html内容，包含标签内容
html(val)//设置所有匹配元素的html内容，识别标签，能够表现出标签的效果

text()// 取得所有匹配元素的内容，只有文本内容，没有标签
text(val)//设置所有匹配元素的内容，不识别标签，将标签作为文本插入进去
示例:
$('.c1').text('<h3>你好,太白</h3>');
$('.c1').html('<h3>你好,太白</h3>');
```

### 值操作

```
获取值
	input type='text'的标签--$('#username').val();
	input type='radio'标签获取被选中的标签的值 --- $(':radio:checked').val();
	input type='checkbox'标签获取被选中的标签的值 --- 直接$(':checkbox:checked').val();是不行的,需要循环取值  
		var d = $(':checkbox:checked');
		for (var i=0;i<d.length;i++){
			console.log(d.eq(i).val());
		}
		
	单选select --- $('#city').val();
	多选select --- $('#author').val(); // ["2", "3"]	

设置值
	input type='text'的标签 --- $('#username').val('李杰');
	input type='radio'标签 ---  $('[name="sex"]').val(['3']);
			如果 $('[name="sex"]').val('3'),所有标签的值都变成了'3';
	input type='checkbox'设置值 --- $('[name="hobby"]').val(['2','3'])
	单选select --- $('#city').val('1');  option value='1'
	多选select --- $('#author').val(['2','3'])
	
```



### 属性操作

```js
attr(attrName)// 返回第一个匹配元素的属性值
attr(attrName, attrValue)// 为所有匹配元素设置一个属性值
attr({k1: v1, k2:v2})// 为所有匹配元素设置多个属性值
removeAttr(attrName)// 从每一个匹配的元素中删除一个属性

示例:
	设置单个属性
		$('.c1').attr('xx','oo');
	设置多个属性
		$('.c1').attr({'age':'18','sex':'alex'});
	查看属性
		$('.c1').attr('属性名');
    	$('.c1').attr('xx');
    删除属性
    	$('.c1').removeAttr('xx');

prop -- 针对的是checked\selected\disabled..

查看标签是否有checked属性,也就是是否被选中
	    attr $(':checked').attr('checked'); //checked -- undefined
	    prop $(':checked').prop('checked'); //true  -- false
		
		通过设置属性的方式来设置是否选中:
			$(':radio').eq(2).prop('checked',true);  true和false不能加引号
			$(':radio').eq(2).prop('checked',false);

简单总结:
	1.对于标签上有的能看到的属性和自定义属性都用attr
	2.对于返回布尔值的比如checkbox、radio和option的是否被选中或者设置其被选中与取消选中都用prop。
	具有 true 和 false 两个属性的属性，如 checked, selected 或者 disabled 使用prop()，其他的使用 attr()
```



### 文档处理

```js
添加到指定元素内部的后面
	$(A).append(B)// 把B追加到A
	$(A).appendTo(B)// 把A追加到B
	#添加字符串照样能识别标签  *****
	$('#d1').append('<a href="http://www.jd.com">京东</a>');
添加到指定元素内部的前面
	$(A).prepend(B)// 把B前置到A
	$(A).prependTo(B)// 把A前置到B
	示例
		$('a').prependTo($('div'));

添加到指定元素外部的后面
	$(A).after(B)// 把B放到A的后面
	$(A).insertAfter(B)// 把A放到B的后面

添加到指定元素外部的前面
	$(A).before(B)// 把B放到A的前面
	$(A).insertBefore(B)// 把A放到B的前面
	
移除和清空元素
	remove()// 从DOM中删除所有匹配的元素。
	empty()// 删除匹配的元素集合中所有的子节点，包括文本被全部删除，但是匹配的元素还
	$('div').remove();
	$('div').empty();

替换
	replaceWith()
	replaceAll()
	示例:
		var a = document.createElement('a')
		a.href = 'http://www.baidu.com';
		a.innerText = 'xxx';
		
		$('span').replaceWith(a);
		$(a).replaceAll('span');
		
clone()克隆
	<button class="btn">屠龙宝刀,点击就送!</button>	

    $('.btn').click(function () {
        // var a = $(this).clone(); //克隆标签
        var a = $(this).clone(true);  //连带事件一起克隆
        $(this).after(a);

    })
```



作业1:  自定义登录认证

作业2:  全选反选取消

作业3:  添加记录和删除记录  表格


























































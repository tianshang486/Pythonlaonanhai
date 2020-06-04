# 昨日内容回顾

## 样式操作

### 样式类

```
addClass()
removeClass()
hasClass()
toggleClass()

```

### css操作

```
.css({'color':'red',})
```

### 位置操作

```
查看位置
	offset()
	position()
设置位置
	offset({top:100,left:200})
```

### 尺寸

```
content
	.height()
	.width()
content + padding
	.innerHeight()
	.innerWidth()
content +padding + border
	.outerHeight()
	.outerWidth()
	
```

### 文本操作

```
查看文本
	.html()  文本+标签
	.text()  文本
设置
	.html('xxx')  识别标签
	.text('xxx')
```

### 值操作

```js
获取值
	input type='text'   --- $('[type="text"]').val()
	input type='radio'  --- $('[typy="radio"]:checked').val()
	input type='checkbox'  --- var a = $('[typy="checkbox"]:checked')	
                                for (var i=0;i<a.length;i++){
                                    a.eq(i).val();
                                }	
	select 单选   ---  $('select').val();
	select 多选   ---  $('select').val();
	
设置值
	input type='text'   --- $('[type="text"]').val('xxx')
	input type='radio'  --- $('[typy="radio"]').val(['1'])
	input type='checkbox'  --- $('[typy="checkbox"]').val(['1','2'])
	
	select 单选   ---  $('select').val('1');
	select 多选   ---  $('select').val(['1','2']);
	
```

### 属性操作

```js
attr()  
	查看属性  .attr('属性名') 
	设置属性  .attr({属性名':'属性值',})
	
prop()
	checked  selected disabled..
	查看属性
		.prop('checked') -- true\false
	设置属性
    	.prop('checked',true)
```

### 文档操作

```
插入到某个标签的里面的后面
$(A).append(B)         $(A).append('<a href="">xx</a>') 
$(B).appendTo(A) 

插入到某个标签里面的前面
$(A).prepend(B)
$(B).prependTo(A)

插入到某个标签外面的后面
$(A).after(B)
$(B).insertAfter(A)

插入到某个标签外面的前面
$(A).before(B)
$(B).insertBefore(A)

清空和移除
remove()  
empty()

替换
$(A).replaceWith(B)
$(B).replaceAll(A)

克隆
.clone()
.clone(true)  连带事件一起克隆
```



# 今日内容

## 事件

### 事件绑定方式

```js
<script src="jquery.js"></script>
<script>
    //方式1
    // $('#d1').click(function () {
    //     $(this).css({'background-color':'green'});
    // });
    //方式2
    $('#d1').on('click',function () {
        $(this).css({'background-color':'green'});
    })

</script>
```

### 常用事件

```js
click  左键点击事件
    //获取光标触发的事件
    $('[type="text"]').focus(function () {
        $('.c1').css({'background-color':'black'});
    });
    //失去光标(焦点)触发的事件
    $('[type="text"]').blur(function () {
        $('.c1').css({'background-color':'purple'});
    });

    //域内容发生改变时触发的事件
    $('select').change(function () {
        $('.c1').toggleClass('cc');
    });

    //鼠标悬浮触发的事件
    // $('.c1').hover(
    //     //第一步:鼠标放上去
    //     function () {
    //         $(this).css({'background-color':'blue'});
    //     },
    //     //第二步,鼠标移走
    //     function () {
    //         $(this).css({'background-color':'yellow'});
    //     }
    // )

    // 鼠标悬浮  等同于hover事件
    // 鼠标进入
    // $('.c1').mouseenter(function () {
    //     $(this).css({'background-color':'blue'});
    // });
    // 鼠标移出
    //  $('.c1').mouseout(function () {
    //     $(this).css({'background-color':'yellow'});
    // });
	
    // $('.c2').mouseenter(function () {
    //     console.log('得港绿了');
    // });
    // 鼠标悬浮事件
    // $('.c2').mouseover(function () {
    //     console.log('得港绿了');
    // });
    // mouseover 和 mouseenter的区别是：mouseover事件是如果该标签有子标签，那么移动到该标签或者移动到子标签时会连续触发，mmouseenter事件不管有没有子标签都只触发一次，表示鼠标进入这个对象


//键盘按下触发的事件  e\event事件对象
    $(window).keydown(function (e) {
        // console.log(e.keyCode); //每个键都有一个keyCode值,通过不同的值来触发不同的事件
        if (e.keyCode === 37){
            $('.c1').css({'background-color':'red'});
        }else if(e.keyCode === 39){
            $('.c1').css({'background-color':'green'});
        }
        else {
            $('.c1').css({'background-color':'black'});
        }
    })
    // 键盘抬起触发的事件
    $(window).keyup(function (e) {
        console.log(e.keyCode);
    })

	
	input事件:
        22期百度:<input type="text" id="search">
        <script src="jquery.js"></script>
        <script>
            $('#search').on('input',function () {
                console.log($(this).val());
            })

        </script>

```

### 事件冒泡

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        #d1{
            background-color: red;
            height: 200px;
        }
        #d2{
            background-color: green;
            height: 100px;
            width: 100px;
        }

    </style>

</head>
<body>

<div id="d1">
    <div id="d2"></div>

</div>


<script src="jquery.js"></script>
<script>
    $('#d1').click(function () {
        alert('父级标签');
    });
    $('#d2').click(function () {
        alert('子级标签');
    });
    

</script>

</body>
</html>
```

### 阻止后续事件发生

```
    $('#d1').click(function () {
        alert('父级标签');
    });
    $('#d2').click(function (e) {
        alert('子级标签');
        return false;
        // e.stopPropagation();
    });

```



### 事件委托

```
事件委托是通过事件冒泡的原理，利用父标签去捕获子标签的事件，将未来添加进来的某些子标签自动绑定上事件。

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<div id="d1">
    <button class="c1">爱的魔力转圈圈</button>

</div>

<script src="jquery.js"></script>
<script>
    // $('.c1').on('click',function () {
    //     alert('得港被雪飞调教了,大壮很难受!');
    //     var btn = document.createElement('button');
    //     $(btn).text('爱的魔力转圈圈');
    //     $(btn).addClass('c1');
    //     console.log(btn);
    //     //添加到div标签里面的后面
    //     $('#d1').append(btn);
    //
    // });

	#将'button' 选择器选中的标签的点击事件委托给了$('#d1');
    $('#d1').on('click','button',function () {
        alert('得港被雪飞调教了,大壮很难受!');
        var btn = document.createElement('button');
        $(btn).text('爱的魔力转圈圈');
        $(btn).addClass('c1');
        console.log(btn);
        console.log($(this)) //还是我们点击的那个button按钮
        //添加到div标签里面的后面
        $('#d1').append(btn);

    });


</script>
</body>
</html>
```



页面载入和window.onload

```js
1. jquery文件要在使用jquery的代码之前引入

2. js代码最好都放到body标签下面或者里面的最下面来写

3.window.onload
	// window.onload = function () {
    //     $('.c1').click(function () {
    //         $(this).css({'background-color':'green'});
    //     })
    // }
4.页面载入,$(function (){alert('xx');}) -- $(document).ready(function(){});
	页面载入与window.onload的区别
　　　　1.window.onload()函数有覆盖现象，必须等待着图片资源加载完成之后才能调用
　　　　2.jQuery的这个入口函数没有函数覆盖现象，文档加载完成之后就可以调用（建议使用此函数）
　　　　
示例:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="jquery.js"></script>
    <script>
        // 等待整个页面中的内容全部加载完成之后,触发window.onload对应的函数里面的内容
        // window.onload 有覆盖现象,会被后面的window.onload给重新赋值
        // window.onload = function () {
        //     $('.c1').click(function () {
        //         $(this).css({'background-color':'green'});
        //     })
        // }

        
        $(function () {
            $('.c1').click(function () {
                $(this).css({'background-color':'green'});
            })
        });

    </script>
    <script src="xx.js"></script>


    <style>
        .c1{
            background-color: red;
            height: 200px;
            width: 200px;
        }
    </style>
</head>
<body>

<div class="c1"></div>

<img src="" alt="">


</body>

</html>
　　　　

```

















### 　　










































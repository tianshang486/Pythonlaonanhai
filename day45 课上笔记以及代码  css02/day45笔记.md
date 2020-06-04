# 昨日内容回顾

## 选择器

### 基本选择器

```
元素选择器 p{color:red;}
id选择器 #d1{color:red;}
类选择器 .c1{color:red;}

通用选择器 *{}
组合选择器 
	后代选择器     选择器 选择器{}
	儿子选择器  选择器>选择器{}
	毗邻选择器  选择器+选择器{}
	弟弟选择器  选择器~选择器{}
属性选择器
	[属性名] --- [title]
	[属性名=属性值] --- [title=xxx]
伪类选择器
	a:hover{}  鼠标悬浮
	a:link{}   为未问的a标签
	a:active{} 点击瞬间设置的效果
	a:visited{} 已访问连接设置效果
	input:focus{}   获取焦点时设置的样式
伪元素选择器
	选择器:first-letter 首字母
	选择器:before  选择器对应标签内部前面插入一些内容
	选择器:after  选择器对应标签内部后面插入一些内容
分组选择器 选择器,选择器,选择器....{}
		
选择器优先级
	继承    0
	元素    1
	类      10
	id      100
	内敛     1000
    最牛逼   !important  color:red!important;
	
    
```



## css属性相关

### 字体属性

```
字体  font-family:'宋体'
字体大小  font-size:48px; 默认16px
字体颜色  color:red;
	     color:#ffffff
	     color:rgb(0,0,0)
	     color:rgba(0,0,0,0.3) 0.3透明度
子重   font-weight:bold; 100-900的数字
字体对齐 text-align:left;right;center
文字装饰:text-decoration:none;underline;overline;line-through;
首行缩进:text-indent:32px;  16px

```



### 背景属性

```
背景颜色  background-color:red;
背景图片  background-image:url('图片路径')
背景平铺  background-repeat:no-repeat;
图片位置  background-position:100px 50px; 距离左100px,距离上50px;
图片位置  background-position:right bottom;
简写:background:red url('路径') no-repeat 100px 50px;
###background-attachment:fixed;  固定在屏幕的某个位置上
```



# 今日内容

## 边框

```css
	div{
            
            width: 200px;
            height: 200px;
            /*border-style: solid;*/  边框样式
            /*border-color: red;*/    边框颜色
            /*border-width: 10px;*/   边框宽度
            /*border:10px solid red;*/  简写方式

            
            
            /*border-left-style: solid;*/
            /*border-left-width: 10px;*/

            /*border-right-style: dashed;*/
            /*border-top-style: dashed;*/
            /*border-bottom-style: dashed;*/
            /*border-right-width: 5px;*/
            border-left:10px solid red;  单独设置边框的简写方式

        }

控制圆角
	border-radius: 50%;  
```



## display属性

```cs
        div{
            width: 100px;
            height: 100px;
            border: 1px solid red;
            /*display: inline;  !* 将标签设置为内敛标签 *!*/
            /*display: inline-block;  !* 将标签设置为同时具备内敛和块级标签的一些特性,比如可以设置高度宽度,但是不独占一行 *!*/
            /*display: none;  !* 隐藏标签 ,并且不占用自己之前的空间*!*/

        }
        span{
            border: 2px solid blue;

        }

        .c1{
            width: 200px;
            height: 200px;
            /*display: inline-block;*/  
            display: block; /* 将内敛标签设置为块级标签 */
        }
        
     值	           意义
     display:"none"	HTML文档中元素存在，但是在浏览器中不显示。一般用于配合JavaScript代码使用。
     display:"block"	默认占满整个页面宽度，如果设置了指定宽度，则会用margin填充剩下的部分。
     display:"inline"	按行内元素显示，此时再设置元素的width、height、margin-top、margin-  bottom和float属性都不会有什么影响。
     display:"inline-block"	使元素同时具有行内元素和块级元素的特点。   
	
	
隐藏标签
	visibility: hidden; /* 隐藏标签,但是标签还占用原来的空间 */
    /*display: none;  !* 隐藏标签 ,并且不占用自己之前的空间*!*/
```



## css盒子模型

```css
content内容区域  
padding 内边距
border 边框宽度
	div{
            width: 200px;
            height: 100px;
            border: 2px solid deeppink;
            /*padding-top: 10px;*/
            /*padding-left: 5px;*/
            /*padding-right: 2px;*/
            /*padding-bottom: 4px;*/
            /*padding: 10px 20px;  !* 10px上下内边距 ,20px左右内边距 *!*/
            /*padding: 10px 20px 5px 2px;  !* 10px上下内边距 ,20px左右内边距 *!*/
            padding: 10px 20px 5px 0;  /* 10px上下内边距 ,20px左右内边距 */
            
        }

margin 外边距
top距离上面标签的距离
bottom距离下面标签的距离
left 距离左边标签的距离
rigth 距离右边标签的距离

        .d1 {
            width: 200px;
            height: 100px;
            border: 2px solid deeppink;
            margin-bottom: 200px;  
        }
		.d2{
            margin-top: 100px;  
            border: 2px solid blue;

        }

	两个简写的方式
	/*margin: 10px 20px;*/
	margin: 10px 5px 6px 3px;

	两个情况:
		垂直方向如果上下两个标签都设置了margin外边距,那么取两者的最大的值
		水平方法,两个标签都设这外边距,取两者的边距之和


```



## 浮动float

```css
	.c1{
            background-color: red;
            height: 100px;
            width: 100px;
            float: left;
        }
        .c2{
            background-color: blue;
            height: 100px;
            width: 100px;
            float: right;
        }
        
浮动会造成父级标签塌陷问题
解决方法:
	1 父级标签设置高度
	2 伪元素选择器清除浮动,给父级标签加上下面这个类值
		.clearfix:after{
            content: '';
            display: block;
            clear: both;  清除浮动clear
        }
        
clear的值和描述        
	值	描述
	left	在左侧不允许浮动元素。
	right	在右侧不允许浮动元素。
	both	在左右两侧均不允许浮动元素。
```

## overflow溢出属性 

```css
 	.c1{
            width: 200px;
            height: 200px;
            border: 1px solid red;
            /*overflow: hidden;*/
            overflow: auto;  
        }
	<div class="c1">
    	总结一下：为什么要有浮动啊，是想做页面布局，但是浮动有副作用，父级标签塌陷，所以要想办法去掉这个副作用，使用了clear来清除浮动带来的副作用，我们当然也可以通过设置标签为inline-block来实现这种布局效果，但是把一个块级标签变成一个类似内敛标签的感觉，不好操控，容易混乱，所以一般都用浮动来进行布局。
	</div>

值	描述
visible	默认值。内容不会被修剪，会呈现在元素框之外。
hidden	内容会被修剪，并且其余内容是不可见的。
scroll	内容会被修剪，但是浏览器会显示滚动条以便查看其余的内容。
auto	如果内容被修剪，则浏览器会显示滚动条以便查看其余的内容。
```



圆形头像示例

```
<!DOCTYPE HTML>
<html>
<head>
  <meta charset="UTF-8">
  <meta http-equiv="x-ua-compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>圆形的头像示例</title>
  <style>

    .header-img {
      width: 150px;
      height: 150px;
      border: 3px solid white;
      border-radius: 50%;
      overflow: hidden;
    }
    
    .header-img>img {
        width: 100%;  #让img标签按照外层div标签的宽度来显示

    }
  </style>
</head>
<body>

<div class="header-img">
  <img src="meinv.png" alt="">
</div>

</body>
</html>
```

总结一点:width宽度设置的时候,直接可以写100px,30%这种百分比的写法,它的宽度按照父级标签的宽度的百分比来计算.

定位position:相对定位和绝对定位

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
            background-color: blue;
            height: 100px;
            width: 100px;
            /*position: relative;  !*相对定位,保留原来的空间位置,相对自己原来的位置移动,以左上角为基准*!*/

            /*top: 20px; 往下移20px,距离原来位置的上边框20px */
            /*top: -20px;*/
            /*left: 20px;*/
            /*right: ;*/
            /*bottom: ;*/

            position: absolute; /* 绝对定位,不保留自己原来的位置,按照父级标签或者祖先级标签..设置了position为 relative的标签的位置进行移动,如果一直找不到设置了设个属性的标签,那么按照body标签来移动 */

            top: 20px;
            left: 20px;
        }
        .c3{
            background-color: green;
            height: 100px;
            width: 100px;
        }
        .ccc{
            height: 100px;
            width: 200px;
            background-color: purple;
        }
        .cc{
            position: relative;
            left: 200px;
        }
    </style>
</head>
<body>
<div class="ccc"></div>
<div class="cc">
    <div class="c1"></div>
    <div class="c2"></div>
    <div class="c3"></div>
</div>

</body>
</html>
```



回到顶部示例:position为fixed固定定位,通过相对于浏览器窗口的距离来设置位置.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .c1{
            background-color: red;
            height: 500px;
            width: 200px;
        }
        .c2{
            background-color: green;
            height: 500px;
            width: 200px;
        }

        .s1{
            position: fixed; /*固定定位,位置是根据浏览器窗口来的*/
            /*top:20px;*/
            left: 20px;
            bottom: 20px;
            background-color: blue;
            height: 40px;
            width: 80px;
            text-align: center;

            line-height: 40px; /* 和标签高度一致,标签内容就垂直居中 */

        }
        .s1 a{
            color: white;
            text-decoration: none;
        }
    </style>
</head>
<body>

<!--<a name="top">这里是顶部,亲爱的</a>-->  <!-- 锚点 -->
<div id="top">这是顶部</div> <!-- 锚点 -->

<div class="c1"></div>
<div class="c2"></div>

<span class="s1">
    <a href="#top">回到顶部</a> <!-- 触发锚点 -->
</span>

</body>
</html>


锚点设置的两种方式
	<!--<a name="top">这里是顶部,亲爱的</a>-->  <!-- 锚点 -->
	<div id="top">这是顶部</div> <!-- 锚点 -->
触发锚点的a标签写法
<a href="#top">回到顶部</a> <!-- 触发锚点 -->
```



## z-index控制层级

模态对话框示例:

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .shadow{
            position: fixed;
            top:0;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: rgba(0,0,0,0.5);
            z-index: 99;
        }
        .mode{
            position: fixed;
            height: 400px;
            width: 300px;
            background-color: white;
            z-index: 100;  /* 数值越大越在上层显示 */
            left: 50%;  /* 按照窗口宽度的50%来移动 */
            top:50%;    /* 按照窗口高度的50%来移动 */
            margin-left: -150px;
            margin-top: -200px;

        }

    </style>
</head>
<body>

<div>
    <h1>
        22期,吴老板唱歌
    </h1>
</div>


<div class="mode">

</div>

<div class="shadow">

</div>


</body>
</html>
```



## opacity透明度

```
        .c1{
            background-color: rgba(255,0,0,0.3); /* 背景颜色或者字体颜色等单独的透明度 */
            height: 100px;
            width: 100px;
        }
        .c2{
            background-color: rgb(255,0,0);
            height: 100px;
            width: 100px;
            opacity: 0.3;  /* 整个标签透明度 */
        }
<div class="c1">
    你好
</div>
<div class="c2">
    我好
</div>

```






















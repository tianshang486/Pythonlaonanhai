

# 昨日内容回顾

## HTML

### 标签分类

内敛标签:不独占一行,只能嵌套内敛标签

块级标签:独占一行,能嵌套内敛标签和某些块级标签

### 标签封闭

```html
<img >  自封闭
<div></div> 全封闭
```

### head标签

​	meta标签,title标签

### body标签

```html
h1-h6  b u s i p span div br hr img a form input button table ul li ol li select label
textarea dl dt dd 
特殊符号 &nbsp;空格...

```

#### input

```html
type属性
text password date radio checkbox file submit reset button hidden 

name属性 分组,提交数据时的key,提交的数据value

value属性 指定默认值

默认选中  checked属性

readonly 只读
disabled 禁用

```



#### table

```html
<table border="1" cellpadding="1" cellspacing="1">
        <thead>
            <tr>
                <th>姓名</th>
                <th>年龄</th>
                <th>爱好</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>alexdsb</td>
                <td>84</td>
                <td>吹牛逼</td>
            </tr>
        </tbody>
    </table>
```

#### form表单

```html
    <form action="地址">
        <input type="text" name="username">

        <input type="radio" name="sex" value="1">
        <input type="radio" name="sex" value="2">
        <input type="submit">
        <button>提交</button>
    </form>
```

#### img

```html
    <img src="图片地址" alt="图片未加载成功的提示信息" title="鼠标悬浮的提示信息" width="1" height="1">
```

#### a

```html
    <a href="超链接地址" target="_blank"></a>
    <a href="超链接地址" target="_self"></a>
```

#### select下拉框

```html
    <select name="city" multiple>
        <option value="1">上海</option>
        <option value="2" selected>深圳</option>
        <option value="2">惠州</option>
    </select>
selected默认选中
multiple 多选
```

#### label标签

```html
        <label for="username1">用户名</label>
        <input type="text" name="username1" id="username1">

        <label>
            <input type="text" name="username2" id="username2">
        </label>
```

#### textarea 文本输入框

```html
<textarea name="" id="" cols="30" rows="10"></textarea>
```



# 今日内容

CSS选择器(**C**ascading **S**tyle **S**heet，层叠样式表)

css代码写法:  h1{color:red;}  选择器{css属性:属性值;}

css代码引入

```html
方式1
	head标签里面写
	<style>
        div{
            background-color: red;
            height: 100px;
            width: 100px;
        }
    </style>
方式2
	内敛样式:
	<div style="background-color: blue; height: 200px;width: 200px;"></div>
方式3 
	外部文件引入
	head标签里面写link标签
	<link rel="stylesheet" href="文件路径">
```



## css选择器

### 基本选择器

```html
元素选择器:
	div{  #标签名字
         color:red;
	}
id选择器:id值不能重复
	<div id="xuefei">
    	雪飞大美女
	</div>
	
	#xuefei{  
		color:green;
	}
类选择器: 类值可以重复
	<div id="dazhuang" class="c1">
    	大壮dsb
	</div>
	<div id="xuefei" class="c1">
    	雪飞大美女
	</div>
	
	.c1{
		color: green;
	}
	
	div.c1{ #div标签里面含有class值为c1的标签
		color: green;
	}
通用选择器
*{ #找到所有的标签
	color: green;
}

```



### 组合选择器

#### 后代选择器

```
div a{   #找到div标签后代里面的所有a标签
	color:red;
}
```

#### 儿子选择器

```
div>a{ #找到div的儿子标签这一代的a标签
	color:red;
}
```

#### 毗邻选择器

```
div+a{  #找到是紧挨着div标签的下一个标签(是兄弟标签)
	 color: red;
}
```

#### 弟弟选择器

```
div~a{  #找到的是同级的后面的所有兄弟标签
	color: red;
}
```



### 属性选择器

```html
	#通过属性名来查找
	[title]{ #找到所有含有title属性的标签  
		color: red;
	}
	
	div[title]{  #含有title属性的div标签
		color: red;
	}
	#通过属性名对应的值来查找,当属性值的值为数字的时候,数字要加上引号[title='666']
	input[type=text]{ #含有type属性,并且type属性的值为text的input标签
		background-color: red;
	}
```

### 分组

```
多个选择器选择的标签设置相同css样式的时候,就可以用分组
div,p{  #div选择器和p选择器共同设置相同的样式,可以逗号分隔
	color:red;
}
```

### 伪类选择器

```html
a标签自带的效果:未访问过的时候是蓝色的字体颜色,访问过之后是紫色的,自带下划线

/* 未访问的链接 */
a:link {
  color: #FF0000
}

/* 已访问的链接 */
a:visited {
  color: #00FF00
} 

/* 鼠标移动到链接上 */  这个用的比较多,可以应用在其他标签上
a:hover {  
  color: #FF00FF
} 

/* 选定的链接 */ 就是鼠标点下去还没有抬起来的那个瞬间，可以让它变颜色
a:active {
  color: #0000FF
}

/*input输入框获取焦点时样式*/
input:focus {   #input默认的有个样式，鼠标点进去的时候，input框会变浅蓝色的那么个感觉
  #outline: none;
  background-color: #eee; #框里面的背景色
}
```

### 伪元素选择器

```css
 		/*伪元素选择器*/
        div:first-letter{
            color: red;
            font-size: 20px;
        }
        /*在p标签内容的前面插入一些内容*/
        p:before{
            content: '?';
            color: green;
            font-size:100px;
        }
        /*在p标签内容的后面插入一些内容*/
        p:after{
            content: '哈哈!';
            color: pink;
        }
```



### 选择器的优先级

```html
      /*优先级数字越大,越优先显示其效果,优先级相同的,显示后面定义的选择器对应的样式*/
        /*id选择器优先级为100*/
        /*#d1{*/
            /*color:deepskyblue;*/
        /*}*/
        /*!*继承的优先级为0*!*/
        /*body{*/
            /*color:red;*/
        /*}*/
        /*!*类选择器的优先级是10*!*/
        /*.c1{*/
            /*color: blue;*/
        /*}*/
        /*.c2{*/
            /*color: orange;*/
        /*}*/
        /*!*元素选择器优先级是1*!*/
        /*div{*/
            /*color: green;*/
        /*}*/
        内敛样式优先级为1000
        <p class="cc3" style="color: red;">我是cc3的p标签</p>
        
        important优先级最高,最牛逼
        .cc1 .cc3 {
            color: purple!important;
        }
```



## css属性相关

高度宽度设置,注意:只有块级标签能够设置高度宽度,内敛标签不能设置高度宽度,它的高度宽度是由内容决定的

```
	div{
            width: 100px;  宽度
            height: 100px; 高度
            background-color: pink;
        }
```



补充:a标签的字体颜色设置必须选中a标签才行

```
.c1 a{  
	color: red;
}
```



### 字体属性

#### 字体

```
.c1{
	font-family: '楷体','宋体','微软雅黑';
}
```

#### 字体大小

```
.c1{
            /*font-family: '楷体','宋体','微软雅黑';*/
            font-size:14px; 默认字体大小为16px.
            
        }
```

#### 字体颜色

```
color:red;
```

#### 子重,粗细

```
 .c1{
           
            font-weight: bold;
            font-weight: 100;
        }
        

值	描述
normal	默认值，标准粗细
bold	粗体
bolder	更粗
lighter	更细
100~900	设置具体粗细，400等同于normal，而700等同于bold

```

#### 颜色表示方式

```css
		p{
            /*color: red;*/
            /*color: #78FFC9;*/
            /*color: rgb(123,199,255);*/
             color: rgba(123,199,255,0.3);  多了一个透明度的数字:0-1的一个数字
        }
```

### 文字属性

#### 文字对齐

```css
	text-align
	
	div{
            width: 200px;
            height: 200px;
            background-color: yellow;
            /*text-align: center;*/
            text-align: right;
        }
        
	left	左边对齐 默认值
	right	右对齐
	center	居中对齐
```

#### 文字装饰

```
	text-decoration
	
	div a{
            /*text-decoration: none;*/  #给a标签去除下划线
            /*text-decoration: line-through;*/
            text-decoration: overline;
        }
	值	描述
	none	默认。定义标准的文本。
	underline	定义文本下的一条线。
	overline	定义文本上的一条线。
	line-through	定义穿过文本下的一条线。
```

#### 首行缩进

```
p {
  text-indent: 32px; #首行缩进两个字符，因为我记得一个字在页面上的默认大小为16px
}
```



### 背景属性

```css
背景颜色
background-color: red;

	div{
            width: 600px;
            height: 600px;
            /*background-color: red;*/
            /*background-image: url("yeye.jpg");*/
            /*background-repeat: no-repeat;*/
            /*background-position: 100px 50px;*/  相对于div标签的,距离左边100px,距离上面50px
            background:url("yeye.jpg") no-repeat left center;
            /*background-position: right top;*/

        }
简写方式,颜色  图片路径 是否平铺 图片位置
background:#ffffff url('1.png') no-repeat right top;
        
```










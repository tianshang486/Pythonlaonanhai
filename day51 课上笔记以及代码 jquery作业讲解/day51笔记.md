# 昨日内容回顾

## 事件

### 事件绑定方式

```
方式1
	$('div').click(function(){});
方式2
	$('div').on('click',function({}));

```

### 常用事件

```
click
focus
blur
change
hover
mouseenter
mouseout
mouseover
keydown
keyup  -- 事件对象.keyCode
```

### 事件冒泡

```
子标签事件触发之后,会连带触发父标签及上层标签的事件
```

### 阻止后续事件发生

```
return false;
e.stopPropagation()
```

### 事件委托

```
将事件委托给上层标签
上层标签对象.on('click','委托人选择器',function(){});
```

### 页面载入

```
window.onload = function(){};  
	存在覆盖现象
	等页面中所有内容加载完成之后,执行
$(function(){})
$(document).ready(function(){});  
	不存在覆盖现象
	并且不等待图片\视频等内容的加载
```



# 今日内容

## 动画效果



## each循环

```js
循环标签对象数组
$('li').each(function(k,v){
	console.log(k,v);
});

循环普通数组
var d1 = ['aa','bb','cc'];
$.each(d1,function(k,v){
	console.log(k,v);
})

跳出循环  return false; 类似于break
$('li').each(function(k,v){
	console.log(k,v.innerText);
	if (k === 1){
		return false;
	}

});

跳出本次循环  return; 类似于continue
$('li').each(function(k,v){
	
	if (k === 1){
		return;
	}
	console.log(k,v.innerText);
});

```



## data

```
给标签对象添加数据,类似于添加了全局变量
	.data(key, value): 设置值
	.data(key)   取值
	.removeData(key) 删除值
```

### 插件(了解)

```js
<script>
jQuery.extend({ //$.extend({})
  min:function(a, b){return a < b ? a : b;}, //自定义了一个min和max方法，min和max作为键，值是一个function
  max:function(a, b){return a > b ? a : b;}
});
jQuery.min(2,3);// => 2
jQuery.max(4,5);// => 5
$('div').min(1,2);不能通过标签对象来调用
</script>

<script>
  jQuery.fn.extend({  //给任意的jQuery标签对象添加一个方法
    check:function(){
      return this.each(function(){this.checked =true;});
    },
    uncheck:function(){
      return this.each(function(){this.checked =false;});
    }
  });
// jQuery对象可以使用新添加的check()方法了。
$("input[type='checkbox']").check();
</script>

```
























































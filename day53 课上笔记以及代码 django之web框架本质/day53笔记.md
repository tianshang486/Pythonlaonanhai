# 今日内容

```
http协议  超文本传输协议
请求  和   响应

请求格式
    GET / HTTP/1.1  ---  GET /clschao/articles/9230431.html?name=chao&age=18 HTTP/1.1
    User-Agent:....
    xx:xx

    请求数据  get请求方法没有请求数据  post请求数据方法的请求数据放在这里

响应格式
    HTTP/1.1 200 ok
    kl:v1
    k2:v2

    响应数据

URL:  https://www.cnblogs.com/clschao/articles/9230431.html
    传送协议。
    层级URL标记符号(为[//],固定不变)
   
    服务器。（通常为域名，有时为IP地址）
    端口号。（以数字方式表示，若为HTTP的默认值“:80”可省略）
    路径。（以“/”字符区别路径中的每一个目录名称）  /clschao/articles/9230431.html
    查询。（GET模式的窗体参数，以“?”字符为起点，每个参数以“&”隔开，再以“=”分开参数名称与数据，通常以UTF8的URL编码，避开字符冲突的问题）
    https://www.cnblogs.com/clschao/articles/9230431.html?name=chao&age=18
    

请求方法
	get post
    GET提交的数据会放在URL之后，也就是请求行里面，以?分割URL和传输数据，参数之间以&相连，如EditBook?name=test1&id=123456.（请求头里面那个content-type做的这种参数形式，后面讲） POST方法是把提交的数据放在HTTP包的请求数据部分中.
    GET提交的数据大小有限制（因为浏览器对URL的长度有限制），而POST方法提交的数据没有限制.
    GET与POST请求在服务端获取请求数据方式不同，就是我们自己在服务端取请求数据的时候的方式不同了

	常用的get请求方式:浏览器输入网址  ,a标签 ,form标签 method='get'
	post请求方法,一般都用来提交数据.比如用户名密码登录	

	其他方法:HEAD PUT DELETE TRACE OPTIONS CONNECT PATCH

响应状态码 
    1xx消息——请求已被服务器接收，继续处理
    2xx成功——请求已成功被服务器接收、理解、并接受
    3xx重定向——需要后续操作才能完成这一请求
    4xx请求错误——请求含有词法错误或者无法被执行
    5xx服务器错误——服务器在处理某个正确请求时发生错误

http协议特点
	1.基于  请求-响应 的模式
	2.无状态保存
	3.无连接  

请求:request
响应:response

```




















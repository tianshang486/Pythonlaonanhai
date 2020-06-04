# 环境变量
# python -->python.exe
# 在任何目录下都能够找到python.exe文件
# 才能在任意位置输入python命令启动python解释器

# mysqld install  安装mysql服务  mysql服务就被注册到操作系统中
# net start mysql 启动mysql服务
# net stop mysql

# 启动客户端连接server
# mysql -uroot -p123 -h192.168.14.12

# mysql>select user();   查看当前登录的用户
# mysql>set password = password('123'); 给当前用户设置密码
#
# 创建一个其他用户
# create user 'guest'@'192.168.14.%' identified by '123';
# 给一个用户授权
# grant 权限类型 on ftp.* to 'guest'@'192.168.14.%';
# grant all
# grant select on day37.* to 'guest'@'192.168.14.%';
# grant select,insert


# 操作数据库
# 查看所有数据库  show databases;
# 创建一个数据库  create database 数据库名;
# 切换到这个库下  use 数据库的名字
# 查看这个库下有多少表 show tables;

# 操作表
# 创建一张表
# create table student(name char(12),age int);
# 查看表结构
# desc student;

# 操作数据
# 插入数据 : insert into student values ('wusir',73);
# 查询数据 : select * from student;
# 修改数据 : update student set age=85 where name='alex';
# 删除数据 : delete from student where name = 'alex';
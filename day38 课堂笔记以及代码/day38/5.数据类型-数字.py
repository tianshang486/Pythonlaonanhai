# int 不约束长度,最多表示10位数
# float(m,n)
    # m 一共多少位,
    # n 小数部分多少位

# create table t1(
#     id int,               # 默认是有符号的
#     age tinyint unsigned  # 如果需要定义无符号的使用unsigned
# );

# create table t2(
#   f1 float(5,2),   # 保留2位小数 并四舍五入
#   f2 float,
#   f3 double(5,2),
#   f4 double
# )

# insert into t2(f2,f4) values(5.1783682169875975,5.1783682169875975179);

# create table t3(
#   f1 float,   # 保留2位小数 并四舍五入
#   d1 double,
#   d2 decimal(30,20),
#   d3 decimal
# );
# insert into t3 values(5.1783682169875975179,5.1783682169875975179,
#                       5.1783682169875975179,5.1783682169875975179);
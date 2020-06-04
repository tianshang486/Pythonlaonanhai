# 1.select语句
# 最简单的select
    # select * from 表;
    # select 字段,... from 表;
# 重命名字段
    # select 字段 as 新名字,... from 表;
    # select 字段 新名字,... from 表;
# 去重
    # select distinct 字段 from 表;
    # select distinct age,sex from employee;
# 使用函数
    # concat
    # concat_ws
# 四则运算的
    #  select emp_name,salary*12 from employee; 乘法
    #  select emp_name,salary*12 as annual_salary from employee;
# 使用判断逻辑
    # case when语句 相当于 if条件判断句

# where 筛选所有符合条件的行
    # 比较运算符
        # > < >= <= <> !=
    # 范围
        # between 10000 and 20000 要1w-2w之间的
        # in (10000,20000)   只要10000或者20000的
    # 模糊匹配
        # like
            # % 通配符 表示任意长度的任意内容
            # _ 通配符 一个字符长度的任意内容
        # regexp
            # '^a'
            # 'g$'
    # 逻辑运算
        # not\and\or

# 查看岗位描述不为NULL的员工信息
    # is
    # select * from employee where post_comment is not null;
# 查看岗位是teacher且薪资不是10000或9000或30000的员工姓名、年龄、薪资
    # select emp_name, age, salary
    # from employee wherepost = 'teacher' and salary not in(10000,9000,30000)
# 查看岗位是teacher且名字是jin开头的员工姓名、年薪
    #  select emp_name,salary*12 from employee where post = 'teacher' and emp_name like 'jin%';

# 分组 group by 根据谁分组,可以求这个组的总人数,最大值,最小值,平均值,求和 但是这个求出来的值只是和分组字段对应
    # 并不和其他任何字段对应,这个时候查出来的所有其他字段都不生效.
# 聚合函数
    # count 求个数
    # max  求最大值
    # min  求最小值
    # sum  求和
    # avg  求平均

    # SELECT post,emp_name FROM employee GROUP BY post;
    # SELECT post,GROUP_CONCAT(emp_name) FROM employee GROUP BY post;

# having 过滤语句
    # 在having条件中可以使用聚合函数,在where中不行
    # 适合去筛选符合条件的某一组数据,而不是某一行数据
    # 先分组再过滤 : 求平均薪资大于xx的部门,求人数大于xx的性别,求大于xx人的年龄段
# 查询各岗位内包含的员工个数小于2的岗位名、岗位内包含员工名字、个数
# group by post having count(id) < 2;

# 排序 order by
    # 默认是升序  asc
    # 降序  desc
    # order by age ,salary desc
        # 优先根据age从小到大排,在age相同的情况下,再根据薪资从大到小排

# limit m,n
    # 从m+1项开始,取n项
    # 如果不写m,m默认为0

    # limit n offset m
# 查询平均年龄在25岁以上的部门名
# select name from department where id in (
#     select dep_id from employee group by dep_id having avg(age)>25);

# 查看技术部员工姓名
    # 先查询技术部的部门id
    # select id from department where name = '技术';
    # 再根据这个部门id找到对应的员工名
    # select name from employee where dep_id =(select id from department where name = '技术');
    # select name from employee where dep_id in (select id from department where name = '技术');

# 查看不足1人的部门名
    # 先把所有人的部门id查出来
    # select distinct dep_id from employee;
    # 然后查询部门表,把不在所有人部门id这个范围的dep_id找出来
    # select name from department where id not in (select distinct dep_id from employee);

# 查询大于所有人平均年龄的员工名与年龄
    # 求平均年龄
    # select avg(age) from employee;
    # select * from employee where age >28;
    # select name,age from employee where age >(select avg(age) from employee);

# 查询大于部门内平均年龄的员工名、年龄
    # select dep_id,avg(age) from employee group by dep_id;
    # select name,age from employee as t1 inner join (select dep_id,avg(age) avg_age from employee group by dep_id) as t2
    # on t1.dep_id = t2.dep_id where age>avg_age;


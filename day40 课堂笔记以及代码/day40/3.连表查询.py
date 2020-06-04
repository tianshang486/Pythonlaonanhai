# 所谓连表
    # 总是在连接的时候创建一张大表,里面存放的是两张表的笛卡尔积
    # 再根据条件进行筛选就可以了

# 表与表之间的连接方式
    # 内连接 inner join ... on ...
        # select * from 表1,表2 where 条件;(了解)
        # select * from 表1 inner join 表2  on 条件
        # select * from department inner join employee on department.id = employee.dep_id;
        # select * from department as t1 inner join employee as t2 on t1.id = t2.dep_id;
    # 外连接
        # 左外连接 left join ... on ...
            # select * from 表1 left join 表2 on 条件
            # select * from department as t1 left join employee as t2 on t1.id = t2.dep_id;
        # 右外连接 right join ... on ...
            # select * from 表1 right join 表2 on 条件
            # select * from department as t1 right join employee as t2 on t1.id = t2.dep_id
        # 全外连接 full join
            # select * from department as t1 left join employee as t2 on t1.id = t2.dep_id
            # union
            # select * from department as t1 right join employee as t2 on t1.id = t2.dep_id;

# 1.找到技术部的所有人的姓名
# select * from department d inner join employee e on e.dep_id = d.id;
# select e.name from department d inner join employee e on e.dep_id = d.id where d.name='技术';

# 2.找到人力资源部的年龄大于40岁的人的姓名
# select * from department d inner join employee e on e.dep_id = d.id
# select * from department d inner join employee e on e.dep_id = d.id where d.name='人力资源' and age>40;

# 3.找出年龄大于25岁的员工以及员工所在的部门
# select * from department d inner join employee e on e.dep_id = d.id;
# select e.name,d.name from department d inner join employee e on e.dep_id = d.id where age>25;

# 4.以内连接的方式查询employee和department表，并且以age字段的升序方式显示
# select * from department d inner join employee e on e.dep_id = d.id order by age;

# 5.求每一个部门有多少人
# select d.name,count(e.id) from department d left join employee e on e.dep_id = d.id group by d.name;
# 且按照人数从高到低排序
# select d.name,count(e.id) c from department d left join employee e on e.dep_id = d.id group by d.name order by c desc;

# 所谓连表就是把两张表连接在一起之后 就变成一张大表  从from开始一直到on条件结束就看做一张表
# 之后 where 条件 group by 分组 order by limit 都正常的使用就可以了
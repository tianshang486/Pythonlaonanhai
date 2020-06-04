# create table t1(
#   id int primary key auto_increment,
#   username char(12) not null,
#   sex enum('male','female') default 'male',
#   hobby set('上课','写作业','考试') not null
# );

# 增 insert into 表(字段,...) values (值,...);
# insert into t1 value (1,'大壮','male','上课,写作业');
# insert into t1 values(2,'杜相玺','male','写作业,考试');
# insert into t1 values(3,'b哥','male','写作业'),(4,'庄博','male','考试');
# insert into t1(username,hobby) values ('杨得港','上课,写作业,考试'),('李帅','考试')
# insert into t2(id,name) select id,username from t1;

# 删
# 清空表
    # delete from 表;
        # 会清空表,但不会清空自增字段的offset(偏移量)值
    # truncate table 表;
        # 会清空表和自增字段的偏移量
# 删除某一条数据
    # delete from 表 where 条件;

# 改
    # update 表 set 字段=值 where 条件;
    # update 表 set 字段=值,字段=值 where 条件;


# 10个查询 1一个增删改











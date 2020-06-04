# 联合索引
# (id,email)
# id = 100 and email like 'eva%';

# 索引合并 :分开创建在查询过程中临时合并成一条 Using union(ind_id,ind_email)
    # 创建索引的时候
    # create index ind_id on s1(id)
    # create index ind_email on s1(email)
    # select * from s1 where id=100 or email = 'eva100@oldboy'
    # 临时把两个索引ind_id和ind_email合并成一个索引


# 覆盖索引:在查询过程中不需要回表   Using index
    # 对id字段创建了索引
    # select id from s1 where id =100     覆盖索引:在查找一条数据的时候,命中索引,不需要再回表
    # select count(id) from s1 where id =100     覆盖索引:在查找一条数据的时候,命中索引,不需要再回表
    # select max(id) from s1 where id =100     覆盖索引:在查找一条数据的时候,命中索引,不需要再回表
    # select name from s1 where id =100   相对慢

# 什么是mysql的执行计划?用过explain么?
    # 在执行sql语句之前,mysql进行的一个优化sql语句执行效率的分析(计划),可以看到有哪些索引,实际用到了那个索引,执行的type等级
    # id name email
    # select * from s1 where id = 1000000 and name=eva and email = 'eva1000000@oldboy';
        # 有没有索引
        # 有几个
        # 用哪一个索引比较效率高
    # explain select * from s1 where id = 1000000 and name=eva and email = 'eva1000000@oldboy';

#

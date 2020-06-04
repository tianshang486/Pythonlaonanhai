import pymysql

# conn = pymysql.connect(host='127.0.0.1',
#                        user='root',
#                        password="123",
#                        database='homework')
# cur = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 查询返回字典
# cur = conn.cursor()  # cursor游标
# cur.execute('select * from student;')
# print(cur.rowcount)   # 获取查出多少行,便于使用fetchone取所有结果
# for i in range(cur.rowcount):
#     ret = cur.fetchone()      # 获取一条结果
#     print(ret)

# try:
#     cur.execute('select * from student;')
#     ret = cur.fetchone()      # 获取一条结果
#     print(ret)
#     ret2 = cur.fetchmany(10)  # 获取多条结果
#     print(ret2)
#     ret3 = cur.fetchall()     # 获取全部结果
#     print(ret3)
# except pymysql.err.ProgrammingError as e:
#     print(e)
# cur.close()
# conn.close()


# 增加 删除 修改
# conn = pymysql.connect(host='127.0.0.1',
#                        user='root',
#                        password="123",
#                        database='homework')
# cur = conn.cursor()  # cursor游标
# try:
#     # cur.execute('insert into student values(18,"男",3,"大壮")')
#     # cur.execute('update student set gender = "女" where sid = 17')
#     cur.execute('delete from student where sid = 17')
#     conn.commit()
# except Exception as e:
#     print(e)
#     conn.rollback()     # 可以试一下 myisam
# cur.close()
# conn.close()

# 实际操作mysql的时候会遇到的一个问题

# 结合数据库 和python 写一个登录
# user = input('username :')
# pwd = input('password :')
# conn = pymysql.connect(host='127.0.0.1',
#                        user='root',
#                        password="123",
#                        database='day42')
# sql = 'select * from userinfo where user = %s and password = %s'
# cur = conn.cursor()
# cur.execute(sql,(user,pwd))
# print(cur.fetchone())

# sql注入
# select * from userinfo where user = "1869" or 1=1;-- " and password = "3714";









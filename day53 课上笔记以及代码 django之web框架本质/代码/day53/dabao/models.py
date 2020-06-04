import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123',
    database='day53',
    charset='utf8'
)

cursor = conn.cursor(pymysql.cursors.DictCursor)
sql = 'create table userinfo(id int primary key auto_increment,name char(10),age int not null);'
cursor.execute(sql)
conn.commit()
cursor.close()
conn.close()
















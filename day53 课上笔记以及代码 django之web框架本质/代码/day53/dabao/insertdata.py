
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
sql = 'insert into userinfo(name,age) values("dazhuang",18);'
cursor.execute(sql)
conn.commit()
cursor.close()
conn.close()



import pymysql

def showdata():
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='123',
        database='day53',
        charset='utf8'
    )
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = 'select * from userinfo;'
    cursor.execute(sql)
    data = cursor.fetchone()
    # print(data)
    conn.commit()
    cursor.close()
    conn.close()
    return data

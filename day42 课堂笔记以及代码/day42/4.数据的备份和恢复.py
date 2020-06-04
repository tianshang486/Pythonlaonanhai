# D:\python_22\day42\tmp.sql

# 表和数据的备份
    # 备份数据 在cmd命令行直接执行
    # mysqldump -uroot -p123 -h127.0.0.1 homework > D:\python_22\day42\tmp.sql

    # 恢复数据 在mysql中执行命令
    # 切换到一个要备份的数据库中
    # source D:\python_22\day42\tmp.sql

# 备份库
    # 备份
    # mysqldump -uroot -p123 --databases homework > D:\python_22\day42\tmp2.sql
    # 恢复
    # source D:\python_22\day42\tmp2.sql


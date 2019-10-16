import sqlite3
# 建立数据库对象，返回Connection对象
# 连接到数据库'E:\\SQLiteDatebase\\test.db'，
#如果test.db存在，则打开，不存在，则创建该数据库
# 返回sqlite3.connection对象
# con=sqlite3.connect('E:\\SQLiteDatebase\\test.db')
# con=sqlite3.connect('E:/SQLiteDatebase/test.db')
con=sqlite3.connect(r'E:\SQLiteDatebase\test.db')
# 创建游标对象
cur=con.cursor()

# 使用 Cursor 对象的 execute() 方法执行 SQL 命令返回结果集
# 调用 cur.execute()、cur.executemany()、cur.executescript()方法查询数据库
# cur.execute(sql)：——————执行 SQL 语句
# cur.execute(sql,参数)：————执行带参数的SQL 语句
# cur.executemany(sql,seq_of_parameters)：————根据参数执行多次 SQL 语句
# cur.executescript(sql_script)：————执行 SQL 脚本
    # 创建一个包含3个字段 id、sort、name的表 category:
cur.execute("create table categoty(id primary key, sort, name)")


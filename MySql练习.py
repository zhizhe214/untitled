#!/usr/bin/python3
import pymysql

# 打开数据库连接
db = pymysql.connect(host="127.0.0.1", user="root",password="sql2008",database="AAA",charset="utf8")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# SQL 删除语句
sql = "DELETE FROM EMPLOYEE WHERE FIRST_NAME = 'Mac' "
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交修改
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()

# 关闭数据库连接
db.close()
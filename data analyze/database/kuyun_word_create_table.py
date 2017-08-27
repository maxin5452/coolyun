#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
# 打开数据库连接

db= MySQLdb.connect(
        host='127.0.0.1',
        port = 3306,
        user='root',
        passwd='000000',
        db ='testdb',
        )
# 使用cursor()方法获取操作游标 
cursor = db.cursor()
# 如果数据表已经存在使用 execute() 方法删除表。
cursor.execute("DROP TABLE IF EXISTS WORD")
# 创建数据表SQL语句
sql = """CREATE TABLE WORD (
         name  CHAR(20) NOT NULL,
         file_stamp VARCHAR(100),
         file_time DATETIME,
         userUrl VARCHAR(250),
         region VARCHAR(30),
         rank INT UNSIGNED,
         count FLOAT )"""

cursor.execute(sql)
# 关闭数据库连接
db.close()

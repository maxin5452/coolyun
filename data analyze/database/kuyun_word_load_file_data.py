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

# SQL 插入语句
sql = """load data local infile \"../output0823-7/part-00000\" 
into table WORD(name,file_stamp, file_time, userUrl, region,rank,count);"""
#WORD(name，file_stamp, file_time, userUrl, region,rank,count)
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# 关闭数据库连接
db.close()

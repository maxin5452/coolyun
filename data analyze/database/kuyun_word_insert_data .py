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
sql = """INSERT INTO WORD(name,
         file_stamp, file_time, userUrl, region,rank,count)
         VALUES ('养老金好', 'news_1_20170823175927_0', '2017-08-23 17:59:27', 'he.people.com.cn/', 'news',1,1)"""
#养老金	news_1_20170823175927_0	'2017-08-23 17:59:27'	he.people.com.cn/	news	1	1
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

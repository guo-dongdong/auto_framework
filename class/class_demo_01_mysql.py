# -*- coding:utf-8 -*-
# @Time :2020-07-16 20:05
# @Email :876417305@qq.com
# @Author :yanxia
# @File :class_demo_01_mysql.PY

import pymysql
from pymysql.cursors import DictCursor

# 建立连接
# TODO:utf-8  -->  utf8
conn = pymysql.connect(host= '120.78.128.25',
                       port= 3306,
                       user= 'future',
                       password= '123456',
                       charset= 'utf8',
                       database= 'futureloan',
                       cursorclass=DictCursor)  #元组变成列表+字典
# print(conn)

# 建立游标   游标，数据库中一个重要的概念
cursor = conn.cursor()

# 执行sql语句
mobile = '15006005770'
# 传递参数的第一种方法，format   不要用format传递参数
# cursor.execute('select * from member where mobile_phone={};'.format(mobile))
# 2.args 参数
cursor.execute('select * from member where mobile_phone = %s;', args=[mobile])

# 获取游标结果
res = cursor.fetchall()     # 获取所有
# res = cursor.fetchone()     # 获取一个
# res = cursor.fetchmany()    # 获取两个
print(res)

# 关闭游标，关闭连接
cursor.close()
conn.close()



"""
数据库操作
1.建立连接      conn = pymysql.connect()
2.建立游标      cursor = conn.cursor()
3.执行sql语句   cursor.execute('')
4.获取结果      res = cursor.fetchall()
5.关闭游标+连接   cursor.close()/conn.close()
"""
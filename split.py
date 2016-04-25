#!/usr/bin/env python3

import pymysql

conn = pymysql.connect('localhost' , 'root' , 'root' , 'social1' , charset = 'utf8')
cur = conn.cursor()
table = 'qqplus'
# 取得条数
cur.execute("SELECT COUNT(*) FROM %s;" % table)
for each in cur:
    count = each[0]
for x in range(0 , count-1 , 10000000):
    print("现在生成表%s%d......" % (table , x/10000000+1))
    cur.execute("CREATE TABLE `%s%d` SELECT * FROM `%s` LIMIT %d,10000000;" % (table , x/10000000+1 , table , x))

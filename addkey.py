#!/usr/bin/env python3

import pymysql

conn = pymysql.connect('localhost' , 'root' , 'root' , 'social1' , charset='utf8')
table = 'house'

for num in range(1,3):
    print("当前表:%s%d" % (table , num))
    # 获取列名
    cur = conn.cursor()
    cur.execute("SELECT column_name FROM information_schema.columns WHERE table_schema='social1' and table_name='%s%d';" % (table , num))
    columns = []
    for each in cur:
        columns.append(each[0])
    # 获得已经加KEY的列名
    cur.execute("SHOW CREATE TABLE %s%d;" % (table , num))
    for each in cur:
        for column in columns:
            if each[1].find("KEY `%s`" % column)>=0:
                columns.remove(column)
    # 计算应该加KEY的列名
    columns = list(set(columns) & set(("Name" , "CtfId" , "Mobile" , "Tel" , "EMail")))
    # 开始加列名
    sql = "ALTER TABLE %s%d " % (table , num)
    for each in columns:
        sql += "ADD KEY `%s` (`%s`)," % (each , each)
    sql = sql[:-1]
    cur.execute(sql)
    cur.close()

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
    # 检测每列是否为空
    for column in columns:
        result = cur.execute("SELECT * FROM %s%d WHERE %s is not null and %s not regexp '^[[:blank:]]*$' LIMIT 1;" % (table , num , column , column))
        if result:
            print("%s列不为空!" % column)
            for each in cur:
                print(each)
        else:
            print("%s列为空!开始删除列..." % column)
            cur.execute("ALTER TABLE %s%d DROP COLUMN %s;" % (table , num , column))
            print("删除完毕!")
    cur.close()

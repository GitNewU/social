#!/usr/bin/env python3

import pymysql

conn = pymysql.connect('localhost','root','root','social1',charset='utf8')

for num in range(1,42):
    cur = conn.cursor()
    result = cur.execute("SELECT * FROM soyun%d WHERE %s IS NOT NULL AND %s NOT REGEXP '^[[:blank:]]*$' LIMIT 10;" % (num , 'salt' , 'salt'))
    print('soyun%d:' % num)
    for each in cur:
        print(each)

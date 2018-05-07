#/usr/bin/python
# -*- coding: utf-8 -*-
from celery import  shared_task
from django.db import connections
from unit.public_sql_audit import Inception
import time

@shared_task
def add(a, b):
    res = a*b
    print(time.localtime())
    time.sleep(20)
    print(time.localtime())
    return res

@shared_task
def osc(uid,main_sql,sql_id):
    try:
        cursor = connections['default'].cursor()
        result = Inception().inceptionQuery(main_sql)
        flag = []
        cursor = connections['default'].cursor()
        sql_del = '''delete from tb_execute_detail'''
        cursor.execute(sql_del)
        for row in result:
            flag.append(row[2])
            rep_str = row[5]
            strs = rep_str.replace("'", "\\'")
            strss = strs.replace('"', "\\'")
            sql_ins = '''insert into tb_execute_detail(tid,stage,errlevel,stagestatus,errormessage,`sql`,Affected_rows,sequence,backup_dbname,execute_time,sqlsha1,sql_id) values({0},"{1}",{2},"{3}","{4}","{5}",{6},"{7}","{8}","{9}","{10}",{11}) ;'''.format(row[0], row[1], row[2], row[3], row[4], strss , row[6], row[7], row[8], row[9], row[10], sql_id)
            cursor.execute(sql_ins)
        cursor.close()
        if 2 in flag or 1 in flag:
            sql_flag_fail = '''update tb_sql_audit set flag=4,auditor={0},audit_date=now() where id={1}'''.format(uid, sql_id)
            cursor = connections['default'].cursor()
            cursor.execute(sql_flag_fail)
            cursor.close()
            return 1
        else:
            sql_flag_succ = '''update tb_sql_audit set flag=5,auditor={0},audit_date=now() where id={1}'''.format(uid, sql_id)
            cursor = connections['default'].cursor()
            cursor.execute(sql_flag_succ)
            cursor.close()
            return 0
    except Exception as e:
        print(e)
        Inception().update_audit_flag_err(sqlid=sql_id)

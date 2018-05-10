#/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import  connections

class Monitor(object):

    @staticmethod
    def get_monitor_config():
        try:
            SQL = '''select name,value from options where name="monitor" UNION select name,value from options where name="monitor_mysql" 
            UNION select name,value from options where name="monitor_oracle" UNION select name,value from options where name="monitor_redis" UNION 
            select name,value from options where name="frequency_monitor"'''
            cursor = connections['lepus'].cursor()
            cursor.execute(SQL)
            res = cursor.fetchall()
            return res
        except Exception as e:
            print(e)
            return 2

    @staticmethod
    def up_monitor_total_config(total,mysql,oracle,redis,freq):
        try:
            #arr_name = ('monitor','monitor_mysql','monitor_oracle','monitor_redis','frequency_monitor')
            total_sql = '''update options set value="{0}" where name="monitor";''' .format(total)
            mysql_sql = '''update options set value="{0}" where name="monitor_mysql";''' .format(mysql)
            oracle_sql = '''update options set value="{0}" where name="monitor_oracle";'''  .format(oracle)
            redis_sql = '''update options set value="{0}" where name="monitor_redis";'''  .format(redis)
            freq_sql = '''update options set value="{0}" where name="frequency_monitor";'''  .format(freq)

            cursor = connections['lepus'].cursor()
            cursor.execute(total_sql)
            cursor.execute(mysql_sql)
            cursor.execute(oracle_sql)
            cursor.execute(redis_sql)
            cursor.execute(freq_sql)
            cursor.close()
            return 0
        except Exception as e:
            print(e)
            return e
      

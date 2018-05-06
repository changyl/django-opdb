#/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import  connections
import collections
import json
import datetime
import MySQLdb

from sqlaudit.models.sql_audit import SqlAudit


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return json.JSONEncoder.default(self, obj)

class Inception(object):

    def __init__(self,user=None,password=None,host=None,port=None,dbname=None,content=None,request=None):
        self.user = user


    def mosaic(self,user,password,host,port,dbname,content,request):
        '''
        desc:检查是否用户类别，is_staff=0-普通用户；1-超级用户；普通用户有警告则无法执行。
        :param user:
        :param password:
        :param host:
        :param port:
        :param dbname:
        :param content:
        :param request:
        :return:
        '''
        if request.user.is_staff == 0:
            target_sql = '''/*--user={0};--password={1};--host={2};--execute=1;--enable-remote-backup;--port={3};*/'''.format(user, password,
                                                                                                       host, port)
            db_sql = '''use {0};'''.format(dbname)
            ddl_dml_sql = '''{0}'''.format(content)
            main_sql = '''{0}inception_magic_start;{1}{2} inception_magic_commit;'''.format(target_sql, db_sql,
                                                                                            ddl_dml_sql)
        else:
            target_sql = '''/*--user={0};--password={1};--host={2};--execute=1;--enable-remote-backup;--enable-ignore-warnings;--port={3};*/'''.format(
                user, password, host, port)
            db_sql = '''use {0};'''.format(dbname)
            ddl_dml_sql = '''{0}'''.format(content)
            main_sql = '''{0}inception_magic_start;{1}{2} inception_magic_commit;'''.format(target_sql, db_sql,ddl_dml_sql)
        return main_sql

    def execute(self,request,main_sql,sql_id):
        try:
            if request.method == "POST" and request.user.is_staff == 1:
                result = self.inceptionQuery(main_sql)
                cursor = connections['default'].cursor()
                flag = []
                for row in result:
                    flag.append(row[2])
                    rep_str = row[5]
                    strs = rep_str.replace("'", "\\'")
                    strss = strs.replace('"', "\\'")
                    sql_del = '''delete from tb_execute_detail where sql_id={0}''' .format(sql_id)
                    sql_ins = '''insert into tb_execute_detail(tid,stage,errlevel,stagestatus,errormessage,`sql`,Affected_rows,sequence,backup_dbname,execute_time,sqlsha1,sql_id) values({0},"{1}",{2},"{3}","{4}","{5}",{6},"{7}","{8}","{9}","{10}",{11}) ;''' .format(row[0],row[1],row[2],row[3],row[4],strss,row[6],row[7],row[8],row[9],row[10],sql_id)
                    cursor = connections['default'].cursor()
                    cursor.execute(sql_del)
                    cursor.execute(sql_ins)
                cursor.close()
                if 2 in flag:
                    sql_flag ='''update tb_sql_audit set flag=4,creator={0},audit_date=now() where id={1}''' .format(request.user.id,sql_id)
                    cursor = connections['default'].cursor()
                    cursor.execute(sql_flag)
                    return 1
                else:
                    sql_flag_02 = '''update tb_sql_audit set flag=5,creator={0},audit_date=now() where id={1}'''.format(request.user.id,sql_id)
                    cursor = connections['default'].cursor()
                    cursor.execute(sql_flag_02)
                    return 0
            else:
                cursor = connections['default'].cursor()
                result = self.inceptionQuery(main_sql)
                flag = []
                for row in result:
                    flag.append(row[2])
                    rep_str = row[5]
                    strs = rep_str.replace("'", "\\'")
                    strss = strs.replace('"', "\\'")
                    sql_del = '''delete from tb_execute_detail where sql_id={0}'''.format(sql_id)
                    sql_ins = '''insert into tb_execute_detail(tid,stage,errlevel,stagestatus,errormessage,`sql`,Affected_rows,sequence,backup_dbname,execute_time,sqlsha1,sql_id) values({0},"{1}",{2},"{3}","{4}","{5}",{6},"{7}","{8}","{9}","{10}",{11}) ;'''.format(
                        row[0], row[1], row[2], row[3], row[4], strss, row[6], row[7], row[8], row[9], row[10], sql_id)
                    cursor = connections['default'].cursor()
                    cursor.execute(sql_del)
                    cursor.execute(sql_ins)
                cursor.close()
                if 2 in flag or 1 in flag:
                    '''1-警告;2-错误;'''
                    sql_flag = '''update tb_sql_audit set flag=4,creator={0},audit_date=now() where id={1}'''.format(
                        request.user.id, sql_id)
                    cursor = connections['default'].cursor()
                    cursor.execute(sql_flag)
                    return 1
                else:
                    sql_flag_02 = '''update tb_sql_audit set flag=5,creator={0},audit_date=now() where id={1}'''.format(
                        request.user.id, sql_id)
                    cursor = connections['default'].cursor()
                    cursor.execute(sql_flag_02)
                    return 0
        except Exception as e:
            print (e)
            return 0


    def preAuditExecute(self,user,password,host,port,dbname,content):
        """
        :param user:
        :param password:
        :param host:
        :param port:
        :param dbname:
        :param content:
        :return: sql
        :desc:拼接具体审核的sql格式
        :author:changyl
        """
        target_sql = '''/*--user={0};--password={1};--host={2};--enable-check;--port={3};*/'''.format(user,password,host,port)
        db_sql = '''use {0};'''.format(dbname)
        sql = '%s' % content
        main_sql = '''%sinception_magic_start;%s %s inception_magic_commit;''' % (target_sql,db_sql,sql)
        return main_sql



    def inceptionQuery(self,main_sql):
        """
        :param main_sql:
        :return:执行审核sql，返回审核结果
        :author:changyl
        """

        conn = MySQLdb.connect(host='', user='root', passwd='', db='', port=)
        cur = conn.cursor()
        cur.execute(main_sql.encode('utf-8'))
        result = cur.fetchall()
        return result

    def is_audit_on(self,id):
        q_res = '''select id from SQLAUDIT where id=%s and flag=2''' % (id)
        cursor = connections['default'].cursor()
        cursor.execute(q_res)
        row = cursor.fetchone()
        #1是已经审核，0是未审核
        if row is None:
            return 0
        else:
            return 1

    def get_audit_type(self,sql_id):
        res = SqlAudit.objects.values('audit_type').filter(id=sql_id)
        return res

    def update_audit_flag(self,sql_id):
        check_sql = '''select errlevel from tb_audit_detail where sql_id={0}''' .format(sql_id)
        cursor = connections['default'].cursor()
        cursor.execute(check_sql)
        row = cursor.fetchall()
        flag = []
        for r in row:
            flag.append(r[0])

        if 1 in flag or 2 in flag:
            flag2_sql = '''update tb_sql_audit set flag=2 where id={0}''' .format(sql_id)
            cursor = connections['default'].cursor()
            cursor.execute(flag2_sql)
        else:
            flag1_sql = '''update tb_sql_audit set flag=1 where id={0}'''.format(sql_id)
            cursor = connections['default'].cursor()
            cursor.execute(flag1_sql)
        return 0

    def insert_audit_res(self,row,strss,sql_id):
        try:
            sql = '''REPLACE into tb_audit_detail(tid,stage,errlevel,stagestatus,errormessage,`sql`,Affected_rows,sequence,backup_dbname,execute_time,sqlsha1,sql_id) values({0},"{1}",{2},"{3}","{4}",'{5}',{6},"{7}","{8}","{9}","{10}",{11}) ;'''.format(
                row[0], row[1], row[2], row[3], row[4], strss, row[6], row[7], row[8], row[9], row[10], sql_id)
            cursor = connections['default'].cursor()
            cursor.execute(sql)
            cursor.close()
            return 0
        except Exception as e:
            print(e)
            return 1




    def rollback(self,sqlid, content):
        '''执行回滚语句'''
        try:
            sql_dt_id = '''select db_id from tb_sql_audit where id={0}'''.format(sqlid)
            cursor = connections['default'].cursor()
            cursor.execute(sql_dt_id)
            row1 = cursor.fetchone()
            sql_database_info = '''select host,user,passwd,port,db_name from tb_cmdb_databases where id={0}'''.format(
                row1[0])
            cursor = connections['default'].cursor()
            cursor.execute(sql_database_info)
            row2 = cursor.fetchone()

            sql = '''{0}'''.format(content[0])
            conn = MySQLdb.connect(host=row2[0], user=row2[1], passwd=row2[2], db=row2[4], port=row2[3])
            cur = conn.cursor()
            cur.execute(sql.encode('utf-8'))

            result = conn.commit()
            return result
        except Exception as e:
            print (e)
            return 0


class SqlAuditExecute:

    @staticmethod
    def sqlList(request):
        ''' 所有审核内容列表 '''
        try:
            start = 0
            length = 0
            sumcnt = 0
            draw = request.GET.get('draw', None)
            start = request.GET.get('start', None)
            length = request.GET.get('length', None)

            if request.user.is_staff == True:
                sql_sum = '''select count(*) from tb_sql_audit where  create_date >date_format(now(),'%Y-%m-%d 00:00:00')'''
                sql_arry = '''select t.id,d.db_name,t.content,t.flag,t.create_date,t.username,t.remarks,a.username,t.audit_date from (SELECT r.id as id,db_id,content,create_date ,u.username,r.flag,r.remarks,r.auditor,r.audit_date  FROM  tb_sql_audit as r left join auth_user as u ON r.creator=u.id where  r.create_date>date_format(now(),'%Y-%m-%d 00:00:00') ) as t left join tb_cmdb_databases d on d.id=t.db_id left join auth_user as a on t.auditor=a.id  order by t.id desc  limit {0},{1}'''.format(
                    start, length)
            else:
                sql_sum = '''select count(*) from tb_sql_audit where  create_date >date_format(now(),'%Y-%m-%d 00:00:00') and creator={0}'''.format(
            request.user.id)
                sql_arry = '''select t.id,d.db_name,t.content,t.flag,t.create_date,t.username,t.remarks,a.username,t.audit_date from (SELECT r.id as id,db_id,content,create_date ,u.username,r.flag,r.remarks,r.auditor,r.audit_date  FROM  tb_sql_audit as r left join auth_user as u ON r.creator=u.id where  r.create_date>date_format(now(),'%Y-%m-%d 00:00:00') and creator={0} ) as t left join tb_cmdb_databases d on d.id=t.db_id left join auth_user as a on t.auditor=a.id  order by t.id desc  limit {1},{2}'''.format(
                    request.user.id, start, length)

            cursor1 = connections['default'].cursor()
            cursor1.execute(sql_sum)
            sum_row = cursor1.fetchone()

            cursor2 = connections['default'].cursor()
            cursor2.execute(sql_arry)
            all_row = cursor2.fetchall()

            dict = collections.OrderedDict()
            dict['draw'] = draw
            dict['recordsTotal'] = sum_row[0]
            dict['recordsFiltered'] = sum_row[0]
            dict['data'] = all_row
            json_object = json.dumps(dict, cls=DateEncoder)
            cursor1.close()
            cursor2.close()
            return json_object
        except Exception as e:
            print (e)
            return 0

    def sqlHistoryList(self,request):
        '''所有审核内容列表'''
        try:
            start = 0
            length = 0
            sumcnt = 0
            draw = request.GET.get('draw', None)
            start = request.GET.get('start', None)
            length = request.GET.get('length', None)
            if request.user.is_staff == True:
                sql_sum = '''select count(*) from tb_sql_audit where  create_date <date_format(now(),'%Y-%m-%d 00:00:00')'''
                sql_arry = '''select t.id,d.db_name,t.content,t.flag,t.create_date,t.username,t.remarks,a.username,t.audit_date from (SELECT r.id as id,db_id,content,create_date ,u.username,r.flag,r.remarks,r.auditor,r.audit_date  FROM  tb_sql_audit as r left join auth_user as u ON r.creator=u.id where  r.create_date<date_format(now(),'%Y-%m-%d 00:00:00') ) as t left join tb_cmdb_databases d on d.id=t.db_id left join auth_user as a on t.auditor=a.id  order by t.id desc  limit {0},{1}'''.format(
                    start, length)
            else:
                sql_sum = '''select count(*) from tb_sql_audit where  create_date <date_format(now(),'%Y-%m-%d 00:00:00') and creator={0}'''.format(
            request.user.id)
                sql_arry = '''select t.id,d.db_name,t.content,t.flag,t.create_date,t.username,t.remarks,a.username,t.audit_date from (SELECT r.id as id,db_id,content,create_date ,u.username,r.flag,r.remarks,r.auditor,r.audit_date  FROM  tb_sql_audit as r left join auth_user as u ON r.creator=u.id where  r.create_date<date_format(now(),'%Y-%m-%d 00:00:00') and creator={0} ) as t left join tb_cmdb_databases d on d.id=t.db_id left join auth_user as a on t.auditor=a.id order by t.id desc  limit {1},{2}'''.format(
                    request.user.id, start, length)
            cursor1 = connections['default'].cursor()
            cursor1.execute(sql_sum)
            sum_row = cursor1.fetchone()

            cursor2 = connections['default'].cursor()
            cursor2.execute(sql_arry)
            all_row = cursor2.fetchall()

            dict = collections.OrderedDict()
            dict['draw'] = draw
            dict['recordsTotal'] = sum_row[0]
            dict['recordsFiltered'] = sum_row[0]
            dict['data'] = all_row
            json_object = json.dumps(dict, cls=DateEncoder)
            cursor1.close()
            cursor2.close()
            return json_object
        except Exception as e:
            print (e)
            return 0

    @staticmethod
    def get_db_info(db_name):
        sql_database_info = '''select host,user,passwd,port,db_name,creator from tb_cmdb_databases  where db_name="{0}"'''.format(
            db_name)
        cursor = connections['default'].cursor()
        cursor.execute(sql_database_info)
        row = cursor.fetchone()
        return row

    @staticmethod
    def sqlResultList(sql_id):
        '''所有审核结果列表'''
        sql_arry = '''select  *   FROM  tb_audit_detail where sql_id={0} '''.format(sql_id)
        cursor = connections['default'].cursor()
        cursor.execute(sql_arry)
        all_row = cursor.fetchall()
        return all_row

    @staticmethod
    def executeResultList(sql_id):
        '''所有审核结果列表'''
        sql_arry = '''select  *   FROM  tb_execute_detail where sql_id={0} '''.format(sql_id)
        cursor = connections['default'].cursor()
        cursor.execute(sql_arry)
        all_row = cursor.fetchall()
        return all_row


    @staticmethod
    def updateSql(sql_id,cont):
        try:
            sql = '''update tb_sql_audit set content="{1}" where id={0}''' .format(sql_id,cont)
            cursor = connections['default'].cursor()
            cursor.execute(sql)
            return 1
        except Exception as e:
            print (e)
            return 0


    @staticmethod
    def get_sql_audit_status(sql_id):
        pass





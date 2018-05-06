from users.models.group import GroupMenus,Group
from django.db import  connections
import collections

class Tools:
    def __init__(self,request=None,context=None):
        self.request = request
        self.context = context

    @staticmethod
    def get_content(request,context):
        sql = '''select menus_id from tb_group_menus  where group_id in (select group_id from auth_user_groups where user_id = %s )''' % (request.user.id)
        cursor = connections['default'].cursor()
        cursor.execute(sql)
        res = cursor.fetchone()

        if res:
            sql = '''select * from tb_menus where flag=1 and id in (%s)''' % (res[0])
            cursor = connections['default'].cursor()
            cursor.execute(sql)
            qt = cursor.fetchall()
            context['menus'] = qt
            context['username'] = request.user.username
            context['url'] = request.path
        else:
            print ('have not %s' % res)
        return context

    @staticmethod
    def get_content_group(request, context):
        sql = '''select menus_id from tb_group_menus  where group_id in (select group_id from auth_user_groups where user_id = %s )''' % (
        request.user.id)
        cursor = connections['default'].cursor()
        cursor.execute(sql)
        res = cursor.fetchone()

        if res:
            sql = '''select * from tb_menus where flag=1 and id in (%s)''' % (res[0])
            cursor = connections['default'].cursor()
            cursor.execute(sql)
            qt = cursor.fetchall()

            context['menus'] = qt
            context['username'] = request.user.username
            context['url'] = request.path
        else:
            print ('have not %s' % res)
        return context

    @staticmethod
    def get_menus():
        sql = '''select id,ch_nm from tb_menus where flag=1'''
        cursor = connections['default'].cursor()
        cursor.execute(sql)
        menus = cursor.fetchall()
        return menus

    @staticmethod
    def get_users():
        sql = '''select id,username from auth_user '''
        cursor = connections['default'].cursor()
        cursor.execute(sql)
        menus = cursor.fetchall()
        return menus

    @staticmethod
    def get_prem():
        sql = '''select id,ch_nm from tb_menus where flag=1'''
        cursor = connections['default'].cursor()
        cursor.execute(sql)
        menus = cursor.fetchall()
        return menus

    @staticmethod
    def get_db():
        sql = '''SELECT id,db_tag FROM tb_cmdb_databases where flag = 1;'''
        cursor = connections['default'].cursor()
        cursor.execute(sql)
        menus = cursor.fetchall()
        return menus




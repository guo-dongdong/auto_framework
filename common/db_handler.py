# -*- coding:utf-8 -*-
# @Time :2020-07-16 21:57
# @Email :876417305@qq.com
# @Author :yanxia
# @File :db_handler.PY

import pymysql
from pymysql.cursors import DictCursor

from common import config_handler
from config.setting import config


class DBHandler:

    def __init__(self,host,port,user,password,charset,
                 database=None,cursorclass=DictCursor,**kw):
        """初始化"""

        # 建立连接
        # TODO:utf-8  -->  utf8
        self.conn = pymysql.connect(host=host,port=port,user=user,
                                    password=password,charset=charset,
                                    database=database,
                                    cursorclass=cursorclass,**kw)
        self.cursor = self.conn.cursor()

    def query(self, sql, args=None, one=True):
        """sql语句"""
        self.cursor.execute(sql, args)
        # 获取结果
        if one:

            return self.cursor.fetchone()
        else:
            return self.cursor.fetchall()

    def close(self):
        """关闭连接"""
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    # 参数读取配置文件
    # yaml读取
    yaml_data = config_handler.read_yaml(config.yaml_config_path)
    db = DBHandler(host=yaml_data['database']['host'],
                   port=yaml_data['database']['port'],
                   user=yaml_data['database']['user'],
                   password=yaml_data['database']['password'],
                   charset=yaml_data['database']['charset'],
                   database=yaml_data['database']['database'],)
    res = db.query("select * from member limit 2;", one=False)
    print(res)
# -*- coding:utf-8 -*-


"""投资相关测试用例"""
import os
import unittest
from datetime import datetime
from common.db_handler import DBHandler
from common.helper import generate_mobile
from common.logger_handler import LoggerHandler
from libs import ddt
from common.excel_handler import ExcelHandler
from config.setting import config
from common.requests_handler import RequestsHandler
import json
from common import config_handler
from middleware.helper import save_token, Context
from middleware.yaml_handler import yaml_data



# yaml读取
# yaml_data = config_handler.read_yaml(config.yaml_config_path)
yaml_data


@ddt.ddt
class TestInvest(unittest.TestCase):

    # 读取数据
    excel_handler = ExcelHandler(config.data_path)
    data = excel_handler.read('invest')

    logger = LoggerHandler(yaml_data["logger"]["name"],
                           yaml_data["logger"]["level"],
                           config.log_path + yaml_data["logger"]["file"])


    def setUp(self):
        self.req = RequestsHandler()

        self.db = DBHandler(host=yaml_data['database']['host'],
                   port=yaml_data['database']['port'],
                   user=yaml_data['database']['user'],
                   password=yaml_data['database']['password'],
                   charset=yaml_data['database']['charset'],
                   database=yaml_data['database']['database'])


        # 登录用户，得到token
        # 结果
        save_token()
        self.token = Context.token
        self.member_id = Context.member_id

        # save_loan_id()


    def tearDown(self) -> None:
        self.req.close_session()
        self.db.close()


    @ddt.data(*data)
    def test_Invest(self, test_data):

        '''投资接口'''
        # 1.替换json数据中的member_id，  #member_id#  替换成Context.member_id
        # 2. 访问接口，得到实际结果
        # 3.断言

        # 查询数据库， 查询member_id的用户余额
        sql = "SELECT * FROM member WHERE id = %s;"
        user = self.db.query(sql, args=[self.member_id, ])
        print(user)
        before_money = user["leave_amount"]


        if "#member_id#" in test_data['data']:
            test_data['data'] = test_data['data'].replace('#member_id#', str(self.member_id))

        # if "#wrongr_id#" in test_data['data']:
        #     test_data['data'] = test_data['data'].replace('#wrongr_id#', str(self.member_id + 2))

        # print(test_data)

        # 读取excel当中的headers，得到字典
        headers = json.loads(test_data['headers'])
        # 添加Authorization 头信息
        headers['Authorization'] = self.token

        # 访问接口得到实际结果
        res = self.req.visit(test_data['method'],
                             config.host + test_data['url'],
                             json=json.loads(test_data['data']),
                             headers=headers)

        # 断言1  code码
        self.assertEqual(test_data['expected'], res['code'])

        # 断言2：  成功用例需要进行数据库校验
        # 判断是否为成功用例，如果是成功用例，校验数据库
        if res['code'] == 0:
            # 查看数据库结果，充值金额+充值前的金额==充值后的金额
            money = json.loads(test_data['data'])['amount']
            # 获取充值前的金额
            # before_money
            # 获取充值后的金额
            sql = "SELECT * FROM member WHERE id = %s;"
            after_user = self.db.query(sql, args=[self.member_id, ])
            after_money = after_user["leave_amount"]

            self.assertEqual(after_money, before_money - money)


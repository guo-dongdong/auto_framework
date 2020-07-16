# -*- coding:utf-8 -*-
# @Time :2020-07-07 22:08
# @Email :876417305@qq.com
# @Author :yanxia
# @File :test_register.PY

"""注册相关测试用例"""
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

# yaml读取
yaml_data = config_handler.read_yaml(config.yaml_config_path)


@ddt.ddt
class TestRegister(unittest.TestCase):

    # 读取数据
    excel_handler = ExcelHandler(config.data_path)
    data = excel_handler.read('register')

    logger = LoggerHandler(yaml_data["logger"]["name"],
                           yaml_data["logger"]["level"],
                           yaml_data["logger"]["file"])


    def setUp(self):
        self.req = RequestsHandler()

        self.db = DBHandler(host=yaml_data['database']['host'],
                   port=yaml_data['database']['port'],
                   user=yaml_data['database']['user'],
                   password=yaml_data['database']['password'],
                   charset=yaml_data['database']['charset'],
                   database=yaml_data['database']['database'],)

    def tearDown(self) -> None:
        self.req.close_session()
        self.db.close()


    @ddt.data(*data)
    def test_register(self, test_data):

        # 判断test_data['data']如果出现了#exsit_phone#,使用generate_mobile()随机生成一个手机号码
        if '#exist_phone#' in test_data['data']:
            # mobile = generate_mobile()
            # # 查询数据库，如果数据库存在改手机号，就直接使用这么号码
            mobile = self.db.query('select * from member limit 1;')
            if mobile:
            # 直接查找数据库，随机找一个，直接使用这个手机号
            # 替换
                test_data['data'] = test_data['data'].replace('#exist_phone#', mobile['mobile_phone'])
            else:
                # 随机生成一个，数据库当中还是不存在
                # 注册成功,通过接口注册          直接通过插入数据库
                pass

        if '#new_phone#' in test_data['data']:
            while True:
                mobile = generate_mobile()
                # 查询数据库，如果数据库存在改手机号，就直接使用这么号码
                mobile = self.db.query('select * from member where mobile_phone=%s;', args=[mobile])
                # 直接查找数据库，随机找一个，直接使用这个手机号
                # 替换
                if not mobile:
                    break

            test_data['data'] = test_data['data'].replace('#exist_phone#', mobile['mobile_phone'])



        # 访问接口得到实际结果
        res = self.req.visit(test_data['method'],
                             config.host + test_data['url'],
                             json=json.loads(test_data['data']),
                             headers=json.loads(test_data['headers']))
        # 获取预期结果test_data['expected']
        # 断言

        # 如果断言失败，要将失败的用例保存到log中
        # AssertionError
        try:
            self.assertEqual(test_data['expected'], res['code'])
            # 写入excel数据
            self.excel_handler.write(config.data_path,
                                     "register",
                                     test_data['case_id'] + 1,
                                     9,
                                     "测试通过")
        except AssertionError as e:
            # 记录log
            self.logger.error("测试用例失败:{}".format(e))

            self.excel_handler.write(config.data_path,
                                     "register",
                                     test_data['case_id'] + 1,
                                     9,
                                     "测试失败")

            # 手动抛出异常，否则测试用例会自动通过
            raise e



        # 把实际结果写入excel

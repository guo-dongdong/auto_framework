# -*- coding:utf-8 -*-
# @Time :2020-07-07 22:08
# @Email :876417305@qq.com
# @Author :yanxia
# @File :test_register.PY

"""注册相关测试用例"""
import os
import unittest

from common.logger_handler import LoggerHandler
from libs import ddt
from common.excel_handler import ExcelHandler
from config.setting import config
from common.requests_handler import RequestsHandler
import json


@ddt.ddt
class TestRegister(unittest.TestCase):

    # 读取数据
    excel_handler = ExcelHandler(config.data_path)
    data = excel_handler.read('register')

    logger = LoggerHandler("python25")

    def setUp(self):
        self.req = RequestsHandler()

    def tearDown(self) -> None:
        self.req.close_session()


    @ddt.data(*data)
    def test_register(self, test_data):

        # 访问接口得到实际结果
        res = self.req.visit(test_data['method'],
                             config.host + test_data['url'],
                             json=json.loads(test_data['data']),
                             headers=json.loads(test_data['headers']))
        # 获取预期结果test_data['expected']
        # 断言

        try:
            self.assertEqual(test_data['expected'], res['code'])
        except AssertionError as e:
            return "断言失败：", e


        # 如果出现断言失败，要将失败的用例记录写到log里面
        # AssertionError

        # 把实际结果写入excel

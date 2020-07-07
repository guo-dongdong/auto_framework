# -*- coding:utf-8 -*-
# @Time :2020-07-07 22:08
# @Email :876417305@qq.com
# @Author :yanxia
# @File :test_register.PY

"""注册相关测试用例"""
import os
import unittest
import ddt
from common.excel_handler import ExcelHandler
from config.setting import config, DevConfig
from common.requests_handler import RequestsHandler


@ddt.ddt
class TestRegister(unittest.TestCase):

    # 读取数据
    excel_handler = ExcelHandler(config.data_path)
    data = excel_handler.read('register')

    def setUp(self):
        self.req = RequestsHandler()

    def tearDown(self) -> None:
        self.req.close_session()


    @ddt.data(*data)
    def test_register(self, test_data):

        # 访问接口得到实际结果
        res = self.req.visit(test_data['method'],
                             DevConfig.host + test_data['url'],
                             json=eval(test_data['data']),
                             headers=eval(test_data['headers']))
        # 获取预期结果test_data['expected']
        # 断言
        self.assertEqual(test_data['expected'], res['code'])

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-07-09 11:12
# @Author  : guoDD
# @Email   : Email
# @File    : run

import os
import unittest
from datetime import datetime

from libs.HTMLTestRunnerNew import HTMLTestRunner
from config.setting import config

# 初始化testloader加载器
testloader = unittest.TestLoader()
# 查找测试用例
suite = testloader.discover(config.case_path)

# 测试报告
# 报告名称加时间戳
ts = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
# ts = str(int(time.time()))
file_name = 'Test_Result_{}.html'.format(ts)
file_path = os.path.join(config.report_path, file_name)
# HTML
# TODO:HTML一定要使用二进制的方式打开
with open(file_path, 'wb',) as f:
    runner = HTMLTestRunner(f,title="Test接口测试报告",description="Test接口测试报告",tester="_小川")
    runner.run(suite)


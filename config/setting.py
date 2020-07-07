# -*- coding:utf-8 -*-
# @Time :2020-07-07 22:20
# @Email :876417305@qq.com
# @Author :yanxia
# @File :setting.PY
import os


class Config:

    # 项目路径
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 测试数据路径
    data_path = os.path.join(root_path, 'data/cases.xlsx')

class DevConfig(Config):

    # 项目域名
    host = 'http://120.78.128.25:8766/futureloan'


config = Config()
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

    # 测试用例路径
    case_path = os.path.join(root_path, 'test_cases')

    # config路径
    config_path = os.path.join(root_path, 'config')

    # 测试报告路径
    report_path = os.path.join(root_path, 'report')
    if not os.path.exists(report_path):
        os.mkdir(report_path)

    # log路径
    log_path = os.path.join(root_path, 'log')
    if not os.path.exists(log_path):
        os.mkdir(log_path)

    # # 艳霞
    #     print(log_path)
    #     print(os.mkdir(log_path))

    #yaml
    yaml_config_path = os.path.join(config_path, 'config.yaml')

class DevConfig(Config):

    # 项目域名
    host = 'http://120.78.128.25:8766/futureloan'


config = DevConfig()

if __name__ == '__main__':
    m=Config()
    print(m.log_path)
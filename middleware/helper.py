# -*- coding:utf-8 -*-
# @Time :2020-07-19 17:01
# @Email :876417305@qq.com
# @Author :yanxia
# @File :helper.PY

from common import config_handler
from common.requests_handler import RequestsHandler
from config.setting import config
from middleware.yaml_handler import yaml_data
from jsonpath import jsonpath

# yaml读取
# yaml_data = config_handler.read_yaml(config.yaml_config_path)
# print(yaml_data)
yaml_data

def login():
    """登录用户，返回token"""
    # 访问登录接口

    req = RequestsHandler()
    res = req.visit('post',
                    config.host + '/member/login',
                    json=yaml_data['user'],
                    headers={"X-Lemonban-Media-Type":"lemonban.v2"})
    return res

def login_admin():
    pass

# 保存token
class Context:
    token = ''
    member_id = None

def loan_id():
    """查询数据了，得到loan_id
    临时变量，保存到Context当中
    """
    pass


def save_token():
    """保存token信息"""
    data = login()

    token = jsonpath(data, '$..token')[0]
    token_type = jsonpath(data, '$..token_type')[0]
    member_id = jsonpath(data, '$..id')[0]
    # 拼接token
    token = " ".join([token_type, token])
    # return token

    # 设置默认值
    Context.token = token
    Context.member_id = member_id

    # return {"token":token, "member":member_id}





if __name__ == '__main__':
    # data = login()
    # token = data['data']['token_info']['token']
    # token_type = data['data']['token_info']['token_type']

    # jsonpath  ==》 专门用来解析json的路径工具
    # 安装 jsonpath，pip install
    # 引入  from jsonpath import jsonpath
    # print(jsonpath(data, '$..token')[0])
    # print(jsonpath(data, '$..token_type')[0])
    # print(jsonpath(data, '$..id')[0])

    data = save_token()
    print(data)
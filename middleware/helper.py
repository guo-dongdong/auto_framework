# -*- coding:utf-8 -*-
# @Time :2020-07-19 17:01
# @Email :876417305@qq.com
# @Author :yanxia
# @File :helper.PY
import re

from common import config_handler
from common.db_handler import DBHandler
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

# Context().loan_id()

# 保存token
class Context:
    # token = ''
    # member_id = None

    @property
    def loan_id(self):
        """查询数据了，得到loan_id
        临时变量，保存到Context当中
        return  返回loan标当中的id值
        """
        db = DBHandler(host=yaml_data['database']['host'],
                       port=yaml_data['database']['port'],
                       user=yaml_data['database']['user'],
                       password=yaml_data['database']['password'],
                       charset=yaml_data['database']['charset'],
                       database=yaml_data['database']['database'])
        loan = db.query('select * from loan where status=2 limit 10;')
        db.close()
        return loan['id']

    @property
    def token(self):
        """token属性，而且属性会动态变化
        Context().token    获取token自动调用这个方法
        """
        data = login()
        t = jsonpath(data, '$..token')[0]
        token_type = jsonpath(data, '$..token_type')[0]
        t = " ".join([token_type, t])
        return t

    @property
    def member_id(self):
        data = login()
        m_id = jsonpath(data, '$..id')[0]
        return m_id

    @property
    def admin_member_id(self):
        """"""
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

def replace_label(target):
    """while 循环"""
    re_pattern = r'#(.*?)#'
    while re.findall(re_pattern, target):
        # 如果能够匹配，直接替换
        key = re.search(re_pattern, target).group(1)
        target = re.sub(re_pattern, str(getattr(Context, key)), target, 1)
    return target




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

    # data = save_token()
    # print(data)
    print(Context().token)
    print(Context().member_id)

    print(Context().loan_id)

    replace_label()
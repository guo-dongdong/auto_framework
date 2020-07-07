 #!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-06-30 15:49
# @Author  : guoDD
# @Email   : Email
# @File    : homework_requests

"""

"""
import requests



class RequestsHandler:

    def __init__(self):
        self.session = requests.Session()


    def visit(self,  method, url, params=None, data=None, json=None, **kwargs):

        """访问一个接口，可使用get，post请求，put，delect等"""
        """
        请求方法method
        请求地址url
        请求参数params，data，json
        """

        # if method.lower() == 'get':
        #     res = self.session.get(url, params=params, **kwargs)
        # elif method.lower() == 'post':
        #     res = self.session.post(url, params=params, data=data, json=json, **kwargs)
        # else:
        #     # 可以处理请求方法
        #     res = self.session.request(method, url, params=params, data=data, json=json, **kwargs)
        res = self.session.request(method, url, params=params, data=data, json=json, **kwargs)
        try:
            return res.json()
        except ValueError:
            print("not json",res)
            return res

    def close_session(self):
        self.session.close()
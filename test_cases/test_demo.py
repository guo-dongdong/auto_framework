# -*- coding:utf-8 -*-
# @Time :2020-07-23 20:48
# @Email :876417305@qq.com
# @Author :yanxia
# @File :test_demo.PY
import unittest
from mock import Mock

def add(a, b):
    """"""
    pass

class TestAdd(unittest.TestCase):
    def test_add(self):

        #mock 对象
        add = Mock(return_value=8)

        self.assertEqual(7, add(3.4))
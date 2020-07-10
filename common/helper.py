#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-07-10 14:51
# @Author  : guoDD
# @Email   : Email
# @File    : helper
import random


def generate_mobile():
    """随机生成一个手机号码  1[3,5,7,8]+9位"""
    phone = '1' + random.choice(['3','5','7','8'])
    for i in range(9):
        num = random.randint(0,9)
        phone += str(num)
    return phone


if __name__ == '__main__':
    print(generate_mobile())
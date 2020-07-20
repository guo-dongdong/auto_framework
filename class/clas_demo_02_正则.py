# -*- coding:utf-8 -*-
# @Time :2020-07-20 22:07
# @Email :876417305@qq.com
# @Author :yanxia
# @File :clas_demo_02_正则.PY
"""
正则表达式是一种通用的字符串匹配技术
是不会因为编程语言不一样而发生变化的

语法：
re.match('a2', 'a234')  能否在开头找到a2

findall()
[abc],  a = re.findall(r'[abc]', 'helloae')

., 任意的一个， 除了/n  a = re.search(r'.', 'hello')

{m,n}  a = re.findall(r'\d{11}', 'sfw12313213265456sfsw')

a = re.findall(r'1[35]\d{9}', 'sfw12313213265456sfsw')


"""

import re

# .  匹配任意一个字符串，除了\n
# re_pattern = r'.'
# res = re.findall(re_pattern, "aa\nsdfd\tdsmfegfgwamegdgfmdgdfg")
# print(res)

# \d   -- 匹配数字
# re_pattern = r'\d'
# re_pattern_01 = r'\D'
# res = re.findall(re_pattern, "aa\nsdfd\tdsmf123egfgwam4egdgfm5dgdfg")
# res_01 = re.findall(re_pattern_01, "aa\nsdfd\tdsmf123egfgwam4egdgfm5dgdfg")
# print(res)
# print(res_01)

# \w   -- 匹配数字字母下划线
# \W反向
# {2,}  匹配至少2次
# TODO:在正则表达式中，千万不要随便打空格
re_pattern = r'\w{2,}'
res = re.findall(re_pattern, "aa\nsdfd\tdsg_@fm12345dgdfg")
print(res)
re_pattern_01 = r'\W'
res1 = re.findall(re_pattern_01, "aa\nsdfd\tdsg_@fm5dgdfg")
print(res1)

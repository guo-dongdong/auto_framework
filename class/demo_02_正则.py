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
# {,2}  匹配最多两次
# {2,4}  匹配2-4次
# TODO:在正则表达式中，千万不要随便打空格
# re_pattern = r'\w{2,}'
# re_pattern = r'\w{,2}'
# re_pattern = r'\w{2,4}'
# res = re.findall(re_pattern, "aa\nsdfd\tdsg_@fm12345dgdfg")
# print(res)
# re_pattern_01 = r'\W'
# res1 = re.findall(re_pattern_01, "aa\nsdfd\tdsg_@fm5dgdfg")
# print(res1)


# 如何去匹配一个手机号
# re_pattern = r'1[35789]\d{9}'
# res = re.findall(re_pattern, "aa\nsdfd\tdsg_@f14298461920m12345dgdfg")
# print(res)

# * 匹配0次或者任意次
# re_pattern = r'\d*'
# res = re.findall(re_pattern, "aa\nsd2fd\td3s4g_5@66")
# print(res)

# ?  非贪婪模式
# re_pattern = r'\d?'
# res = re.findall(re_pattern, "aa\nsd2fd\td3s4g_5@66")
# print(res)

# mystr = '{"member_id":"#member_id#","loan_id":"#loan_id#","amount":-3,"username":"#username#"}'
# re_pattern = r'#(.*?)#'
# res = re.findall(re_pattern, mystr)
# print(res)

# re.sub    替换
# mystr = re.sub(re_pattern, 'mem123', mystr, 1)
# mystr = re.sub(re_pattern, 'loan123', mystr, 1)
# mystr = re.sub(re_pattern, 'username123', mystr, 1)

# print(mystr)

class Context:
    member_id = 2067
    loan_id = 100
    username = "guodongong"

def replace_label(target):
    """while 循环"""
    re_pattern = r'#(.*?)#'
    while re.findall(re_pattern, target):
        # 如果能够匹配，直接替换
        key = re.search(re_pattern, target).group(1)
        target = re.sub(re_pattern, str(getattr(Context, key)), target, 1)
    return target

if __name__ == '__main__':
    mystr = '{"member_id":"#member_id#","loan_id":"#loan_id#","amount":-3,"username":"#username#"}'

    a = replace_label(mystr)
    print(a)
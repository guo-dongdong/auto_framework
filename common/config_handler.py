#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-07-06 14:14
# @Author  : guoDD
# @Email   : Email
# @File    : config_handler


from configparser import ConfigParser
import yaml

class ConfigHandler(ConfigParser):

    def __init__(self, file, encoding='utf-8'):
        """参数
        - file：配置文件的路径名
        """
        super().__init__()
        self.read(file, encoding=encoding)

def read_yaml(file, encoding='utf-8'):
    with open(file, encoding=encoding) as f:
        return yaml.load(f.read(), Loader=yaml.FullLoader)


def write_yaml(file, data, encoding='utf-8'):
    """
    写入yaml
    处理中文  allow_unicode=True
    """
    with open(file, encoding=encoding, mode='w') as f:
        yaml.dump(data, stream=f, allow_unicode=True)


if __name__ == '__main__':
    # config = ConfigHandler('python_25.ini')
    # a = config.get("teachers","name")
    # print(a)
    #
    # b = read_yaml("python_25.yaml")
    # print(b)

    # 先读取yaml数据
    data = read_yaml("python_25.yaml")
    write_yaml("pytron_26.yaml", data)
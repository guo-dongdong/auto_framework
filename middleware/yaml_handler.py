# -*- coding:utf-8 -*-
# @Time :2020-07-19 17:13
# @Email :876417305@qq.com
# @Author :yanxia
# @File :yaml_handler.PY

import yaml
from config.setting import config


class YamlHandler:

    def __init__(self, file):
        self.file = file

    def read(self, encoding='utf-8'):
        f = open(self.file, encoding=encoding)
        # TODO: f.read()和f 都可以作为参数
        data = yaml.load(f, yaml.FullLoader)
        f.close()
        return data

yaml_data = YamlHandler(config.yaml_config_path).read()



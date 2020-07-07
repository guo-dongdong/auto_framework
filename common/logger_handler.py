#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-07-05 16:12
# @Author  : guoDD
# @Email   : Email
# @File    : logger_handler
import logging


class LoggerHandler(logging.Logger):

    def __init__(self,
                 name='root',
                 level='DEBUG',
                 file=None,
                 format='%(asctime)s - %(filename)s:%(lineno)d:%(name)s:%(levelname)s - %(message)s'
                 ):
        super().__init__(name)

        # 设置级别
        self.setLevel(level)
        fmt = logging.Formatter(format)

        # 初始化处理器
        if file:
            file_handler = logging.FileHandler(file)
            # 设置handler级别
            file_handler.setLevel(level)
            file_handler.setFormatter(fmt)
            self.addHandler(file_handler)


        stream_handler = logging.StreamHandler()
        # 设置handler的级别
        stream_handler.setLevel(level)
        stream_handler.setFormatter(fmt)
        self.addHandler(stream_handler)


logger = LoggerHandler("python25",file='python25_log.txt')

if __name__ == '__main__':
    logger = LoggerHandler()
    logger.debug("hello world_python_python")
# coding:utf-8
'''日志模块
%(name)s              Logger的名字
%(levelno)s           数字形式的日志级别
%(levelname)s        文本形式的日志级别
%(pathname)s         调用日志输出函数的模块的完整路径名，可能没有
%(filename)s         调用日志输出函数的模块的文件名
%(module)s           调用日志输出函数的模块名
%(funcName)s         调用日志输出函数的函数名
%(lineno)d           调用日志输出函数的语句所在的代码行
%(created)f         当前时间，用UNIX标准的表示时间的浮 点数表示
%(relativeCreated)d         输出日志信息时的，自Logger创建以 来的毫秒数
%(asctime)s         字符串形式的当前时间。默认格式是 “2017-07-08 16:49:45,896”。逗号后面的是毫秒
%(thread)d          线程ID。可能没有
%(threadName)s      线程名。可能没有
%(process)d         进程ID。可能没有
%(message)s         用户输出的消息
'''
import logging
import os
import time


class LogInfo(object):
    '''配置log格式等级'''

    def __init__(self, app=None):
        # 根据时间的文件名
        # self.log_file_name = time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log'
        # __file__获取模块所在的路径
        # self.log_file_str = os.path.abspath(
        #     os.path.join(os.path.dirname(__file__), os.pardir, 'log')) + os.sep + self.log_file_name
        # self.handler = logging.FileHandler(self.log_file_str, encoding='UTF-8')
        self.logging_format = logging.Formatter(
            '[time]:%(asctime)s [level]:%(levelname)s [fileName]:%(filename)s [function]:%(funcName)s [lineNo]:%(lineno)s [msg]:%(message)s')
        # self.handler.setFormatter(logging_format)
        self.logger = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        # app.logger.addHandler(self.handler)
        self.logger = app.logger

    def get_logger(self, level):
        '''
        根据等级获取获取日志对象
        :param level: 日志等级
            debug
            error
            info
        :return:
            logger对象
        '''
        log_file_name = time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log'
        file_str = {
            'debug_dir': os.path.abspath(
                os.path.join(os.path.dirname(__file__), os.pardir, 'log/debug_log')) + os.sep + log_file_name,
            'info_dir': os.path.abspath(
                os.path.join(os.path.dirname(__file__), os.pardir, 'log/info_log')) + os.sep + log_file_name,
            'error_dir': os.path.abspath(
                os.path.join(os.path.dirname(__file__), os.pardir, 'log/error_log')) + os.sep + log_file_name

        }
        handler = None
        '''
            'ERROR': ERROR,   40
            'WARNING': WARNING,   30
            'INFO': INFO,   20
            'DEBUG': DEBUG,    10 默认
            高等级的日志会覆盖低等级的日志，
        '''
        if level == 'debug':
            handler = logging.FileHandler(file_str['debug_dir'], encoding='UTF-8')
            handler.setLevel(logging.DEBUG)
            handler.setFormatter(self.logging_format)
        elif level == 'info':
            handler = logging.FileHandler(file_str['info_dir'], encoding='UTF-8')
            handler.setLevel(logging.INFO)  # 只会显示info及以上的日志
            handler.setFormatter(self.logging_format)
        elif level == 'error':
            handler = logging.FileHandler(file_str['error_dir'], encoding='UTF-8')
            handler.setLevel(logging.ERROR)  # 只会显示error及以上的日志
            handler.setFormatter(self.logging_format)
        self.logger.addHandler(handler)
        return self.logger

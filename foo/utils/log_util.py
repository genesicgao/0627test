
import logging
import os
import sys
from datetime import datetime
from logging import Formatter, StreamHandler
import socket

from pythonjsonlogger import jsonlogger


def get_host_name():
    try:
        host_name = socket.gethostname()
        return host_name
    except:
        print("Unable to get Hostname and IP")
        return None


def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except:
        return None
    finally:
        s.close()
    return ip


class ElkJsonFormatter(jsonlogger.JsonFormatter):
    host_name = get_host_name()
    host_ip = get_host_ip()

    def add_fields(self, log_record, record, message_dict):
        super(ElkJsonFormatter, self).add_fields(log_record, record, message_dict)
        now = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        log_record['@timestamp'] = now
        log_record['level'] = record.levelname
        log_record['logger'] = record.name
        log_record['host_name'] = ElkJsonFormatter.host_name
        log_record['host_ip'] = ElkJsonFormatter.host_ip


class LogUtil(object):

    @staticmethod
    def create_logger(name: str = 'feigua-spider'):

        class LeLevelFilter:
            def __init__(self, level):
                self.level = level

            def filter(self, record):
                return record.levelno <= self.level

        class GtLevelFilter:
            def __init__(self, level):
                self.level = level

            def filter(self, record):
                return record.levelno > self.level

        logger = logging.getLogger(name)
        if len(logger.handlers) > 0:
            return logger

        # logging.basicConfig(format=_LOG_FORMAT)
        formatter = Formatter(
            '%(asctime)s %(levelname)s [%(thread)d-%(threadName)s] %(module)s.%(funcName)s:%(lineno)d %(message)s')

        # 错误日志与普通日志分开记录
        info_handler = StreamHandler(sys.stdout)
        info_handler.setFormatter(formatter)
        info_handler.addFilter(LeLevelFilter(logging.INFO))

        error_handler = StreamHandler(sys.stderr)
        error_handler.setFormatter(formatter)
        error_handler.addFilter(GtLevelFilter(logging.ERROR))

        logging.root.handlers = [info_handler, error_handler]
        logger.setLevel(logging.DEBUG)

        return logger


logger = LogUtil.create_logger('spider')
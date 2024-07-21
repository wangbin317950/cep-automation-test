# encoding: utf-8
"""
@author: SESA734239
@contact: wang.bin@non.se.com
@time: 7/20/2024 9:33 AM
"""
import logging


def assert_equals(actual, expect):
    try:
        assert actual == expect
        logging.info(f'断言成功!实际结果:{actual},预期结果:{expect}')
    except Exception as e:
        logging.error(f'断言失败!实际结果:{actual},预期结果:{expect},异常信息:{e}')
        raise e

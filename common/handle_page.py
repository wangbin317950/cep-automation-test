# encoding: utf-8
"""
@author: SESA734239
@contact: wang.bin@non.se.com
@time: 7/19/2024 9:35 PM
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


class HandlePage:
    """
    所有页面的基类，里面封装了公用的方法
    """

    def __init__(self, driver):
        self.driver = driver

    def wait_element_clickable(self, locator, timeout=8, poll_frequency=0.5):
        try:
            web_element = WebDriverWait(self.driver, timeout, poll_frequency).until(EC.element_to_be_clickable(locator))
        except Exception as e:
            logging.error(f'显示等待元素:{locator}可被点击发生了异常:{e}')
            raise e
        return web_element

    def wait_element_visible(self, locator, timeout=8, poll_frequency=0.5):
        try:
            web_element = WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.visibility_of_element_located(locator))
        except Exception as e:
            logging.error(f'显示等待元素:{locator}可见发生了异常:{e}')
            raise e
        return web_element

    def wait_element_invisible(self, locator, timeout=8, poll_frequency=0.5):
        try:
            web_element = WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.invisibility_of_element_located(locator))
        except Exception as e:
            logging.error(f'显示等待元素:{locator}不可见发生了异常:{e}')
            raise e
        return web_element

    def click(self, locator, **kwargs):
        logging.info(f'对元素:{locator}进行点击')
        self.wait_element_clickable(locator, **kwargs).click()

    def input(self, locator, data, **kwargs):
        logging.info(f'对元素:{locator}进行输入数据:{data}')
        self.wait_element_visible(locator, **kwargs).send_keys(data)

    def get_element_display(self, locator, **kwargs):
        result = self.wait_element_visible(locator, **kwargs).is_displayed()
        logging.info(f'获取元素:{locator}是否显示的结果:{result}')
        return result

    def get_element_text(self, locator, **kwargs):
        text = self.wait_element_visible(locator, **kwargs).text
        logging.info(f'获取元素:{locator}的文本:{text}')
        return text

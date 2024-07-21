# encoding: utf-8
"""
@author: SESA734239
@contact: wang.bin@non.se.com
@time: 7/19/2024 9:39 PM
"""
from common.handle_assert import assert_equals
from page.home_page import HomePage
from page.login_page import LoginPage


def test_login(get_driver, login_fixture):
    """
     测试管理员用户登录
    :param get_driver:
    :param login_fixture:
    :return:
    """
    login_page = LoginPage(get_driver)
    login_page.input_password('Aa123456!')
    login_page.click_login_button()
    assert_equals(HomePage(get_driver).get_admin_text(), 'admin')

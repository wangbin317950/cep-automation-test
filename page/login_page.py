# encoding: utf-8
"""
@author: SESA734239
@contact: wang.bin@non.se.com
@time: 7/19/2024 9:38 PM
"""
from selenium.webdriver.common.by import By
from common.handle_page import HandlePage


class LoginPage(HandlePage):
    password_input_locator = (By.XPATH, '//input[@placeholder="密码"]')
    login_button_locator = (By.XPATH, '//span[text()="登录"]')

    def input_password(self, password):
        self.input(LoginPage.password_input_locator, password)

    def click_login_button(self):
        self.click(LoginPage.login_button_locator)

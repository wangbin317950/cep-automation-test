# encoding: utf-8
"""
@author: SESA734239
@contact: wang.bin@non.se.com
@time: 7/19/2024 9:36 PM
"""
from selenium.webdriver.common.by import By
from common.handle_page import HandlePage


class HomePage(HandlePage):
    dropdown_button_locator = (
        By.CSS_SELECTOR, '.el-dropdown-link.navbar-bg-hover.select-none.el-tooltip__trigger.el-tooltip__trigger')
    logout_button_locator = (By.XPATH, '//li[text()=" 退出系统"]')
    admin_text_locator = (By.XPATH, '//p[text()="admin"]')

    def click_dropdown_button(self):
        self.click(HomePage.dropdown_button_locator)

    def click_logout_button(self):
        self.click(HomePage.logout_button_locator)

    def get_admin_text(self):
        return self.get_element_text(HomePage.admin_text_locator)

# encoding: utf-8
"""
@author: SESA734239
@contact: wang.bin@non.se.com
@time: 7/19/2024 9:41 PM
"""
import logging
import os
import pathlib
import time
import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from datetime import datetime

from common.handle_config import base_url
from common.handle_path import log_path, driver_path
from page.home_page import HomePage
from py.xml import html

driver = None


def pytest_addoption(parser):
    parser.addoption('--env', default="test", choices=['dev', 'test', 'production'],
                     help="命令行参数'--env'设置环境切换")


def pytest_html_report_title(report):
    report.title = "Colibri Expert Platform Test Report"


def pytest_configure(config, get_env):
    config._metadata['BaseUrl'] = base_url[get_env]
    # time_now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    # os.path.join(config.rootdir, 'log', f'{time_now}.log')
    config.option.log_file = log_path


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    """
    th：表头
    td：表格
    :param cells:
    :return:
    """
    cells.insert(2, html.th('Description'))  # 添加描述列（Description）
    cells.insert(1, html.th('Time', class_='sortable time', col='time'))  # 添加可排序时间（Time）列
    cells.pop()  # 删除链接（Link）列


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.insert(1, html.td(datetime.now(), class_='col-time'))
    cells.pop()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    当测试失败的时候，自动截图，展示到html报告中
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
    report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")  # 设置编码显示中文
    print("report::", report)
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        print("xfail::", xfail)
        if (report.skipped and xfail) or (report.failed and not xfail) or report.passed:  # 如果只要测试失败截图，去掉report.passed
            file_name = report.nodeid.replace("::", "_") + ".png"
            print("file_name::", file_name)
            screen_img = driver.get_screenshot_as_base64()
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:242px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """
    收集测试结果
    :param terminalreporter:
    :param exitstatus:
    :param config:
    :return:
    """
    total = terminalreporter._numcollected
    passed = len([i for i in terminalreporter.stats.get('passed', []) if i.when != 'teardown'])
    failed = len([i for i in terminalreporter.stats.get('failed', []) if i.when != 'teardown'])
    error = len([i for i in terminalreporter.stats.get('error', []) if i.when != 'teardown'])
    skipped = len([i for i in terminalreporter.stats.get('skipped', []) if i.when != 'teardown'])
    pass_rate = format(len(terminalreporter.stats.get('passed', [])) / terminalreporter._numcollected * 100, '.2f')
    duration = time.time() - terminalreporter._sessionstarttime
    total_times = str(format(duration, '.2f')) + '秒'  # 时间取2位小数，单位为秒
    logging.info(
        f'本次用例执行结果概览:==> 用例合计数:{total},执行通过数:{passed},执行失败数:{failed},执行报错数:{error},跳过用例数:{skipped},执行成功率:{pass_rate}%,运行总耗时:{total_times}.')


@pytest.fixture(scope='session')
def get_env(request):
    return request.config.getoption('--env')


@pytest.fixture()
def get_driver():
    # pathlib.Path(__file__).absolute().parent / "msedgedriver.exe"
    service = Service(executable_path=driver_path)
    global driver
    driver = webdriver.Edge(service=service)
    driver.maximize_window()
    logging.info("打开Edge浏览器,最大化窗口")
    yield driver
    driver.quit()


@pytest.fixture()
def login_fixture(get_env, get_driver):
    get_driver.get(f'{base_url[get_env]}/login')
    yield
    home_page = HomePage(get_driver)
    home_page.click_dropdown_button()
    home_page.click_logout_button()

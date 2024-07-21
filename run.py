# encoding: utf-8
"""
@author: SESA734239
@contact: wang.bin@non.se.com
@time: 7/19/2024 9:44 PM
"""

import pytest

from common.handle_path import report_path

"""
运行命令
python run.py
pytest --count=3 --repeat-scope=function
"""
# ./report/{time_now}.html
pytest.main(
    [
        '-v',
        '-s',
        # '--env=dev'
        # 'case/test_login.py::test_login',
        # '--count=3',
        # '--repeat-scope=function',
        f'--html={report_path}',
        '--self-contained-html'
    ]
)

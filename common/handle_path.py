# encoding: utf-8
"""
@author: SESA734239
@contact: wang.bin@non.se.com
@time: 7/19/2024 10:11 PM
"""
import pathlib
import time

time_now = time.strftime("%Y-%m-%d_%H-%M-%S")
report_path = str(pathlib.Path(__file__).parent.parent / "report" / "report.html")
log_path = str(pathlib.Path(__file__).parent.parent / "log" / f"{time_now}.log")
driver_path = str(pathlib.Path(__file__).parent.parent / "msedgedriver.exe")

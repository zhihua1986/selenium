# -*-coding:utf-8-*-
# _author_ = "janehost"
import os
import smtplib
import sys
import time
import unittest
from email.mime.text import MIMEText

from HTMLTestRunner import HTMLTestRunner

now = time.strftime("%Y-%m-%d %H_%M_%S")
filename = './report/' + now + 'result.html'
fp = open(filename, 'wb')
runner = HTMLTestRunner(stream=fp, title='全渠道自动化测试报告',
                        description='环境：windows 7 浏览器：Chrome')
discover = unittest.defaultTestLoader.discover('tase_case/',
                                               pattern='*_sta.py')
runner.run(discover)
fp.close()
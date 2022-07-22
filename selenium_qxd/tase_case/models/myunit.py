'''定义测试框架类,用于集成unittest.TestCase类，因为笔者创建的所有测试类中setUp()与tearDown()方法所做的
事情相同，所以，将他们抽象为MyTest()类，好处就是在编写测试用例时不再考虑这两个方法的实现。'''
from .driver import *
import unittest
import ddt
from selenium.common.exceptions import NoSuchElementException
import sys
from selenium import webdriver

class Mytest(unittest.TestCase):
    def setUp(self):
        self.driver=browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()



    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()

# -*-coding:utf-8-*-
# _author_ = "janehost"
from time import sleep
import unittest, random, sys
from models import myunit, function
from page_obj.loginPage import Login



class loginTest(myunit.Mytest):
    def user_login_verify(self, company='辉煌测试',username="", password=""):
        Login(self.driver).user_login(company,username,password)

    def test_login1(self):


        '''用户名、密码为空登录'''
        self.user_login_verify(company='辉煌测试',username="", password="")
        po = Login(self.driver)
        self.assertEqual(po.login_error_hint(), '用户名不能为空！')
        function.insert_img(self.driver, "user_pawd_empty.jpg")

    def test_login2(self):
        '''用户名正确，密码为空登录验证'''
        self.user_login_verify(username="admin")
        po = Login(self.driver)
        self.assertIn(po.login_error_hint(),'对不起，密码错误，请重新输入密码！\n\n密码的字母必须使用正确的大小写。\n\n密码错误5次将锁住该用户，已错误1次！' )
        function.insert_img(self.driver,"pawd_empty.jpg")

    def test_login3(self):
        '''用户名为空，密码正确'''
        self.user_login_verify(password="12345678a")
        po = Login(self.driver)
        self.assertEqual(po.login_error_hint(), '用户名不能为空！')
        function.insert_img(self.driver, "user_empty.jpg")

    def test_login4(self):
        '''用户名和密码不匹配'''

        self.user_login_verify(username='admin', password="2sdfd")
        po = Login(self.driver)
        self.assertIn(po.login_error_hint(), '对不起，密码错误，请重新输入密码！\n\n密码的字母必须使用正确的大小写。\n\n密码错误5次将锁住该用户，已错误2次！' )
        function.insert_img(self.driver, "pass_error.jpg")

    def test_login5(self):
        '''用户名、密码正确'''
        self.user_login_verify(username="admin", password="12345678a")
        sleep(3)
        po = Login(self.driver)
        self.assertEqual(self.driver.title, '管家婆全渠道')
        function.insert_img(self.driver, "user_pwd_true.jpg")
if __name__ == '__main__':
    unittest.main()

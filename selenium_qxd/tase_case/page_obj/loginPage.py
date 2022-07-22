# 用户登录页面
from .base import *

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
class Login(Page):
    url = '/'
    company_loc = (By.ID,'$f3abfdbe$CompanyName')
    login_user_loc = (By.ID,'$f3abfdbe$UserCode')
    login_password_loc = (By.ID,'$f3abfdbe$PassWord')
    login_button_loc = (By.ID,'$f3abfdbe$btnLogin')
    # 登录错误的提示定位
    login_error_loc = (By.XPATH,'/html/body/table/tbody/tr[2]/td/div/table/tbody/tr/td/table/tbody/tr[1]/td[2]/table/tbody/tr/td')

    # 输入公司名、
    def login_company(self,company):
        self.find_element(*self.company_loc).clear()
        self.find_element(*self.company_loc).send_keys(company)
    # 输入用户名
    def login_username(self,username):
        self.find_element(*self.login_user_loc).clear()
        self.find_element(*self.login_user_loc).send_keys(username)
    # 输入密码
    def login_password(self,password):
        self.find_element(*self.login_password_loc).clear()
        self.find_element(*self.login_password_loc).send_keys(password)
    # 登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    # 统一登录入口
    def user_login(self, company= "辉煌测试",username = "admin",password="12345678a"):




        # 获取用户名和页面登录
        self.open()
        self.xf = self.driver.find_element_by_id('contentFrame')
        self.swtich_frame(self.xf)
        #self.driver.swtich_to_frame(self.xf)


        #self.swtich_frame(By.ID,'contentFrame')

        self.login_company(company)
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        time.sleep(5)
    # 登录错位提示信息
    def login_error_hint(self):
        return self.find_element(*self.login_error_loc).text






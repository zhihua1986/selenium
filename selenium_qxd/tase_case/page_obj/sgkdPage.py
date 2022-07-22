from page_obj.base import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from page_obj.loginPage import Login
from selenium.common.exceptions import  NoSuchElementException
import csv

# 手工开单界面
class Sgkd(Page):
    url = '/'
    # 新增单据按钮的定位
    bill_button_loc = (By.ID,'$f8c81e13$Add')
    # 手工开单标题的定位
    title_loc = (By.XPATH,'//*[contains(text(),"手工开单")]')
    # 网店名称的定位
    shop_name_loc = (By.CLASS_NAME,'ButtonEdit')
    shopbutton_name_loc = (By.ID,'$2b5e41ce$button4')
    # 业务员的定位
    Salesman_loc = (By.XPATH,'//*[@id="$e527fc78$MainPanel"]/div[2]/div[2]/div/div[1]/table/tbody/tr[2]/td[4]/table/tbody/tr/td[2]/div/div')
    Salesman_button_loc = (By.ID,'$cf1dd51f$button3')
    # 订单编号
    order_number_sendkeys = (By.XPATH, '//*[@id="$e527fc78$MainPanel"]/div[2]/div[2]/div/div[1]/table/tbody/tr[2]/td[6]/input')
    # 发货仓库定位
    whs_loc = (By.XPATH,'//*[@id="$e527fc78$MainPanel"]/div[2]/div[2]/div/div[1]/table/tbody/tr[2]/td[8]/table/tbody/tr/td[2]/div/div')

    whs_button_loc = (By.ID,'$5944506d$button4')
    # 买家账号
    buyaccount_loc = (By.XPATH, '//*[@id="$e527fc78$MainPanel"]/div[2]/div[2]/div/div[1]/table/tbody/tr[3]/td[2]/input')
    # 开单日期的定位
    date_loc = (By.ID,'//*[@id="$e527fc78$MainPanel"]/div[2]/div[2]/div/div[1]/table/tbody/tr[2]/td[10]/table/tbody/tr/td[2]/div/div')
    today_date_loc = (By.CLASS_NAME,'TodayButton Button')
    # 收货人的定位
    receiver_loc = (By.XPATH,'//*[@id="$e527fc78$MainPanel"]/div[2]/div[2]/div/div[1]/table/tbody/tr[3]/td[4]/table/tbody/tr/td[1]/input')
    # 手机号码的定位
    phone_number_loc = (By.XPATH,'//*[@id="$e527fc78$MainPanel"]/div[2]/div[2]/div/div[1]/table/tbody/tr[3]/td[8]/input')
    # 收货地区
    area_loc = (By.XPATH,'//*[@id="$e527fc78$MainPanel"]/div[2]/div[2]/div/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td[2]/div/div')
    #area_province_loc = (By.XPATH,'//*[contains(text(),\'%s\')]'%list1[0]['province'])
    #area_province_loc = (By.XPATH, '//*[contains(text(),\'%s\')]' %s)
    #area_city_loc = (By.XPATH,'//*[contains(text(),\'%s\')]'%list1[0]['city'])
    #area_city_loc = (By.XPATH,'//*[contains(text(),\'%s\')]'%s)
    #area_selected_loc = (By.XPATH,'//*[contains(text(),\'%s\')]'%list1[0]['area'])
    area_button_loc = (By.ID,'$1862ecd4$button1')
    # 详细地址定位
    detailed_address_loc = (By.XPATH,'//*[@id="$e527fc78$MainPanel"]/div[2]/div[2]/div/div[1]/table/tbody/tr[4]/td[4]/input')
    # 住来单位定位
    supplier_loc = (By.XPATH,'//*[@id="$e527fc78$MainPanel"]/div[2]/div[2]/div/div[1]/table/tbody/tr[5]/td[12]/table/tbody/tr/td[2]/div/div')
    supplier_button_loc = (By.ID,'$5af49555$button4')
    # 选择商品定位
    cells_loc = (By.XPATH,"//table[@class='GridBodyRows']/tbody/tr/td[2]")
    #select_shop_loc = (By.XPATH,"//*[contains(@id,'$GoodsInfoGrid_column0')]/div/table/tbody/tr/td/input")
    select_button_loc = (By.CLASS_NAME,'Ok')
    # 数量框的定位
    number_loc1 = (By.XPATH, '//*[contains(@id,"$Grid")]/div[2]/table/tbody/tr[1]/td[17]/div')
    number_loc2 = (By.XPATH, '//*[contains(@id,"$Grid")]/div[2]/table/tbody/tr[1]/td[17]/table/tbody/tr/td[1]/input')
    # 单价框的定位
    price_loc1 = (By.XPATH, '//*[contains(@id,"$Grid")]/div[2]/table/tbody/tr[1]/td[19]/div')
    price_loc2 = (By.XPATH, '//*[contains(@id,"$Grid")]/div[2]/table/tbody/tr[1]/td[19]/table/tbody/tr/td[1]/input')

    # 赠品的定位
    gift_loc = (By.XPATH, '//*[contains(@id,"$Grid")]/div[2]/table/tbody/tr[1]/td[21]')
    gift_loc2 = (By.XPATH, '//*[contains(@id,"$Grid")]/div[2]/table/tbody/tr[1]/td[21]/div/input')
    # 保存订单定位
    save_button_loc =(By.CLASS_NAME,'Save')
    # 过账错误提示的定位
    bill_error_loc = (By.XPATH,'/html/body/table[2]/tbody/tr[2]/td/div/table/tbody/tr/td/table/tbody/tr[1]/td[2]/table/tbody/tr/td')
    # 选择开单按钮
    def bill_button(self):
        self.find_element(*self.bill_button_loc).click()
        time.sleep(5)
    # 新增标题
    def select_title(self):

        return self.find_element(*self.bill_button_loc).text


    # 选择网店
    def shop_name(self):
        self.find_element(*self.shop_name_loc).clear()
        double_click=self.find_element(*self.shop_name_loc)
        ActionChains(self.driver).double_click(double_click).perform()
        time.sleep(5)
        self.find_element(*self.shopbutton_name_loc).click()
    # 选择业务员
    def salesman(self,salesman):
        salesman_select=(By.XPATH, '//*[contains(text(),\'%s\')]'% salesman)
        self.find_element(*self.Salesman_loc).click()
        self.find_element(*salesman_select).click
        time.sleep(5)
        self.find_element(*self.Salesman_button_loc).click()

    # 订单编号
    def order_number(self,number):

        self.driver.find_element(*self.order_number_sendkeys).send_keys(number)
    # 选择发货仓库
    def whs(self,whs):
        whs_select= (By.XPATH, '//*[contains(text(),\'%s\')]'% whs)

        self.find_element(*self.whs_loc).click()
        time.sleep(3)
        self.find_element(*whs_select).click()
        time.sleep(5)
        self.find_element(*self.whs_button_loc).click()
    # 买家账号
    def buyaccount(self,account):

        self.find_element(*self.buyaccount_loc).send_keys(account)
    # 输入收货人
    def receiver_send(self,receiver):
        self.find_element(*self.receiver_loc).send_keys(receiver)
    # 输入手机号码
    def phone_number(self,phone):
        self.find_element(*self.phone_number_loc).send_keys(phone)
    # 选择收获地区
    def area(self):
        self.find_element(*self.area_loc).click()
        time.sleep(5)
    def area_province(self,province):
        area_province_loc = (By.XPATH, '//*[contains(text(),\'%s\')]'%province)

        double_click = self.find_element(*area_province_loc)

        ActionChains(self.driver).double_click(double_click).perform()
        time.sleep(5)
    def area_city(self,city):
        area_city_loc = (By.XPATH, '//*[contains(text(),\'%s\')]'%city)
        double_click = self.find_element(*area_city_loc)
        ActionChains(self.driver).double_click(double_click).perform()

        time.sleep(5)
    def area_select(self,area):
        area_selected_loc = (By.XPATH, '//*[contains(text(),\'%s\')]'%area)
        self.find_element(*area_selected_loc).click()
        time.sleep(3)
        self.find_element(*self.area_button_loc).click()
    # 输入详细地址
    def detailed_address(self,address):
        time.sleep(3)
        self.find_element(*self.detailed_address_loc).send_keys(address)

    # 往来单位
    def supplier_a(self,supplier):
        supplier_select= (By.XPATH,'//*[contains(text(),\'%s\')]'% supplier)
        self.find_element(*self.supplier_loc).click()
        time.sleep(3)
        self.find_element(*supplier_select).click()
        self.find_element(*self.supplier_button_loc).click()
    # 选择商品
    def cells_send(self,shop):
        select_shop_loc = (By.XPATH,"//*[contains(text(),\'%s\')]"% shop)
        double_click = self.find_element(*self.cells_loc)
        ActionChains(self.driver).double_click(double_click).perform()
        time.sleep(3)
        self.find_element(*select_shop_loc).click()
        self.find_element(*self.select_button_loc).click()
    # 输入数量
    def number_send(self,amount):

        self.find_element(*self.number_loc1).click()
        self.find_element(*self.number_loc2).send_keys(amount)
    # 输入单价
    def price_send(self,price):


        self.find_element(*self.price_loc1).click()
        self.find_element(*self.price_loc2).send_keys(price)


    # 赠品选择
    def gift_select(self):
        self.driver.implicitly_wait(10)


        self.find_element(*self.gift_loc).click()
        self.find_element(*self.gift_loc2).click()


    # 保存按钮
    def save_button(self):
        self.find_element(*self.save_button_loc).click()
    # 过账单据错误提示
    def bill_error(self):
        return self.find_element(*self.bill_error_loc).text
    # 打开单据
    def open_bill(self):

        '''self.open()
        self.xf = self.driver.find_element_by_id('contentFrame')

        self.swtich_frame(self.xf)'''
        Login(self.driver).user_login()
        self.xf = self.driver.find_element_by_id('contentFrame')
        self.swtich_frame(self.xf)
        time.sleep(3)
        self.bill_button()
        time.sleep(5)
    # 统一过账入口
    def save_bill(self,salesman,number,whs,account,receiver,phone,province,city,area,address,supplier,shop,amount,price):



        self.shop_name()
        self.salesman(salesman)
        self.order_number(number)
        time.sleep(3)
        self.whs(whs)
        self.buyaccount(account)
        self.receiver_send(receiver)
        self.phone_number(phone)
        self.area()
        self.area_province(province)
        self.area_city(city)
        self.area_select(area)
        self.detailed_address(address)
        self.supplier_a(supplier)
        self.cells_send(shop)
        self.number_send(amount)
        self.price_send(price)





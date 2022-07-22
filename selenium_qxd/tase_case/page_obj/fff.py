from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

import time
driver=webdriver.Chrome()
driver.get('http://local.gjpqqd.com:8081')
xf=driver.find_element_by_id('contentFrame')
driver.switch_to_frame(xf)

driver.maximize_window()
# 登录
driver.find_element(By.ID,'$f3abfdbe$CompanyName').send_keys('辉煌测试')
driver.find_element_by_id('$f3abfdbe$UserCode').send_keys('admin')
driver.find_element_by_id('$f3abfdbe$PassWord').send_keys('12345678a')
driver.find_element_by_id('$f3abfdbe$btnLogin').click()
time.sleep(3)
xf=driver.find_element_by_id('contentFrame')
driver.switch_to_frame(xf)
driver.find_element(By.ID,'$f8c81e13$Add').click()
#a=driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td').accept()
#a=driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/div/table/tbody/tr/td/table/tbody/tr[1]/td[2]/table/tbody/tr/td').text
#a=driver.find_element_by_id('$e527fc78$imageBtnLogOff').id
time.sleep(3)
a=driver.find_element_by_xpath('//*[@id="$e527fc78$MainPanel"]/div[1]/div[2]/table/tbody/tr/td[2]/table/tbody/tr/td[2]/table/tbody/tr/td[1]/div').text
print(a)
# 网店
double_click1=driver.find_element(By.CLASS_NAME,'ButtonEdit')
ActionChains(driver).double_click(double_click1).perform()
time.sleep(3)
driver.find_element(By.ID,'$2b5e41ce$button4').click()
# 业务员
driver.find_element(By.XPATH,'//*[@id="$e527fc78$MainPanel"]/div[2]/div[2]/div/div[1]/table/tbody/tr[2]/td[4]/table/tbody/tr/td[2]/div/div').click()
time.sleep(5)
#driver.find_element(By.XPATH,'//*[@id="$cf1dd51f$Grid"]/div[2]/table/tbody/tr').click()

driver.find_element(By.XPATH, '//*[contains(text(),"zy1")]').click()
driver.find_element(By.ID,'$cf1dd51f$button3').click()
# 订单编号
driver.find_element(By.XPATH,'//*[@id="$e527fc78$MainPanel"]/div[2]/div[2]/div/div[1]/table/tbody/tr[2]/td[6]/input').send_keys('45435435543')
# 发货仓库
driver.find_element(By.XPATH,'//*[@id="$e527fc78$MainPanel"]/div[2]/div[2]/div/div[1]/table/tbody/tr[2]/td[8]/table/tbody/tr/td[2]/div/div').click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[contains(text(),"ck1")]').click()
driver.find_element(By.ID,'$5944506d$button4').click()
# 买家帐号
driver.find_element(By.XPATH,'//*[@id="$e527fc78$MainPanel"]/div[2]/div[2]/div/div[1]/table/tbody/tr[3]/td[2]/input').send_keys('123456')
# 收货人
driver.find_element(By.XPATH,'//*[@id="$e527fc78$MainPanel"]/div[2]/div[2]/div/div[1]/table/tbody/tr[3]/td[4]/table/tbody/tr/td[1]/input').send_keys('四川成都')
# 手机
driver.find_element(By.XPATH,'//*[@id="$e527fc78$MainPanel"]/div[2]/div[2]/div/div[1]/table/tbody/tr[3]/td[8]/input').send_keys('18328710328')
#收货地区
driver.find_element(By.XPATH,'//*[@id="$e527fc78$MainPanel"]/div[2]/div[2]/div/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td[2]/div/div').click()
time.sleep(3)
cell_data = csv.DictReader(open(r'C:\Users\Administrator\PycharmProjects\selenium_qxd\test_data\cell.csv','r'))
list1=[]
for cell in cell_data:
    list1.append(cell)

double_click=driver.find_element(By.XPATH,'//*[contains(text(),\'%s\')]'%list1[0]['province'])
    #double_click = driver.find_element(By.XPATH, '//*[contains(text(),"四川省")]')

ActionChains(driver).double_click(double_click).perform()

time.sleep(3)
double_click=driver.find_element(By.XPATH,'//*[contains(text(),\'%s\')]'%list1[0]['city']).click()
ActionChains(driver).double_click(double_click).perform()
time.sleep(3)
driver.find_element(By.XPATH,'//*[contains(text(),\'%s\')]'%list1[0]['area']).click()


driver.find_element(By.ID,'$1862ecd4$button1').click()
# 详细地址
driver.find_element(By.XPATH,'//*[@id="$e527fc78$MainPanel"]/div[2]/div[2]/div/div[1]/table/tbody/tr[4]/td[4]/input').send_keys('四川成都双流花样年别样城')
time.sleep(3)
#住来单位
driver.find_element(By.XPATH,'//*[@id="$e527fc78$MainPanel"]/div[2]/div[2]/div/div[1]/table/tbody/tr[5]/td[12]/table/tbody/tr/td[2]/div/div').click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[contains(text(),"dw1")]').click()
driver.find_element(By.ID,'$5af49555$button4').click()
# 选择商品
double_click=driver.find_element(By.XPATH,"//table[@class='GridBodyRows']/tbody/tr[7]/td[2]")

ActionChains(driver).double_click(double_click).perform()
time.sleep(3)
#driver.find_element(By.XPATH,"//div[@class='GridHeaderCaptionText']/table/tbody/tr/td/input").click()

driver.find_element(By.XPATH,'//*[contains(text(),"sp1")]').click()

time.sleep(3)
driver.find_element(By.CLASS_NAME,'Ok').click()
# 数量输入

#driver.find_element(By.XPATH,'//table[@class="GridBodyRows"]/tbody/tr/td[17]').click()
driver.find_element(By.XPATH,'//*[contains(@id,"$Grid")]/div[2]/table/tbody/tr[1]/td[17]/div').click()
driver.find_element(By.XPATH,'//*[contains(@id,"$Grid")]/div[2]/table/tbody/tr[1]/td[17]/table/tbody/tr/td[1]/input').send_keys(6)

# 第一个单价输入
#driver.find_element(By.XPATH,'//*[@class="GridBodyCell"and @_columnindex="17"]/div').click()
driver.find_element(By.XPATH,'//*[contains(@id,"$Grid")]/div[2]/table/tbody/tr[1]/td[19]/div').click()
driver.find_element(By.XPATH,'//*[contains(@id,"$Grid")]/div[2]/table/tbody/tr[1]/td[19]/table/tbody/tr/td[1]/input').send_keys(10)

'''第二个单价输入
driver.find_element(By.XPATH,'//*[contains(@id,"$Grid")]/div[2]/table/tbody/tr[2]/td[19]/div').click()
driver.find_element(By.XPATH,'//*[contains(@id,"$Grid")]/div[2]/table/tbody/tr[2]/td[19]/table/tbody/tr/td[1]/input').send_keys(20)'''
# 赠品选择

driver.find_element(By.XPATH,'//*[contains(@id,"$Grid")]/div[2]/table/tbody/tr[1]/td[21]').click()
driver.find_element(By.XPATH,'//*[contains(@id,"$Grid")]/div[2]/table/tbody/tr[1]/td[21]/div/input').click()
time.sleep(5)
driver.find_element(By.CLASS_NAME,'Save').click()
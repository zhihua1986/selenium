from selenium import webdriver
import sys,os

def insert_img (driver,file_name):
    #获取当前路径的地址
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = base_dir.replace('\\','/')
    base = base_dir.split('tase_case')[0]
    file_path = base +'report/image/'+file_name
    driver.get_screenshot_as_file(file_path)
if __name__ == '__main__':
    driver=webdriver.Chrome()
    driver.get('http://local.gjpqqd.com:8081/')
    insert_img(driver,'login.jpg')
    driver.quit()




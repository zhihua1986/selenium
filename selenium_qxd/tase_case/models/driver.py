# 定义浏览器驱动函数browser()
from selenium import webdriver


def browser():
    driver=webdriver.Chrome()
    return driver
if __name__ == '__main__':
    driver = browser()
    driver.get('http://local.gjpqqd.com:8081')
    driver.quit()

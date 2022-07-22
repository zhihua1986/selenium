from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys,os

'''
   页面基础类，用于所有页面的继承
   '''
class Page(object):
    base_url='http://local.gjpqqd.com:8081'
    def __init__(self, driver, base_url=base_url, parent=None):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30
        self.parent = parent
    def _open (self,url):
        url = self.base_url + url
        self.driver.get(url)

        assert self.on_page(), 'Did not land on %s' % url
    def open(self):
        self._open(self.url)
    def on_page(self):


        return self.driver.current_url == (self.base_url+self.url)

    def find_element(self,*loc):


        return self.driver.find_element(*loc)
    def find_elements(self,*loc):

        return self.driver.find_elements(*loc)
    def script(self,src):
        return  self.driver.execute_script()
    def swtich_frame(self,loc):
        return self.driver.switch_to_frame(loc)


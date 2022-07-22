
import unittest
from models import myunit, function
from page_obj.sgkdPage import Sgkd
import csv
import time

from page_obj.base import Page
cell_data = csv.DictReader(open(r'C:\Users\Administrator\PycharmProjects\selenium_qxd\test_data\cell.csv','r'))
list1=[]
for cell in cell_data:
    list1.append(cell)

class SgkdTest(myunit.Mytest):
    def test_sgkd(self):
        po = Sgkd(self.driver)
        po.open_bill()
        for list in list1:


            po.save_bill(list['salesman'],list['number'],list['whs'],list['account'],list['receiver'],list['phone'],(list['province']),(list['city']),(list['area']),list['address'],list['supplier'],list['shop'],list['amount'],list['price'])
            if list['gift']=='是':

                po.gift_select()
                po.save_button()
                time.sleep(5)
                #self.assertEqual()


    if __name__=='__main__':
        unittest.main()



import unittest
from models import myunit, function
from page_obj.sgkdPage import Sgkd
import csv
import time
import ddt
cell_data = csv.DictReader(open(r'C:\Users\Administrator\PycharmProjects\selenium_qxd\test_data\cell.csv','r'))
list1=[]
for cell in cell_data:
    list1.append(cell)
@ddt.ddt
class SgkdTest(myunit.Mytest):
    @ddt.data(*list1)
    def test_sgkd(self,list):
        po = Sgkd(self.driver)
        if self.driver.current_url!='http://local.gjpqqd.com:8081':
            po.open_bill()
        po.save_bill(list['salesman'],list['number'],list['whs'],list['account'],list['receiver'],list['phone'],(list['province']),(list['city']),(list['area']),list['address'],list['supplier'],list['shop'],list['amount'],list['price'])
        if list['gift']=='是':
            po.gift_select()

        else:
            po.save_button()
            time.sleep(5)
            self.assertEqual(po.bill_error(),list['预期结果'])
            function.insert_img(self.driver, po.bill_error())
if __name__=='__main__':
        unittest.main()


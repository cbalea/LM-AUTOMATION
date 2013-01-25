'''
Created on 18.09.2012

@author: cbalea
'''
from time import gmtime, strftime
from utils.driver_factory import DriverFactory
from utils.selenium_test_base import SeleniumTestBase
from utils.server_related import ServerRelated


class SeleniumTestBaseCMS(SeleniumTestBase):
    
    def getCurrentDate(self):
        return strftime("%Y-%m-%d", gmtime()) 
    
    def setUp(self):
        self.setup_wit_cookies_load()
        self.driver.get(ServerRelated().serverToBeTested()+"/admin/")




class SeleniumTestBaseNoLoginCMS(SeleniumTestBase):

    def setUp(self):
        self.driver = DriverFactory().initializeDriver()
        self.wait = DriverFactory().initializeWait(self.driver)
        self.driver.maximize_window()
        self.driver.get(ServerRelated().serverToBeTested()+"/admin/")
        
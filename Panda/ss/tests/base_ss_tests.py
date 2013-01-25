'''
Created on 18.09.2012

@author: cbalea
'''
from utils.driver_factory import DriverFactory
from utils.selenium_test_base import SeleniumTestBase


class SeleniumTestBaseSS(SeleniumTestBase):
    
    def setUp(self):
        self.setup_wit_cookies_load()


class SeleniumTestBaseNoLoginSS(SeleniumTestBase):
    
    def setUp(self):
        self.driver = DriverFactory().initializeDriver()
        self.wait = DriverFactory().initializeWait(self.driver)
        self.driver.maximize_window()
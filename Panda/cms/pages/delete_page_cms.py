'''
Created on 11.10.2012

@author: cbalea
'''
from utils.base_page import BasePage



class DeletePageCMS(object):
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.confirmationButton = self.wait.until(lambda driver : driver.find_element_by_xpath("//input[@type='submit']"))
    
    def clickConfirmationButton(self):
        self.confirmationButton.click()
        return BasePage(self.driver, self.wait)

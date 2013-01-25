'''
Created on 09.10.2012

@author: cbalea
'''
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
import time

class BasePage(object):
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def elementExistsByClassName(self, className):
        try:
            return self.driver.find_element_by_class_name(className) 
        except NoSuchElementException:
            return False
    
    def elementExistsById(self, id):
        try:
            return WebDriverWait(self.driver, 5).until(lambda driver : driver.find_element_by_id(id))
        except TimeoutException:
            return False
    
    def elementExistsByXpath(self, xpath):
        try:
            return WebDriverWait(self.driver, 5).until(lambda driver : driver.find_element_by_xpath(xpath))
        except TimeoutException:
            return False
    
    def elementsExistByXpath(self, xpath):
        try:
            return WebDriverWait(self.driver, 2).until(lambda driver : driver.find_elements_by_xpath(xpath))
        except TimeoutException:
            return False
    
    def elementExistsByLinkText(self, linkText):
        try:
            return WebDriverWait(self.driver, 5).until(lambda driver : driver.find_element_by_xpath("//a[text()='%s']" %linkText)) 
        except TimeoutException:
            return False
    
    def isCheckboxChecked(self, checkbox):
        if(checkbox.get_attribute("checked")=="true"):
            return True
        return False
    
    def clickOnLink(self, link):
        self.wait.until(lambda driver : driver.find_element_by_xpath("//a[text()='%s']" %link)).click()

    def sublistExistsInList(self, sublist, big_list):
        for element in sublist:
            if(big_list.index(element) == None):
                return False
        return True
    
    def switchToNewestWindow(self):
        self.waitUntilPopupOpens()
        for handle in self.driver.window_handles:
            self.driver.switch_to_window(handle)
    
    def waitUntilPopupCloses(self):
        windows = len(self.driver.window_handles)
        while(windows > 1):
            time.sleep(1)
            windows = len(self.driver.window_handles)
    
    def waitUntilPopupOpens(self):
        windows = len(self.driver.window_handles)
        timeout=3
        while(windows == 1 and timeout < 0):
            time.sleep(1)
            windows = len(self.driver.window_handles)
            timeout -=1
        if(timeout == 0):
            raise Exception("Popup did not open")
    
    def typeInTinymceEditor(self, iframe, text):
        self.wait.until(lambda driver : driver.find_element_by_xpath("//iframe[@id='%s']" %iframe))
        self.driver.switch_to_frame(iframe)
        self.tinymceEditor = self.driver.switch_to_active_element()
        self.tinymceEditor.click()
        self.tinymceEditor.clear()
        self.tinymceEditor.send_keys(text)
        self.switchToNewestWindow()
    
    def getOptionsTextInCombobox(self, combobox):
        optionElements = combobox.options
        optionsText = [] 
        for element in optionElements:
            optionsText.append(element.text)
        return optionsText
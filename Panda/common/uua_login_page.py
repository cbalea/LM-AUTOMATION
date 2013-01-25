'''
Created on 10.12.2012

@author: cbalea
'''
from selenium.webdriver.remote.webelement import WebElement

class UuaLoginPage(object):
    
    emailField = WebElement(None, None)
    passwordField = WebElement(None, None)
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        driver.switch_to_frame("popup")
        self.emailField = self.wait.until(lambda driver : driver.find_element_by_xpath("//input[@id='id_username']"))
        self.passwordField = self.wait.until(lambda driver : driver.find_element_by_id("id_password"))
        self.createAccountButton = self.wait.until(lambda driver : driver.find_element_by_xpath("//button[contains(@onclick, '/register/')]")) 
        
        
    def typeEmail(self, username):
        self.emailField.send_keys(username)
        
    def typePassword(self, password):
        self.passwordField.send_keys(password)
        
    def submitForm(self):
        self.emailField.submit()
    
    def login(self, username, password):
        self.typeEmail(username)
        self.typePassword(password)
        self.submitForm()
    
    def uua_login_page_is_displayed(self):
        return self.emailField.is_displayed()
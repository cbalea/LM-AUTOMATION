'''
Created on 14.09.2012

@author: cbalea
'''
from common.uua_login_page import UuaLoginPage

class LoginPageCMS(object):
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.username = self.wait.until(lambda driver : driver.find_element_by_id("id_username"))
        self.passwordField = self.wait.until(lambda driver : driver.find_element_by_id("id_password"))
        self.uuaLoginLink = self.wait.until(lambda driver : driver.find_element_by_id("uua_login"))
        
    def typeUsername(self, username):
        self.username.send_keys(username)
        
    def typePassword(self, password):
        self.passwordField.send_keys(password)
        
    def submitForm(self):
        self.username.submit()
    
    def login(self, username, password):
        self.typeUsername(username)
        self.typePassword(password)
        self.submitForm()

    def clickLoginWithYourPbsAccountLink(self):
        self.uuaLoginLink.click()
        return UuaLoginPage(self.driver, self.wait)
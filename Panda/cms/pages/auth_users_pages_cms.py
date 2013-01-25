'''
Created on 07.12.2012

@author: cbalea
'''
from cms.pages.base_page_cms import BasePageCMS
from utils.server_related import ServerRelated

class AuthUsersPageCMS(BasePageCMS):
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.driver.get (ServerRelated().serverToBeTested() + "admin/auth/user/")
    
    def openPageForUser(self, username):
        self.clickOnLink(username)
        return EditUserPageCMS(self.driver, self.wait)




class EditUserPageCMS(BasePageCMS):
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.activeCheckbox = self.wait.until(lambda driver : driver.find_element_by_id("id_is_active"))
    
    def checkActiveCheckbox(self):
        if(self.isCheckboxChecked(self.activeCheckbox) == False):
            self.activeCheckbox.click()
    
    def clickSaveAndContinueEditingButton(self):
        self.clickSaveAndContinueEditing()
        return EditUserPageCMS(self.driver, self.wait)
'''
Created on Oct 31, 2012

@author: jseichei
'''
from cms.pages.base_page_cms import BasePageCMS
from selenium.webdriver.support.select import Select
from utils.server_related import ServerRelated


class RequiredAttributionPageCMS(object):
    
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.driver.get(ServerRelated().serverToBeTested() + "admin/cms/requiredattribution")
        self.addRequiredAttribution = self.wait.until(lambda driver : driver.find_element_by_xpath(".//*[@class='addlink']"))
        
        
    def clickToAddRequiredAttributionButton(self):
        self.addRequiredAttribution.click()
        return AddRequiredAttribution(self.driver, self.wait)
            
        
class AddRequiredAttribution(BasePageCMS):  
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.entityBox = Select(self.wait.until(lambda driver :driver.find_element_by_id("id_entity")))
        self.roleBox = Select(self.wait.until(lambda driver :driver.find_element_by_id("id_role")))
        self.requiredAttributionTextArea = self.wait.until(lambda driver :driver.find_element_by_xpath(".//*[@id='id_text']"))
                                                                                
    
    
    def selectEntity(self):
        self.entityBox.select_by_index(2)
        
        
    def selectRole(self, role):
        self.roleBox.select_by_visible_text(role)
        
        
    def writeInTextArea(self, requiredAttributionText):
        self.requiredAttributionTextArea.send_keys(requiredAttributionText)
        
    
    def clickToSaveAndContinue(self):
        self.clickSaveAndContinueEditing()
        return AddRequiredAttribution(self.driver, self.wait)
        
        
    def getSelectedEntity(self):
        return self.entityBox.first_selected_option.text
    
    
    def getSelectedRole(self):
        return self.roleBox.first_selected_option.text    
    
    
    
        
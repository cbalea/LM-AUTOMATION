'''
Created on 14.11.2012

@author: cbalea
'''
from cms.pages.base_page_cms import BasePageCMS
from utils.server_related import ServerRelated


class EntitiesPageCMS(BasePageCMS):
    
    def __init__(self, driver, wait, noReload = None):
        self.driver = driver
        self.wait = wait
        if (noReload == None):
            self.driver.get(ServerRelated().serverToBeTested() + "admin/cms/entity/")
    
    def clickAddEntity(self):
        self.clickAddButton()
        return EditEntityPageCMS(self.driver, self.wait)



class EditEntityPageCMS(BasePageCMS):
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.name = self.wait.until(lambda driver : driver.find_element_by_id("id_name"))
    
    def typeName(self, value):
        self.name.send_keys(value)
    
    def clickSaveButton(self):
        self.clickSave()
        return EntitiesPageCMS(self.driver, self.wait)
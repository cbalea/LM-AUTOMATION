'''
Created on 14.11.2012

@author: cbalea
'''
from cms.pages.base_page_cms import BasePageCMS
from utils.server_related import ServerRelated


class CountiesPageCMS(BasePageCMS):
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.driver.get(ServerRelated().serverToBeTested() + "admin/authorization/county/")
        self.results = self.wait.until(lambda driver : driver.find_elements_by_xpath("//table[@id='result_list']/tbody/tr/th/a"))
    
    def clickCountyByIndex(self, index):
        self.clickItemInListTableByIndex(index)
        return EditCountyPageCMS(self.driver, self.wait)
    
    def getNumberOfDisplayedCounties(self):
        return len(self.results)
    


class EditCountyPageCMS(BasePageCMS):
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
    
    def clickSaveButton(self):
        self.clickSave()
        return CountiesPageCMS(self.driver, self.wait)
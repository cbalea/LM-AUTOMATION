'''
Created on 16.10.2012

@author: cbalea
'''
from cms.pages.base_page_cms import BasePageCMS
from selenium.webdriver.support.select import Select
from utils.server_related import ServerRelated



class FeatureWellsPageCMS(BasePageCMS):

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.driver.get(ServerRelated().serverToBeTested() + "/admin/station_site/featurewell/")

    def clickFeatureWellByIndex(self, index):
        self.clickItemInListTableByIndex(index)
        return EditFeatureWellPageCMS(self.driver, self.wait)
    
        


class EditFeatureWellPageCMS(BasePageCMS):
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.lmSite = Select(self.wait.until(lambda driver : driver.find_element_by_id("id_lmsite")))
        self.title = self.wait.until(lambda driver : driver.find_element_by_id("id_title"))
        self.items = self.wait.until(lambda driver : driver.find_elements_by_xpath("//select[contains(@id,'id_orderedfeaturewellitem_set')]/option[@selected='selected' and not(text()='---------')]"))
        self.comboboxForNewItem = Select(self.wait.until(lambda driver : driver.find_element_by_xpath("//select[contains(@id,'id_orderedfeaturewellitem_set')]/option[@selected='selected' and text()='---------']/.."))) 

    def getAttachedFeatureWellItems(self):
        itemsText = []
        for item in self.items:
            itemsText.append(item.text)
        return itemsText

    def selectNewItemByIndex(self, index):
        self.comboboxForNewItem.select_by_index(index)
    
    def clickSaveAndContinueEditingButton(self):
        self.clickSaveAndContinueEditing()
        return EditFeatureWellPageCMS(self.driver, self.wait)
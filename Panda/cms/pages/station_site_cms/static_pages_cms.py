'''
Created on 10.01.2013

@author: cbalea
'''
from cms.pages.base_page_cms import BasePageCMS
from selenium.webdriver.support.select import Select
from utils.server_related import ServerRelated


class StaticPagesCMS(BasePageCMS):
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.driver.get(ServerRelated().serverToBeTested() + "admin/station_site/staticpage/")

    def clickAddStaticPage(self):
        self.clickAddButton()
        return EditStaticPageCMS(self.driver, self.wait)
    

class EditStaticPageCMS(BasePageCMS):
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.title = self.wait.until(lambda driver : driver.find_element_by_id("id_title"))
        self.description = self.wait.until(lambda driver : driver.find_element_by_id("id_description"))
        self.placeholder = Select(self.wait.until(lambda driver : driver.find_element_by_id("id_placeholder")))
        
    
    def typeTitle(self, text):
        self.title.clear()
        self.title.send_keys(text)
    
    def typeContent(self, text):
        self.typeInTinymceEditor("id_content_ifr", text)

    def selectPlaceholder(self, option):
        self.placeholder.select_by_visible_text(option)
    
    def clickSaveAndContinueEditingButton(self):
        self.clickSaveAndContinueEditing()
        return EditStaticPageCMS(self.driver, self.wait)
    
    

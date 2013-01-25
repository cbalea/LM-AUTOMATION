'''
Created on 11.12.2012

@author: cbalea
'''
from cms.pages.base_page_cms import BasePageCMS
from selenium.webdriver.support.select import Select
from utils.server_related import ServerRelated

class StationModulesPageCMS(BasePageCMS):

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.driver.get(ServerRelated().serverToBeTested() + "/admin/station_site/stationmodule/")

    def clickAddStationModuleButton(self):
        self.clickAddButton()
        return EditAddStationModulePageCMS(self.driver, self.wait)
    


class EditAddStationModulePageCMS(BasePageCMS):
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.title = self.wait.until(lambda driver : driver.find_element_by_id("id_title"))
        self.todayLinkForStartDate = self.wait.until(lambda driver : driver.find_element_by_xpath("//label[text()='Start on:']/../span/a[text()='Today']"))
        self.todayLinkForEndDate = self.wait.until(lambda driver : driver.find_element_by_xpath("//label[text()='End on:']/../span/a[text()='Today']"))
        self.subheads= self.wait.until(lambda driver : driver.find_elements_by_xpath("//input[contains(@id, 'subhead')]"))
        self.links= self.wait.until(lambda driver : driver.find_elements_by_xpath("//input[contains(@id, 'link')]"))
    
    def selectLmSiteByVisibleText(self, text):
        lmSite = Select(self.wait.until(lambda driver : driver.find_element_by_id("id_lmsite")))
        lmSite.select_by_visible_text(text)
    
    def typeTitle(self, text):
        self.title.send_keys(text)
    
    def clickStartOnTodayLink(self):
        self.todayLinkForStartDate.click()
    
    def clickEndOnTodayLink(self):
        self.todayLinkForEndDate.click()
    
    def selectPlaceholderByVisibleText(self, text):
        placeholder = Select(self.wait.until(lambda driver : driver.find_element_by_id("id_placeholder")))
        placeholder.select_by_visible_text(text)
    
    def typeSubhead(self, promoIndex, text):
        self.subheads[promoIndex].clear()
        self.subheads[promoIndex].send_keys(text)
    
    def typeLink(self, promoIndex, text):
        self.links[promoIndex].send_keys(text)
    
    def typePromo(self, promoIndex, text):
        self.typeInTinymceEditor("id_promo_set-%s-promo_text_ifr" %promoIndex, text)
    
    def clickSaveAndContinueEditingButton(self):
        self.clickSaveAndContinueEditing()
        return EditAddStationModulePageCMS(self.driver, self.wait)
    
    def addImageInPromo(self, promoIndex, imageUrl):
        self.addImageInTinymceEditor("id_promo_set-%s-promo_text_image" %promoIndex, imageUrl)
        

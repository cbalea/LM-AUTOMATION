'''
Created on 08.10.2012

@author: cbalea
'''
from cms.pages.base_page_cms import BasePageCMS
from selenium.webdriver.support.select import Select
from utils.server_related import ServerRelated



class ContentFragmentsPageCMS(BasePageCMS):

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.driver.get(ServerRelated().serverToBeTested() + "/admin/station_site/contentfragment/")

    def clickAddContentFragment(self):
        self.clickAddButton()
        return EditContentFragmentPageCMS(self.driver, self.wait)
    
        


class EditContentFragmentPageCMS(BasePageCMS):
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.title = self.wait.until(lambda driver : driver.find_element_by_id("id_title"))
        self.startOnDate = self.wait.until(lambda driver : driver.find_element_by_id("id_start_on"))
    
    def placeholder(self):    
        return Select(self.wait.until(lambda driver : driver.find_element_by_id("id_placeholder")))
    
    def lmSite(self):
        return Select(self.wait.until(lambda driver : driver.find_element_by_id("id_lmsite")))
    
    def selectLmSite(self, site):
        self.lmSite().select_by_visible_text(site)
    
    def typeTitle(self, title):
        self.title.send_keys(title)
        
    def typeBody(self, bodyText):
        self.typeInTinymceEditor("id_body_ifr", bodyText)
    
    def selectStartOnTomorrow(self):
        self.startOnCalendar = self.wait.until(lambda driver : driver.find_element_by_xpath("//div[@class='form-row field-start_on']/div/span/a/img[@alt='Calendar']"))
        self.startOnCalendar.click()
        self.clickOnLink("Tomorrow")
        
    def selectPlaceholder(self, placeholder):
        self.placeholder().select_by_visible_text(placeholder)
    
    def clickSaveAndContinueEditingButton(self):
        self.clickSaveAndContinueEditing()
        return EditContentFragmentPageCMS(self.driver, self.wait)

    def getSelectedLmSite(self):
        return self.lmSite().first_selected_option.text
    
    def getTitle(self):
        return self.title.get_attribute("value")
    
    def getBody(self):
        return self.getContentOfTinymceEditor("id_body_ifr")
    
    def getStartOnDate(self):
        return self.startOnDate.get_attribute("value")

    def getSelectedPlaceholder(self):
        return self.placeholder().first_selected_option.text
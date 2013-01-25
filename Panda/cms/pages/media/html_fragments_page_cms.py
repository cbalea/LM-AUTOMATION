'''
Created on Nov 9, 2012

@author: jseichei
'''

from cms.pages.base_page_cms import BasePageCMS
from selenium.webdriver.support.select import Select
from utils.server_related import ServerRelated


class HtmlFragmentsPageCMS(object):
    
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.driver.get(ServerRelated().serverToBeTested() + "/admin/cms/htmlfragmentmedia/")
        
        
        
    def clickToAddHtmlFragmentsButton(self):
        self.addHtmlFragmentButton = self.wait.until(lambda driver : driver.find_element_by_xpath(".//*[@id='content-main']/ul/li/a"))
        self.addHtmlFragmentButton.click()
        return EditHtmlFragmentsPage(self.driver, self.wait)
    
    
    
class EditHtmlFragmentsPage(BasePageCMS):
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.htmlFragmentNameField = self.wait.until(lambda driver : driver.find_element_by_xpath(".//*[@id='id_name']"))
        self.htmlFragmentLanguageDropDownList = Select(self.wait.until(lambda driver : driver.find_element_by_xpath(".//*[@id='id_language']")))
        self.fragmentType = Select(self.wait.until(lambda driver : driver.find_element_by_id("id_fragment_type")))
    
    
    def typeInNameField(self, htmlFragmentText):
        self.htmlFragmentNameField.send_keys(htmlFragmentText)   
          
    def getHtmlFragmentName(self):
        return self.htmlFragmentNameField.get_attribute("value")
                                                                        
    def selectLanguage(self, language):
        self.htmlFragmentLanguageDropDownList.select_by_visible_text(language)
    
    def getSelectedLanguage(self):
        return self.htmlFragmentLanguageDropDownList.first_selected_option.text
    
    def typeInContentFields(self, text):
        self.typeInTinymceEditor("id_content_ifr", text)
    
    def getContentFieldsContext(self):
        return self.getContentOfTinymceEditor("id_content_ifr")

    def selectFragmentType(self, value):
        self.fragmentType.select_by_visible_text(value)
    
    def clickToHtmlFragmentSaveAndContinue(self):
        self.clickSaveAndContinueEditing()
        return EditHtmlFragmentsPage(self.driver, self.wait)
    
    
         
    
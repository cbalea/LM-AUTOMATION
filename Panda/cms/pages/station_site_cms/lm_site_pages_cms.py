'''
Created on 20.09.2012

@author: cbalea
'''
from cms.pages.base_page_cms import BasePageCMS



class LMSitesPageCMS(BasePageCMS):

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def clickAddLmSiteButton(self):
        self.clickAddButton()
        return EditAddLmSitePageCMS(self.driver, self.wait)
    
    def openLmSiteByIndex(self, index):
        lmSite = self.wait.until(lambda driver : driver.find_element_by_xpath("//table[@id='result_list']/tbody/tr[%d]/th/a" %index))
        lmSite.click()
        return EditAddLmSitePageCMS(self.driver, self.wait)
    
    def openLmSiteByName(self, name):
        self.clickOnLink(name)
        return EditAddLmSitePageCMS(self.driver, self.wait)


class EditAddLmSitePageCMS(BasePageCMS):
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.subdomain = self.wait.until(lambda driver : driver.find_element_by_id("id_subdomain"))
        self.defaultLmSiteCheckbox = self.wait.until(lambda driver : driver.find_element_by_id("id_default_lmsite"))
        self.name = self.wait.until(lambda driver : driver.find_element_by_id("id_name"))
        self.welcomeTextbox = self.wait.until(lambda driver : driver.find_element_by_id("id_welcome_text"))
        self.countySearch = self.wait.until(lambda driver : driver.find_element_by_id("lmsite_add_county"))
        self.perviewButton = self.wait.until(lambda driver : driver.find_element_by_id("preview_button"))
        self.headerImage = self.wait.until(lambda driver : driver.find_element_by_id("id_header_image"))
    
    def typeHeaderFilePath(self, filePath):
        self.headerImage.send_keys(filePath)
    
    def typeSubdomain(self, subdomain):
        self.subdomain.send_keys(subdomain)
        
    def typeName(self, name):
        self.name.send_keys(name)
    
    def typeWellcomeText(self, text):
        self.welcomeTextbox.clear()
        self.welcomeTextbox.send_keys(text)
    
    def typeInCountySearch(self, county):
        self.countySearch.clear()
        self.countySearch.send_keys(county)
    
    def selectFirstCountyFromSuggestions(self):
        self.suggestion = self.wait.until(lambda driver : driver.find_element_by_xpath("//a[@class='ui-corner-all']"))
        self.suggestion.click()
    
    def clickDefaultLmSiteCheckbox(self):
        if not self.isDefaultLmSiteChecked():
            self.defaultLmSiteCheckbox.click()
    
    def clickSaveAndContinueEditingButton(self):
        self.clickSaveAndContinueEditing()
        return EditAddLmSitePageCMS(self.driver, self.wait)

    def getName(self):
        return self.name.get_attribute("value")
    
    def getSubdomain(self):
        return self.subdomain.get_attribute("value")
    
    def isDefaultLmSiteChecked(self):
        return self.isCheckboxChecked(self.defaultLmSiteCheckbox)
    
    def getWellcomeText(self):
        return self.welcomeTextbox.text
    
    def clickPreviewButton(self):
        self.perviewButton.click()
    
    def getCurrentHeaderImage(self):
        self.currentHeaderImage = self.wait.until(lambda driver : driver.find_element_by_xpath("//div[@class='form-row field-header_image']/div/p/a"))
        return self.currentHeaderImage.text
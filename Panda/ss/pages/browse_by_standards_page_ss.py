'''
Created on 06.12.2012

@author: cbalea
'''
from selenium.webdriver.support.select import Select
from ss.pages.base_page_ss import BasePageSS
from utils.server_related import ServerRelated
import time


class BrowseByStandardsPageSS(BasePageSS):
    loadingImageXpath = "//div[@id='LoadingImage' and contains(@style,'display: block;')]"
    
    def __init__(self, driver, wait, standardId=None):
        self.driver = driver
        self.wait = wait
        if(standardId != None):
            self.driver.get(ServerRelated().serverToBeTested() + "/standards/" + standardId)
        self.pageTitle = self.wait.until(lambda driver : driver.find_element_by_xpath("//div[@class='pbscustom section-head']/h5"))
        self.typeOfStandards = Select(self.wait.until(lambda driver : driver.find_element_by_id("type_standards")))
        self.browseButton = self.wait.until(lambda driver : driver.find_element_by_xpath("//button[@id='browse']"))
        self.keyword = self.wait.until(lambda driver : driver.find_element_by_id("keyword"))
    
    def documentCombobox(self):
        return Select(self.wait.until(lambda driver:driver.find_element_by_id("documents")))

    def gradeCheckbox(self, grade):
        return self.wait.until(lambda driver:driver.find_element_by_xpath("//input[@type='checkbox' and @value='%s']" %grade))

    def displayedStandardSections(self):
        return self.wait.until(lambda driver:driver.find_elements_by_xpath("//div[@id='standards_list']/ul/div"))



    
    def getPageTitle(self):
        return self.pageTitle.text
    
    def selectTypeOfStandardsByIndex(self, index):
        self.typeOfStandards.select_by_index(index)
    
    def selectDocumentByIndex(self, index):
        self.documentCombobox().select_by_index(index)

    def getNumberOfSelectableDocuments(self):
        time.sleep(5)
        options = self.wait.until(lambda driver:driver.find_elements_by_xpath("//select[@id='documents']/option"))
        return len(options)-1

    def checkGradeCheckbox(self, grade):
        if(self.isCheckboxChecked(self.gradeCheckbox(grade))==False):
            self.gradeCheckbox(grade).click()
    
    def clickBrowseButton(self):
        self.browseButton.click()
        
    def waitForResultsToLoad(self):
        timeout = 30
        while(self.elementExistsByXpath(self.loadingImageXpath)):
            timeout = timeout-3
        if(timeout<=0):
            raise Exception("Results not loaded in timeout interval.")

    def getNumberOfDisplayedStandardsSections(self):
        return len(self.displayedStandardSections())         
    
    def typeKeyword(self, word):
        self.keyword.clear()
        self.keyword.send_keys(word)
    
    def getNumberOfStandardsForStatement(self, statement):
        number =  self.wait.until(lambda driver:
                            driver.find_element_by_xpath("//div[contains(text(), '%s')]/../div[contains(@style, 'right;')]" %statement))
        return int(number.text) 
        
    
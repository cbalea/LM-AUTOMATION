'''
Created on 29.11.2012

@author: cbalea
'''
from ss.pages.base_page_ss import BasePageSS
from utils.base_page import BasePage
from utils.server_related import ServerRelated
import time


class SelfPacedLessons(BasePageSS):
    
    def __init__(self, driver, wait, resourceId=None):
        self.driver = driver
        self.wait = wait
        self.driver.get(ServerRelated().serverToBeTested() + "/resource/" + resourceId)
        self.title = self.wait.until(lambda driver : driver.find_element_by_xpath("//div[@class='title']/h2"))
#        self.driver.execute_script("window.SPLOverlay = new PBSLM.Overlay($('#activity_lightbox'));")
        self.clickOnLink("Display SPL")
        self.splFrame = self.wait.until(lambda driver : driver.find_element_by_xpath("//div[@id='activity_lightbox' and not(contains(@style, 'display: none'))]"))
        self.splTitle = self.wait.until(lambda driver : driver.find_element_by_xpath("//div[@id='spl_top_banner']/h1"))
        self.creditsLink = self.wait.until(lambda driver : driver.find_element_by_id("spl_credits_trigger"))
        self.closeButton = self.wait.until(lambda driver : driver.find_element_by_xpath("//div[@class='close']"))
        self.pageButtons = self.wait.until(lambda driver : driver.find_elements_by_xpath("//div[@id='buttons']/a"))
        self.nextButton = self.wait.until(lambda driver : driver.find_element_by_id("spl_next_link"))

    
    def getSplTitle(self):
        return self.splTitle.text
        
    def clickReviewMyWork(self):
        self.clickOnLink("review my work")
    
    def clickNext(self):
        self.nextButton.click()
    
    def getSectionTitle(self):
        secTitle = self.wait.until(lambda driver : driver.find_element_by_xpath("//div[@style='display: block;']/h1/span[contains(@id,'sec_title')]"))
        return secTitle.text
    
    def clickBack(self):
        backButton = self.wait.until(lambda driver : driver.find_element_by_id("spl_back_link"))
        backButton.click()
    
    def clickFinalAssignment(self):
        self.clickOnLink("FINAL ASSIGNMENT")
    
    def clickCredits(self):
        self.clickOnLink("credits")
    
    def clickBackToLesson(self):
        self.clickOnLink("back to lesson")
    
    def clickPage(self, index):
        self.pageButtons[index-1].click()
    
    def getTooltipDefinition(self):
        definition = self.wait.until(lambda driver : driver.find_element_by_xpath("//div[@class='gl_tooltip_definition']/p"))
        return definition.text
    
    def clickWordToOpenDefinition(self, word):
        link = self.wait.until(lambda driver : driver.find_element_by_xpath("//li/a[text()='%s']" %word))
        link.click()

    def isSplFrameDisplayed(self):
        return self.elementExistsByXpath("//div[@id='activity_lightbox' and not(contains(@style,'display: none;'))]")
    
    def clickViewButton(self):
        viewButton = self.wait.until(lambda driver : driver.find_element_by_xpath("//div[@class='sa_section' and @style='display: block;']/div/div/div/button[text()='View']"))
        viewButton.click()
        time.sleep(2)
        self.switchToNewestWindow()
        return BasePage(self.driver, self.wait)
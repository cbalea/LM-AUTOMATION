'''
Created on 11.01.2013

@author: cbalea
'''
from ss.pages.base_page_ss import BasePageSS
from utils.server_related import ServerRelated

class HelpPageSS(BasePageSS):
    
    footer_xpath = "//div[@id='footer_display']/section/div/p"
    
    def __init__(self, driver, wait, noReload = None):
        self.driver = driver
        self.wait = wait
        if(noReload==None):
            self.driver.get(ServerRelated().serverToBeTested() + "help")
    
    def clickTopic(self, topicLink):
        self.clickOnLink(topicLink)
        return HelpPageSS(self.driver, self.wait, "noReload")
    
    def getPageTitle(self):
        title = self.wait.until(lambda driver : driver.find_element_by_xpath("//div[@id='topic_display']/section/div/h3"))
        return title.text
    
    def getPageContent(self):
        content = self.wait.until(lambda driver : driver.find_element_by_xpath("//div[@id='topic_display']/section/div/p"))
        return content.text
    
    def getFooterContent(self):
        footerContent = self.wait.until(lambda driver : driver.find_element_by_xpath(self.footer_xpath))
        return footerContent.text
    
    def footerExists(self):
        return self.elementExistsByXpath(self.footer_xpath)
    
    
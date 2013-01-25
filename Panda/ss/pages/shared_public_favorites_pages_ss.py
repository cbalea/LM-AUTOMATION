'''
Created on 09.01.2013

@author: cbalea
'''
from ss.pages.base_page_ss import BasePageSS
from utils.server_related import ServerRelated

class SharedPublicFavoritesPages(BasePageSS):
    
    def __init__(self, driver, wait, username=None, folder=None):
        self.driver = driver
        self.wait = wait
        if(username!=None and folder!=None):
            self.driver.get(ServerRelated().serverToBeTested() + "/shared/%s/%s" %(username, folder))
        self.folderTitle = self.wait.until(lambda driver : driver.find_element_by_xpath("//div[@class='folder-description']/h3"))
    
    def openSubfolder(self, subfolderName):
        self.clickOnLink(subfolderName)
        return SharedPublicFavoritesPages(self.driver, self.wait)
    
    def getFolderTitle(self):
        return self.folderTitle.text
    
    def getSubfolderTitle(self):
        subfolderTitle = self.wait.until(lambda driver : driver.find_element_by_xpath("//div[@class='subfolder-description']/h3"))
        return str(subfolderTitle.text)
    
    def getSubfolderDescription(self):
        subfolderDescr = self.wait.until(lambda driver : driver.find_element_by_xpath("//div[@class='subfolder-description']/p"))
        return str(subfolderDescr.text)
    
    def getNumberOfFavoritesInFolder(self):
        favsInFolder = self.wait.until(lambda driver : driver.find_elements_by_xpath("//li[@class='favorite']"))
        return len(favsInFolder)
    
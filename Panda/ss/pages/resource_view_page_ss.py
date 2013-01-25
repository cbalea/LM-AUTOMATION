'''
Created on 07.11.2012

@author: cbalea
'''
from ss.pages.base_page_ss import BasePageSS
from utils.server_related import ServerRelated

class ResourceViewPageSS(BasePageSS):
    
    def __init__(self, driver, wait, resourceId=None):
        self.driver = driver
        self.wait = wait
        if resourceId != None:
            self.driver.get(ServerRelated().serverToBeTested() + "/resource/" + resourceId)
        self.title = self.wait.until(lambda driver : driver.find_element_by_xpath("//div[@class='title']/h2"))
        self.grades = self.wait.until(lambda driver : driver.find_element_by_xpath("//div[@class='grade']"))
        
    def favStar(self):
        return self.wait.until(lambda driver : driver.find_element_by_xpath("//span[@class='favorites']/i"))
    
    def getTitle(self):
        return self.title.text
    
    def getGrades(self):
        return self.grades.text
    
    def clickSupportMaterials(self):
        self.clickOnLink("Support Materials")
    
    def clickStandards(self):
        self.clickOnLink("Standards")
        
    def clickComments(self):
        self.clickOnLink("Comments")
    
    def clickLearningObjective(self):
        self.clickOnLink("Learning Objective")
    
    def clickMaterial(self, index):
        suppMat = self.wait.until(lambda driver : driver.find_elements_by_xpath("//div[@title='Support Materials']/section/div"))
        suppMat[index].click()
    
    def getSupportMaterialContent(self, index):
        self.clickSupportMaterials() 
        self.clickMaterial(index)
        material = self.wait.until(lambda driver : driver.find_element_by_xpath("//div[@title='Support Materials']/section/div[contains(@style,'display: block;')]"))
        return material.text
    
    def getNumberOfStandards(self):
        self.clickStandards()
        standards = self.wait.until(lambda driver : driver.find_elements_by_xpath("//div[contains(@class,'active')]/div/ol/li"))
        return len(standards)
    
    def getContentOfLearningObjective(self):
        self.clickLearningObjective()
        learningObjective = self.wait.until(lambda driver : driver.find_element_by_xpath("//div[@class='tab-content pbscustom srp']/div[contains(@class,'active')]/div"))
        return learningObjective.text
    
    def getNumberOfRelatedResources(self):
        relatedResources = self.wait.until(lambda driver : driver.find_elements_by_xpath("//h5[text()='Related Resources']/../../div[contains(@class, 'is-open')]/ul/li/a"))
        return len(relatedResources)
    
    def clickFavoriteStar(self):
        self.favStar().click()
    
    def isFavorited(self):
        return self.isFavoritedStarClicked(self.favStar())
    
    def clickInterractiveAsset(self):
        interractiveAsset = self.wait.until(lambda driver : driver.find_element_by_xpath("//section[@id='player-section']/div/a[@class='popup']"))
        interractiveAsset.click()
        self.switchToNewestWindow()
        return BasePageSS(self.driver, self.wait)
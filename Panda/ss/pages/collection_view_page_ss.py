'''
Created on 07.11.2012

@author: cbalea
'''
from ss.pages.base_page_ss import BasePageSS
from ss.pages.resource_view_page_ss import ResourceViewPageSS
from utils.server_related import ServerRelated

class CollectionViewPageSS(BasePageSS):
    
    def __init__(self, driver, wait, collectionCode=None):
        self.driver = driver
        self.wait = wait
        if(collectionCode!=None):
            self.driver.get(ServerRelated().serverToBeTested() + "/collection/%s" %collectionCode )
        self.banner = self.wait.until(lambda driver : driver.find_element_by_xpath("//div[@class='pbscustom collection-header']/img"))
        self.credits = self.wait.until(lambda driver : driver.find_element_by_xpath("//div[@class='leftcolumn']/section[1]/section/div/p[text()!='']"))
        self.description = self.wait.until(lambda driver : driver.find_element_by_xpath("//div[@class='maincolumn']/section/section/div/p[text()!='']"))
        self.resourceLinks = self.wait.until(lambda driver : driver.find_elements_by_xpath("//div[@class='pbscustom multiresource-single-item-content']/a"))
    
    def getCredits(self):
        return self.credits.text
    
    def getDescription(self):
        return self.description.text
    
    def getBannerImage(self):
        return self.banner.get_attribute("src")
    
    def clickFavoriteStar(self):
        self.favStar.click()
    
    def isFavorited(self):
        return self.isFavoritedStarClicked(self.favStar)
    
    def getNumberOfResources(self):
        return len(self.resourceLinks)
    
    def getResourceName(self, index):
        return self.resourceLinks[index].text

    def clickResource(self, index):
        self.resourceLinks[index].click()
        return ResourceViewPageSS(self.driver, self.wait)
    

'''
Created on Oct 19, 2012

@author: jseichei
'''



from utils.base_page import BasePage



class BasePageSS(BasePage):
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
    
    
    def isFavoritedStarClicked(self, favStar):
        status = favStar.get_attribute("class")
        print "status = [%s]" %status
        if(status == 'icon-star'):
            return True
        if(status == 'icon-star-empty'):
            return False
    
    def searchByKeyword(self, keyword):
        searchbox = self.wait.until(lambda driver : driver.find_element_by_xpath("//form[@id='main_search']/input"))
        searchbox.send_keys(keyword)
        searchbox.submit()

    def get_number_of_resource_views_left_before_neeting_to_login(self):
        number = self.wait.until(lambda driver : driver.find_element_by_xpath("//div[@class='lm-alert-box']/p/strong"))
        return int(number.text)
    
    def isHeaderImageDisplayed(self):
        headerImage = self.wait.until(lambda driver : driver.find_element_by_xpath("//img[@alt='Header Image']"))
        return headerImage.is_displayed()
    
    def clickLinkOnPageByIndex(self, index):
        link = self.wait.until(lambda driver : driver.find_element_by_xpath("//a[%d]" %index))
        link.click()
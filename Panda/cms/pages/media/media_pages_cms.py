'''
Created on 20.09.2012

@author: cbalea
'''
from cms.pages.base_page_cms import BasePageCMS
from selenium.webdriver.support.select import Select
from utils.server_related import ServerRelated

class MediasPageCMS(BasePageCMS):

    def __init__(self, driver, wait, noFreshLoad = None):
        self.driver = driver
        self.wait = wait
        if (noFreshLoad == None):
            self.driver.get(ServerRelated().serverToBeTested() + "/admin/cms/media/")
        
    def clickAddMediaButton(self):
        self.clickAddButton()
        return EditAddMediaPageCMS(self.driver, self.wait)

    def clickMedia(self, link):
        self.clickLastPageInPaginatorIfExists()
        self.clickOnLink(link)
        return EditAddMediaPageCMS(self.driver, self.wait)
    
    def clickAddMediaToAssetButton(self):
        addMediaToAssetButton = self.wait.until(lambda driver:driver.find_element_by_id("asset_add_media"))
        addMediaToAssetButton.click()
    
    
    
class EditAddMediaPageCMS(BasePageCMS):

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.nameField = self.wait.until(lambda driver : driver.find_element_by_id("id_name"))
        self.contentProject = Select(self.wait.until(lambda driver : driver.find_element_by_id("id_content_project")))
        self.file = self.wait.until(lambda driver : driver.find_element_by_id("id_file"))
        
        
    def getName(self):
        return self.nameField.get_attribute("value")
    
    def getSelectedContentProject(self):
        return self.contentProject.first_selected_option.text
    
    def typeName(self, name):
        self.nameField.clear()
        self.nameField.send_keys(name)
    
    def typeFilePath(self, filePath):
        self.file.send_keys(filePath)
    
    def selectContentProjectByVisibleText(self, text):
        self.contentProject.select_by_visible_text(text)
        
    def selectContentProjectByIndex(self, index):
        self.contentProject.select_by_index(index)
    
    def clickSaveButton(self):
        self.clickSave()
        return MediasPageCMS(self.driver, self.wait)
    
    def getCurrentMediaFile(self):
        self.currentMediaFile = self.wait.until(lambda driver : driver.find_element_by_xpath("//div[@class='form-row file']/div/a"))
        return self.currentMediaFile.text
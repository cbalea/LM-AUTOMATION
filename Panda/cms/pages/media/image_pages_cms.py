'''
Created on 20.09.2012

@author: cbalea
'''
from utils.server_related import ServerRelated
from cms.pages.base_page_cms import BasePageCMS


class ImagesPageCMS(BasePageCMS):

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.driver.get(ServerRelated().serverToBeTested() + "/admin/cms/imagemedia/")
        
    def clickOnImage(self, imageName):
        self.clickLastPageInPaginatorIfExists()
        self.clickOnLink(imageName)
        return EditAddImagePageCMS(self.driver, self.wait)
    
    def clickAddImageButton(self):
        self.clickAddButton()
        return EditAddImagePageCMS(self.driver, self.wait)
    
    def openFirstImageOlderThanYesterday(self):
        self.selectFromTableFirstItemOlderThanYesterday()
        return EditAddImagePageCMS(self.driver, self.wait)
    




class EditAddImagePageCMS(BasePageCMS):

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.metaSize = self.wait.until(lambda driver : driver.find_element_by_id("id_size"))
        self.nameField = self.wait.until(lambda driver : driver.find_element_by_id("id_name"))
        self.imageFile = self.wait.until(lambda driver : driver.find_element_by_id("id_image_file"))
        self.metaWidth = self.wait.until(lambda driver : driver.find_element_by_id("id_width"))
        self.metaHeight = self.wait.until(lambda driver : driver.find_element_by_id("id_height"))
        
    def typeName(self, name):
        self.nameField.clear()
        self.nameField.send_keys(name)
    
    def typeImageFilePath(self, imageFilePath):
        self.imageFile.send_keys(imageFilePath)
    
    def typeWidth(self, width):
        self.metaWidth.clear()
        self.metaWidth.send_keys(width)
        
    def typeHeight(self, height):
        self.metaHeight.clear()
        self.metaHeight.send_keys(height)
    
    def typeCaptions(self, caption):
        self.typeInTinymceEditor("id_captions_ifr", caption)
    
    def getName(self):
        return self.nameField.get_attribute("value")
    
    def getCurrentImageFile(self):
        self.currentImageFile = self.wait.until(lambda driver : driver.find_element_by_xpath("//div[@class='form-row image_file']/div/a"))
        return self.currentImageFile.text
    
    def getMetaSize(self):
        return self.metaSize.get_attribute("value")

    def getMetaWidth(self):
        return self.metaWidth.get_attribute("value")

    def getMetaHeight(self):
        return self.metaHeight.get_attribute("value")

    def getCaption(self):
        return self.getContentOfTinymceEditor("id_captions_ifr")
    
    def clickSaveAndContinueEditingButton(self):
        self.clickSaveAndContinueEditing()
        return EditAddImagePageCMS(self.driver, self.wait)
    

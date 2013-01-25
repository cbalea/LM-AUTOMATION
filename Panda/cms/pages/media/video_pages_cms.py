'''
Created on 20.09.2012

@author: cbalea
'''
from cms.pages.base_page_cms import BasePageCMS
from selenium.webdriver.support.select import Select
from utils.server_related import ServerRelated


class VideosPageCMS(BasePageCMS):

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.driver.get(ServerRelated().serverToBeTested() + "/admin/cms/videomedia/")
        
    def clickAddVideoButton(self):
        self.clickAddButton()
        return EditAddVideoPageCMS(self.driver, self.wait)
    
    def clickOnVideo(self, videoName):
        self.clickLastPageInPaginatorIfExists()
        self.clickOnLink(videoName)
        return EditAddVideoPageCMS(self.driver, self.wait)

    def openFirstVideoOlderThanYesterday(self):
        self.selectFromTableFirstItemOlderThanYesterday()
        return EditAddVideoPageCMS(self.driver, self.wait)

    

class EditAddVideoPageCMS(BasePageCMS):

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.size = self.wait.until(lambda driver : driver.find_element_by_id("id_size"))
        self.nameField = self.wait.until(lambda driver : driver.find_element_by_id("id_name"))
        self.contentProject = Select(self.wait.until(lambda driver : driver.find_element_by_id("id_content_project")))
        self.videoFile = self.wait.until(lambda driver : driver.find_element_by_id("id_video_file"))
        self.language = Select(self.wait.until(lambda driver : driver.find_element_by_id("id_language")))
        self.metaWidth = self.wait.until(lambda driver : driver.find_element_by_id("id_width"))
        self.metaHeight = self.wait.until(lambda driver : driver.find_element_by_id("id_height"))
        self.aspectRatio = self.wait.until(lambda driver : driver.find_element_by_id("id_aspect_ratio"))
        self.isExternal = self.wait.until(lambda driver : driver.find_element_by_id("id_is_external"))
        self.saveButtonInHeader = self.wait.until(lambda driver : driver.find_element_by_xpath("//div[@class='submit-row']/input"))
        
    def getCurrentVideoFile(self):
        self.currentVideoFile = self.wait.until(lambda driver : driver.find_element_by_xpath("//div[@class='form-row video_file']/div/a"))
        return self.currentVideoFile.text
    
    def getCurrentCaptionFile(self):
        self.currentCaptionFile = self.wait.until(lambda driver : driver.find_element_by_xpath("//div[@class='form-row caption']/div/p/a"))
        return self.currentCaptionFile.text
    
    def getCurrentTranscriptFile(self):
        self.currentTranscriptFile = self.wait.until(lambda driver : driver.find_element_by_xpath("//div[@class='form-row transcript_path']/div/div/a"))
        return self.currentTranscriptFile.text
    
    def getName(self):
        return self.nameField.get_attribute("value")
    
    def getSelectedContentProject(self):
        return self.contentProject.first_selected_option.text
    
    def getSelectedLanguage(self):
        return self.language.first_selected_option.text
    
    def getWidth(self):
        return self.metaWidth.get_attribute("value")
    
    def getHeight(self):
        return self.metaHeight.get_attribute("value")
    
    def getSize(self):
        return self.size.get_attribute("value")
    
    def getAspectRatio(self):
        return self.aspectRatio.get_attribute("value")
    
    def getEmbeddedCode(self):
        return self.getContentOfTinymceEditor("id_embed_code_ifr")
    
    def isExternalChecked(self):
        return self.isCheckboxChecked(self.isExternal)
    
    def clickSaveButtonInHeader(self):
        self.saveButtonInHeader.click()
        return EditAddVideoPageCMS(self.driver, self.wait)
    
    def clickSaveAndContinueEditingButton(self):
        self.clickSaveAndContinueEditing()
        return EditAddVideoPageCMS(self.driver, self.wait)
    
    def typeCaptionFilePath(self, captionFilePath):
        self.captionFile = self.wait.until(lambda driver : driver.find_element_by_id("id_caption"))
        self.captionFile.send_keys(captionFilePath)

    def typeName(self, name):
        self.nameField.clear()
        self.nameField.send_keys(name)
    
    def typeVideoFilePath(self, videoFilePath):
        self.videoFile.send_keys(videoFilePath)
    
    def typeTranscriptFilePath(self, transcriptFilePath):
        self.transcriptFile = self.wait.until(lambda driver : driver.find_element_by_id("id_transcript_path"))
        self.transcriptFile.send_keys(transcriptFilePath)

    def typeEmbedCode(self, code):    
        self.typeInTinymceEditor("id_embed_code_ifr", code)
            
    def typeWidth(self, width):
        self.metaWidth.clear()
        self.metaWidth.send_keys(width)
    
    def typeHeight(self, height):
        self.metaHeight.clear()
        self.metaHeight.send_keys(height)
    
    def clickIsExternal(self):
        self.isExternal.click()
    
    def typeTranscriptText(self, text):
        self.typeInTinymceEditor("id_transcript_text_ifr", text)   
        
    def getTranscriptText(self):
        return self.getContentOfTinymceEditor("id_transcript_text_ifr")
    
    def selectLanguageByVisibleText(self, text):
        self.language.select_by_visible_text(text)
    
    def typeAspectRatio(self, ratio):
        self.aspectRatio.clear()
        self.aspectRatio.send_keys(ratio)
    
    def selectContentProjectByIndex(self, index):
        self.contentProject.select_by_index(index)
'''
Created on 20.09.2012

@author: cbalea
'''
from cms.pages.base_page_cms import BasePageCMS
from selenium.webdriver.support.select import Select
from utils.server_related import ServerRelated

class AudiosPageCMS(BasePageCMS):

    def __init__(self, driver, wait, noReload=None):
        self.driver = driver
        self.wait = wait
        if (noReload == None):
            self.driver.get(ServerRelated().serverToBeTested() + "/admin/cms/audiomedia/")
        
    def clickOnAudio(self, audioName):
        self.clickLastPageInPaginatorIfExists()
        self.clickOnLink(audioName)
        return EditAddAudioPageCMS(self.driver, self.wait)
    
    def clickAddAudioButton(self):
        self.clickAddButton()
        return EditAddAudioPageCMS(self.driver, self.wait)
    


class EditAddAudioPageCMS(BasePageCMS):

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.nameField = self.wait.until(lambda driver : driver.find_element_by_id("id_name"))
        self.contentProject = Select(self.wait.until(lambda driver : driver.find_element_by_id("id_content_project")))
        self.audioFile = self.wait.until(lambda driver : driver.find_element_by_id("id_audio_file"))
        self.isExternal = self.wait.until(lambda driver : driver.find_element_by_id("id_is_external"))
        self.embedCodeField = self.wait.until(lambda driver : driver.find_element_by_id("id_embed_code"))
        self.language = Select(self.wait.until(lambda driver : driver.find_element_by_id("id_language")))
        self.size = self.wait.until(lambda driver : driver.find_element_by_id("id_size"))
        self.duration = self.wait.until(lambda driver : driver.find_element_by_id("id_duration"))
        
        
    def selectLanguageByVisibleText(self, text):
        self.language.select_by_visible_text(text)
    
    def getName(self):
        return self.nameField.get_attribute("value")
    
    def getSelectedContentProject(self):
        return self.contentProject.first_selected_option.text
    
    def getCurrentAudioFile(self):
        self.currentAudioFile = self.wait.until(lambda driver : driver.find_element_by_xpath("//div[@class='form-row audio_file']/div/a"))
        return self.currentAudioFile.text
    
    def getSelectedLanguage(self):
        return self.language.first_selected_option.text
    
    def getEmbeddedCode(self):
        return self.getContentOfTinymceEditor("id_embed_code_ifr")
    
    def getSize(self):
        return self.size.get_attribute("value")

    def isExternalChecked(self):
        return self.isCheckboxChecked(self.isExternal)
    
    def getCurrentTranscriptFile(self):
        self.currentTranscriptFile = self.wait.until(lambda driver : driver.find_element_by_xpath("//div[@class='form-row transcript_path']/div/div/a"))
        return self.currentTranscriptFile.text
    
    def getTranscriptText(self):
        return self.getContentOfTinymceEditor("id_transcript_text_ifr")
    
    def typeName(self, name):
        self.nameField.clear()
        self.nameField.send_keys(name)
    
    def typeAudioFilePath(self, audioFilePath):
        self.audioFile.send_keys(audioFilePath)
    
    def typeEmbedCode(self, code):
        self.typeInTinymceEditor("id_embed_code_ifr", code)
    
    def selectContentProjectByVisibleText(self, text):
        self.contentProject.select_by_visible_text(text)

    def selectContentProjectByIndex(self, index):
        self.contentProject.select_by_index(index)
    
    def clickIsExternal(self):
        self.isExternal.click()
    
    def typeTranscriptFilePath(self, transcriptFilePath):
        self.transcriptFile = self.wait.until(lambda driver : driver.find_element_by_id("id_transcript_path"))
        self.transcriptFile.send_keys(transcriptFilePath)
    
    def typeTranscriptText(self, text):
        self.typeInTinymceEditor("id_transcript_text_ifr", text)   
    
    def clickSaveAndContinueEditingButton(self):
        self.clickSaveAndContinueEditing()
        return EditAddAudioPageCMS(self.driver, self.wait)
    
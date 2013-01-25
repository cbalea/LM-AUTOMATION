'''
Created on Oct 24, 2012

@author: jseichei
'''
from cms.pages.base_page_cms import BasePageCMS
from selenium.webdriver.support.select import Select
from utils.server_related import ServerRelated


class DocumentMediaPageCMS(object):
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.driver.get(ServerRelated().serverToBeTested() + "/admin/cms/documentmedia/")
        
    
    def clickToAddDocumentMediaButton(self):
        self.addDocumentMediaButton = self.wait.until(lambda driver : driver.find_element_by_xpath(".//*[@id='content-main']/ul/li/a"))
        self.addDocumentMediaButton.click()
        return EditDocumentMediaPage(self.driver, self.wait)
    
    
class EditDocumentMediaPage(BasePageCMS):    
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.nameFieldDocument = self.wait.until(lambda driver : driver.find_element_by_id("id_name"))
        self.documentFileField = self.wait.until(lambda driver : driver.find_element_by_xpath(".//*[@id='id_document_file']"))
        self.languageDocumentField = self.wait.until(lambda driver : driver.find_element_by_id("id_language"))
        self.sizeDocumentField = self.wait.until(lambda driver : driver.find_element_by_id("id_size"))
        
    
    def typeInDocumentNameField(self, documentText):
        self.nameFieldDocument.clear()
        self.nameFieldDocument.send_keys(documentText)
        
        
    def addDocumentFilePath(self, documentPath):
        self.documentFileField.send_keys(documentPath)
        
    
    def selectLanguage(self, language):
        Select(self.languageDocumentField).select_by_visible_text(language)
        
              
    def typeInSize(self, size):
        self.sizeDocumentField.clear()
        self.sizeDocumentField.send_keys(size)
        
    
    def clickToSaveAndContinue(self):
        self.clickSaveAndContinueEditing()
        return EditDocumentMediaPage(self.driver, self.wait)
        
            
    def getDocumentName(self):
        return self.nameFieldDocument.get_attribute('value')    
    
    
    def getDocumentFile(self):
        self.currentDocumentFile = self.wait.until(lambda driver : driver.find_element_by_xpath("//div[@class='form-row document_file']/div/a"))  
        print self.currentDocumentFile.text
        return self.currentDocumentFile.text 
        
        
        
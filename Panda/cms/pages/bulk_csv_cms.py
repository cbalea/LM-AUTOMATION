'''
Created on 26.11.2012

@author: cbalea
'''
from cms.pages.base_page_cms import BasePageCMS
from selenium.webdriver.support.select import Select
from utils.server_related import ServerRelated

class BulkCSVsPage(BasePageCMS):
     
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.driver.get (ServerRelated().serverToBeTested() + "admin/bulk_upload/bulkcsv/")
    
    def clickAddBulkCSVFile(self):
        self.clickAddButton()
        return EditBulkCSVFile(self.driver, self.wait)
    
    def openCsvFile(self, linkFragment):
        elementLink = self.wait.until(lambda driver : driver.find_element_by_xpath("//a[contains(text(), '%s')]" %linkFragment))
        elementLink.click()
        return EditBulkCSVFile(self.driver, self.wait)
    
    def filterCsvFileFailedValidation(self):
        self.clickOnLink("CSV File Failed Validation")
        return BasePageCMS(self.driver, self.wait)


class EditBulkCSVFile(BasePageCMS):

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.contentProject = Select(self.wait.until(lambda driver : driver.find_element_by_id("id_content_project")))
        self.sourceFile = self.wait.until(lambda driver : driver.find_element_by_id("id_file"))
        self.uploadStatus = self.wait.until(lambda driver : driver.find_element_by_xpath("//div/label[text()='Bulk upload status:']/../p"))
    
    def selectContentProjectByIndex(self, index):
        self.contentProject.select_by_index(index)
        
    def typeSourceFile(self, filePath):
        self.sourceFile.send_keys(filePath)
    
    def clickSaveAndContinueEditingButton(self):
        self.clickSaveAndContinueEditing()
        return EditBulkCSVFile(self.driver, self.wait)
    
    def clickImportItButton(self):
        self.clickOnLink("Import it")
        return EditBulkCSVFile(self.driver, self.wait)
    
    def getContentProject(self):
        return self.contentProject.first_selected_option.text
    
    def getCurrentSourceFile(self):
        currentFile = self.wait.until(lambda driver : driver.find_element_by_xpath("//div/label[text()='Source file:']/../p/a"))
        return currentFile.text
    
    def getUploadStatus(self):
        return self.uploadStatus.text
    
    
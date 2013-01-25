'''
Created on 28.09.2012

@author: cbalea
'''
from cms.pages.delete_page_cms import DeletePageCMS
from datetime import datetime, timedelta
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from utils.base_page import BasePage

class BasePageCMS(BasePage):
    
    rightSidePaneXpath = "//div[@id='right_side_split']"
    
    
    def clickSaveAndContinueEditing(self):
        self.saveAndContinueEditingButton = self.wait.until(lambda driver : driver.find_element_by_xpath("//input[@value='Save and continue editing']"))
        self.saveAndContinueEditingButton.click()

    def clickAddButton(self):
        self.addButton = self.wait.until(lambda driver : driver.find_element_by_class_name("addlink"))
        self.addButton.click()        
        
    def clickSave(self):
        self.saveButton = self.wait.until(lambda driver : driver.find_element_by_xpath("//input[@value='Save']"))
        self.saveButton.click()
    
    def getContentOfTinymceEditor(self, iframe):
        self.wait.until(lambda driver : driver.find_element_by_xpath("//iframe[@id='%s']" %iframe))
        self.driver.switch_to_frame(iframe)
        self.tinymceEditor = self.driver.switch_to_active_element()
        self.tinymceEditor.click()
        text = self.tinymceEditor.text
        self.switchToNewestWindow()
        return text

    def addImageInTinymceEditor(self, addImageButtonId, imageUrl):
        addImageButton = self.wait.until(lambda driver : driver.find_element_by_id(addImageButtonId))
        addImageButton.click()
        self.switchToNewestWindow()
        imageUrlField = self.wait.until(lambda driver : driver.find_element_by_id("src"))
        imageUrlField.clear()
        imageUrlField.send_keys(imageUrl)
        imageUrlField.submit()
        self.waitUntilPopupCloses()
        self.switchToNewestWindow()
    
    def getContentOfStatusBox(self):
        self.allDatesAndStatus = self.wait.until(lambda driver : driver.find_element_by_xpath(self.rightSidePaneXpath))
        return self.allDatesAndStatus.text
    
    def clickShowTranscriptsLink(self):
        self.showTranscriptsLink = self.wait.until(lambda driver : driver.find_element_by_xpath("//h2[text()='Transcript']/a"))
        self.showTranscriptsLink.click()
    
    def clickShowCaptionsLink(self):
        self.showCaptionsLink = self.wait.until(lambda driver : driver.find_element_by_xpath("//h2[text()='Caption']/a"))
        self.showCaptionsLink.click()
    
    def clickAddTextButton(self):
        self.clickOnLink("Add text")
    
    def clickShowAllLinkIfExists(self):
        self.showAllLink = self.elementExistsByLinkText("Show all")
        if (self.showAllLink):
            self.showAllLink.click()
    
    def clickCheckboxForItem(self, item, noSearch=None):
        if(noSearch==None):
            self.search_in_searchbar(item)
        element1 = self.elementsExistByXpath("//tr/th/a[contains(text(),'%s')]/../../td/input[@type='checkbox']" %item)
        element2 = self.elementsExistByXpath("//td[contains(text(),'%s')]/../td/input[@type='checkbox']" %item)
        element3 = self.elementsExistByXpath("//tr/td/a[contains(text(),'%s')]/../../td/input" %item)
        if(element1 != False):
            checkboxes = element1
        elif(element2 != False):
            checkboxes = element2
        elif(element3 != False):
            checkboxes = element3
        else:
            raise Exception("No checkbox found for the element!")
        for checkbox in checkboxes:
            checkbox.click()
    
    def getFromTableTheNameOfItemThatContainsText(self, text):
        name_field = self.wait.until(lambda driver:driver.find_element_by_xpath("//tr/td[contains(text(),'%s')]/../th/a" %text))
        return name_field.text
        
    def clickCheckboxByIndex(self, index):
        self.clickShowAllLinkIfExists()
        checkbox = self.wait.until(lambda driver:driver.find_element_by_xpath("//tr[%d]/td[@class='action-checkbox']/input" %index))
        checkbox.click()
    
    def selectDeleteAction(self):
        try:
            action = Select(WebDriverWait(self.driver, 5).until(lambda driver:driver.find_element_by_name("action")))
        except: 
            action = Select(WebDriverWait(self.driver, 5).until(lambda driver:driver.find_element_by_name("user_action_select")))
        action.select_by_index(1)
        goButton = self.wait.until(lambda driver:driver.find_element_by_xpath("//button[text()='Go']"))
        goButton.submit()
        return DeletePageCMS(self.driver, self.wait)

    def resultsTable(self):
        return self.wait.until(lambda driver:driver.find_elements_by_xpath("//table[@id='result_list']/tbody/tr"))
    
    def countRowsInResultsTable(self):
        return len(self.resultsTable())
    
    def selectFromTableFirstItemOlderThanYesterday(self):
        nbOfRows = self.countRowsInResultsTable()
        yesterday = datetime.now() - timedelta(days=1)
        for i in xrange(1, nbOfRows):
            lastModifiedDate = self.wait.until(lambda driver:driver.find_element_by_xpath("//table[@id='result_list']/tbody/tr[%d]/td[last()]" % i)).text
            lastModifiedDate = datetime.strptime(lastModifiedDate, "%Y-%m-%d %H:%M:%S")
            if (lastModifiedDate <= yesterday):
                element = self.wait.until(lambda driver:driver.find_element_by_xpath("//table[@id='result_list']/tbody/tr[%d]/th/a" % i))
                element.click()
                break
    
    def clickExpandLinkFor(self, linkText):
        link = self.wait.until(lambda driver : driver.find_element_by_xpath("//h2[text()='%s']/a" %linkText))
        link.click()
    
    def typeInTextarea(self, textArea, text):
        textArea.clear()
        textArea.send_keys(text)
    
    def getSuccessfullyEditMessage(self):
        message = self.wait.until(lambda driver : driver.find_element_by_xpath("//ul[@class='messagelist']/li[@class='info']"))
        return message.text
    
    def typeInTextFieldById(self, fieldId, filePath):
        self.fileBox = self.wait.until(lambda driver : driver.find_element_by_id(fieldId))
        self.fileBox.send_keys(filePath)
    
    def getNumberOfResultsNextToPaginator(self):
        paginator = self.wait.until(lambda driver:driver.find_element_by_xpath("//p[@class='paginator']"))
        fullText = paginator.text
        words = fullText.split(" ")
        total = words[len(words) - 2]
        return total
    
    def clickLastPageInPaginatorIfExists(self):
        paginatorXpath = "//p[@class='paginator']/a"
        if(self.elementExistsByXpath(paginatorXpath)):
            pages = self.wait.until(lambda driver:driver.find_elements_by_xpath(paginatorXpath))
            pages[len(pages)-1].click()
    
    def search_in_searchbar(self, keyword):
        searchbox = self.wait.until(lambda driver:driver.find_element_by_id("searchbar"))
        searchbox.clear()
        searchbox.send_keys(keyword)
        searchbox.submit()
    
    def clickItemInListTableByIndex(self, index):
        item = self.wait.until(lambda driver : driver.find_element_by_xpath("//table[@id='result_list']/tbody/tr[%d]/th/a" %index))
        item.click()
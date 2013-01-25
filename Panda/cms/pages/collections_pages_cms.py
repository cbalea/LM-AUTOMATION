'''
Created on 19.11.2012

@author: cbalea
'''
from cms.pages.base_page_cms import BasePageCMS
from selenium.webdriver.support.select import Select
from utils.server_related import ServerRelated
import re
from cms.pages.resource.resources_pages_cms import ResourcesPagesCMS

class CollectionsPage(BasePageCMS):
     
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.driver.get(ServerRelated().serverToBeTested() + "admin/cms/collection/")
    
    def clickAddCollection(self):
        self.clickAddButton()
        return EditCollectionPageCMS(self.driver, self.wait)
    
    def openCollection(self, link):
        self.clickShowAllLinkIfExists()
        self.clickOnLink(link)
        return EditCollectionPageCMS(self.driver, self.wait) 



class EditCollectionPageCMS(BasePageCMS):
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.title = self.wait.until(lambda driver : driver.find_element_by_id("id_title"))
        self.url = self.wait.until(lambda driver : driver.find_element_by_id("id_url"))
        self.template = Select(self.wait.until(lambda driver : driver.find_element_by_id("id_collection_template")))
        
    def shortDescriptionField(self):
        return self.wait.until(lambda driver : driver.find_element_by_id("id_short_description"))
    
    def keywordsField(self):
        return self.wait.until(lambda driver : driver.find_element_by_id("id_keywords"))
    
    def role(self):
        return Select(self.wait.until(lambda driver:driver.find_element_by_xpath("//td[@class='req_attr_role']/select")))
    
    def entity(self):
        return Select(self.wait.until(lambda driver:driver.find_element_by_xpath("//select[@class='entity_select']")))
    
    def attributionsTextfield(self):
        return self.wait.until(lambda driver:driver.find_element_by_xpath("//textarea[contains(@name, 'req_attr_text_')]"))
    
    

    
    
    def typeTitle(self, title):
        self.title.send_keys(title)
    
    def typeUrl(self, url):
        self.url.send_keys(url)
    
    def selectCollectionTemplate(self, text):
        self.template.select_by_visible_text(text)
    
    def clickCategoryCheckbox(self, checkboxIndex):
        checkbox = self.wait.until(lambda driver : driver.find_element_by_xpath("//input[@type='checkbox' and @id='id_category_%s']" %checkboxIndex))
        checkbox.click()
    
    def clickSubjectCheckbox(self, checkboxIndex):
        checkbox = self.wait.until(lambda driver : driver.find_element_by_xpath("//input[@type='checkbox' and @id='id_subject_%s']" %checkboxIndex))
        checkbox.click()
    
    def typeShortDescription(self, text):
        self.typeInTextarea(self.shortDescriptionField(), text)
    
    def typeLongDescription(self, text):
        self.typeInTinymceEditor("id_long_description_ifr", text)
    
    def typeKeywords(self, text):
        self.typeInTextarea(self.keywordsField(), text)
    
    def getTitle(self):
        return self.title.get_attribute("value")
    
    def getUrl(self):
        return self.url.get_attribute("value")
    
    def getSelectedCollectionTemplate(self):
        return self.template.first_selected_option.text
    
    def getShortDescription(self):
        return self.shortDescriptionField().text
    
    def getLongDescription(self):
        return self.getContentOfTinymceEditor("id_long_description_ifr")
    
    def getKeywords(self):
        return self.keywordsField().text
    
    def extractIndex(self, element, startSubstring):
        attribute = element.get_attribute("id")
        number = re.search('%s(.+?)' %startSubstring, attribute).group(1)
        return int(number)

    def getClickedBoxes(self, elementsList, startSubstring):
        clickedBoxes = []
        for element in elementsList:
            number = self.extractIndex(element, startSubstring)
            clickedBoxes.append(number)
        return clickedBoxes

    def getClickedCategoryCheckboxes(self):
        elementsList = self.wait.until(lambda driver:driver.find_elements_by_xpath("//input[@type='checkbox' and contains(@id,'id_category_') and @checked='checked']"))
        return self.getClickedBoxes(elementsList, "id_category_")
        
    def getClickedSubjectCheckboxes(self):
        elementsList = self.wait.until(lambda driver:driver.find_elements_by_xpath("//input[@type='checkbox' and contains(@id,'id_subject_') and @checked='checked']"))
        return self.getClickedBoxes(elementsList, "id_subject_")
    
    def selectNewRelatedResource(self, optionIndex):
        selectBoxes = self.wait.until(lambda driver : driver.find_elements_by_xpath("//select[contains(@id, '-resource')]"))
        total = len(selectBoxes)
        resourceBox = Select(self.wait.until(lambda driver : driver.find_element_by_id("id_collectionresource_set-%s-resource" %(total-2) )))
        resourceBox.select_by_index(optionIndex)
    
    def typeInOrderBoxWithIndex(self, index, orderNumber):
        box = self.wait.until(lambda driver:driver.find_element_by_id("id_collectionresource_set-%s-order" %index))
        box.clear()
        box.send_keys(orderNumber)
    
    def getNumberOfAttachedResources(self):
        attachedResources = self.wait.until(lambda driver:driver.find_elements_by_xpath("//tr[contains(@id,'collectionresource_set')]/td[@class='original']/p"))
        return len(attachedResources)
    
    def getResourceOrderNumber(self, resIndex):
        orderBox = self.wait.until(lambda driver:driver.find_element_by_id("id_collectionresource_set-%s-order" %resIndex))
        return orderBox.get_attribute("value")
    
    def typeThumbnailFilePath(self, filePath):
        self.typeInTextFieldById("id_thumbnail", filePath)
    
    def typeBannerFilePath(self, filePath):
        self.typeInTextFieldById("id_banner", filePath)
    
    def getCurrentThumbnail(self):
        thumbnail = self.wait.until(lambda driver:driver.find_element_by_xpath("//label[text()='Thumbnail:']/../a"))
        return thumbnail.text
    
    def getCurrentBanner(self):
        banner = self.wait.until(lambda driver:driver.find_element_by_xpath("//label[text()='Banner:']/../a"))
        return banner.text
    
    def selectRoleByVisibleText(self, option):
        self.role().select_by_visible_text(option)
    
    def selectEntityByVisibleText(self, option):
        self.entity().select_by_visible_text(option)
    
    def selectEntityByIndex(self, index):
        self.entity().select_by_index(index)
    
    def typeAttributionsText(self, text):
        textArea = self.attributionsTextfield()
        self.typeInTextarea(textArea, text)
        
    def getSelectedRole(self):
        return self.role().first_selected_option.text
    
    def getSelectedEntity(self):
        return self.entity().first_selected_option.text
    
    def getAttributionsText(self):
        return self.attributionsTextfield().text
    
    def typeCredits(self, text):
        self.typeInTinymceEditor("id_credits_ifr", text)
    
    def getCredits(self):
        return self.getContentOfTinymceEditor("id_credits_ifr")
    
    def clickSaveAndContinueEditingButton(self):
        self.clickSaveAndContinueEditing()
        return EditCollectionPageCMS(self.driver, self.wait)
    
    def searchForResource(self, searchString):
        searchBox = self.wait.until(lambda driver:driver.find_element_by_id("resource_select_bar"))
        searchBox.send_keys(searchString)
        selectButton = self.wait.until(lambda driver:driver.find_element_by_id("submitter_resource_select"))
        selectButton.click()
        self.switchToNewestWindow()
        return ResourcesPagesCMS(self.driver, self.wait, "filtered")
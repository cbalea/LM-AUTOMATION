'''
Created on Sep 25, 2012

@author: jseichei
'''

from cms.pages.base_page_cms import BasePageCMS
from cms.pages.media.media_pages_cms import EditAddMediaPageCMS, MediasPageCMS
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import Select
from utils.server_related import ServerRelated
import time


class AssetsPageCMS(BasePageCMS):
    
    def __init__(self, driver, wait, filtered=None):
        self.driver = driver
        self.wait = wait
        if(filtered == None):
            self.driver.get(ServerRelated().serverToBeTested() + "/admin/cms/asset/")
    

    def filterViewBy(self, filterBy):
        self.clickOnLink(filterBy)
        return AssetsPageCMS(self.driver, self.wait, "filtered")
    
    def clickAssetByIndex(self, index):
        self.clickItemInListTableByIndex(index)
        return AddEditAssetPageCMS(self.driver, self.wait)

    def clickOnAsset(self, asset):
        self.clickLastPageInPaginatorIfExists()
        self.clickOnLink(asset)
        return AddEditAssetPageCMS(self.driver, self.wait)



class AddEditAssetPageCMS(BasePageCMS):
    
    def __init__(self, driver, wait, loadFromUrl=None):
        self.driver = driver
        self.wait = wait
        if(loadFromUrl!=None):
            self.driver.get(ServerRelated().serverToBeTested() + "admin/cms/asset/add/")
        self.title = self.wait.until(lambda driver : driver.find_element_by_id("id_title"))
        self.contentProjectComboboxAsset =  Select(self.wait.until(lambda driver : driver.find_element_by_id("id_content_project")))
        self.type = Select(self.wait.until(lambda driver : driver.find_element_by_id("id_type")))

    def externalLink(self):
        return self.wait.until(lambda driver:driver.find_element_by_id("id_external_link"))
    
    def externalTranscript(self):
        return self.wait.until(lambda driver:driver.find_element_by_id("id_external_transcript"))
    
    
    
    def selectContentProjectAssetByIndex(self, index):
        self.contentProjectComboboxAsset.select_by_index(index)
    
    def selectTypeByLabel(self, label):
        self.type.select_by_visible_text(label)
        
    def typeTitle(self, title):
        self.title.send_keys(title)
        
    def clickToSaveButton(self):
        self.clickSave()
        return AddEditAssetPageCMS(self.driver, self.wait)
        
    def getTitleAsset(self):
        return self.title.get_attribute("value")

    def clickToSaveAndContinueButton(self):
        self.clickSaveAndContinueEditing()
        return AddEditAssetPageCMS(self.driver, self.wait)
    
    def clickToHideShowAttribution(self):
        self.showHideAttributions = self.wait.until(lambda driver : driver.find_element_by_xpath("//h2[contains(text(),'Attributions')]/a"))
        self.showHideAttributions.click()
        
    def selectAttributionRole(self, role):
        self.roleComboBox = Select(self.wait.until(lambda driver : driver.find_element_by_name("req_attr_role_0")))
        self.roleComboBox.select_by_visible_text(role)
    
    def getAttributionRole(self):
        role = self.wait.until(lambda driver : driver.find_element_by_xpath("//select[contains(@name,'req_attr_role')]/option[@selected='selected']"))                                                          
        return role.text     
    
    def selectEntityByIndex(self, index):
        entityComboBox = Select(self.wait.until(lambda driver : driver.find_element_by_id("entity_0")))
        entityComboBox.select_by_index(index)
    
    def writeInTextareaField(self, text):
        textareaField = self.driver.find_element_by_xpath("//textarea[@name='req_attr_text_0']")
        textareaField.send_keys(text)
    
    def completeAttribution(self, role, text):
        self.clickToHideShowAttribution()
        self.selectAttributionRole(role)
        self.selectEntityByIndex(2)
        self.writeInTextareaField(text)

    def searchMediaByText(self, text):
        searchbar = self.wait.until(lambda driver:driver.find_element_by_id("searchbar"))
        searchbar.send_keys(text)
        self.clickOnLink("Search")
        self.switchToNewestWindow()
        return MediasPageCMS(self.driver, self.wait, "add_media_to_asset")

    def addMediaByText(self, text):
        mediaPg = self.searchMediaByText(text)
        mediaPg.clickCheckboxByIndex(1)
        mediaPg.clickAddMediaToAssetButton()
        self.waitUntilPopupCloses()
        self.switchToNewestWindow()
    
    def firstMediaCombobox(self):
        return Select(self.wait.until(lambda driver:driver.find_element_by_id("id_asset_media_asset-0-media")))

    def selectAssetMediaByVisibleText(self, value):
        self.assetMediaComboBox1 = self.firstMediaCombobox()
        self.assetMediaComboBox1.select_by_visible_text(value)
    
    def clickShowHideLinkForField(self, field):
        expanderLink = self.wait.until(lambda driver : driver.find_element_by_xpath("//h2[contains(text(), '%s')]/a" %field))
        expanderLink.click()
        
    def getMediaObjectType(self):
        self.mediaObjectType = self.wait.until(lambda driver : driver.find_element_by_id("id_asset_media_asset-0-media")) 
        return self.mediaObjectType.get_attribute("value") 
    
    def addPosterImage(self, posterImagePath):
        self.posterImage = self.wait.until(lambda driver : driver.find_element_by_id("id_poster_image")) 
        self.posterImage.send_keys(posterImagePath)
        
    def getPosterImage(self):
        self.posterImageSource = self.wait.until(lambda driver : driver.find_element_by_xpath("//div/label[text()='Poster image:']/../a/img"))
        return self.posterImageSource.get_attribute('src')
   
    def typeInDescriptionBox(self, text):
        textAreaDescription = self.wait.until(lambda driver : driver.find_element_by_id("id_description")) 
        textAreaDescription.clear()
        textAreaDescription.send_keys(text)
    
    def getDescriptionBoxMetadata(self):
        self.textAreaDescription = self.wait.until(lambda driver : driver.find_element_by_id("id_description")) 
        return self.textAreaDescription.text
    
    def typeInAssetType(self, assetText):
        assetType = self.wait.until(lambda driver : driver.find_element_by_id("id_asset_type")) 
        assetType.clear()
        assetType.send_keys(assetText)
    
    def getAssetType(self):
        gettingAssetType = self.wait.until(lambda driver : driver.find_element_by_id("id_asset_type")) 
        return gettingAssetType.get_attribute("value")
        
    def selectMediaTypeGeneral(self):
        mediaTypeGeneral = Select(self.wait.until(lambda driver : driver.find_element_by_id("id_media_type_general")))
        mediaTypeGeneral.select_by_visible_text("Video")
        
    def getMediaTypeGeneral(self):
        gettingmediaTypeGeneral = Select(self.wait.until(lambda driver : driver.find_element_by_xpath("//select[@id='id_media_type_general']")))
        return gettingmediaTypeGeneral.first_selected_option.text
    
    def selectMediaTypeSpecific(self):
        mediaType = self.wait.until(lambda driver : driver.find_element_by_xpath("//select[@id='id_media_type_specific']/option[2]"))
        mediaType.click()
        
    def getMediaTypeSpecific(self):
        gettingMediaTypeSpecific =  self.wait.until(lambda driver : driver.find_element_by_xpath("//select[@id='id_media_type_specific']/option[@selected='selected']"))
        return gettingMediaTypeSpecific.text   
    
    def selectAccessibilityIndicatorsAccessModesAuditory(self):
        accessModesAuditory = self.wait.until(lambda driver : driver.find_element_by_id("id_accessibility_indicators_1"))
        if(self.isCheckboxChecked(accessModesAuditory) == False):
            accessModesAuditory.click()
         
    def getAccessibilityIndicatorsAccessModesAuditory(self):
        gettingAccessibilityIndicatorsAccessModesAuditory = self.wait.until(lambda driver : driver.find_element_by_id("id_accessibility_indicators_1"))
        return self.isCheckboxChecked(gettingAccessibilityIndicatorsAccessModesAuditory)
    
    def selectAccessibilityIndicatorsControlFlexibilityFullKeyboardControl(self):
        fullKeyboardControl = self.wait.until(lambda driver : driver.find_element_by_id("id_accessibility_indicators_8"))
        if(self.isCheckboxChecked(fullKeyboardControl) == False):
            fullKeyboardControl.click()
        
    def getAccessibilityIndicatorsControlFlexibilityFullKeyboardControl(self):
        gettingAccessibilityIndicatorsControlFlexibilityFullKeyboardControl = self.wait.until(lambda driver : driver.find_element_by_id("id_accessibility_indicators_8"))
        return self.isCheckboxChecked(gettingAccessibilityIndicatorsControlFlexibilityFullKeyboardControl)   
    
    def selectAccessibilityIndicatorsHazardsSound(self):
        sounds = self.wait.until(lambda driver : driver.find_element_by_id("id_accessibility_indicators_12"))
        if(self.isCheckboxChecked(sounds) == False):
            sounds.click()
        
    def completeMetadaFields(self, text, assetText):
        self.clickShowHideLinkForField("Metadata")
        self.typeInDescriptionBox(text)
        self.typeInAssetType(assetText)
        self.selectMediaTypeGeneral()
        self.selectMediaTypeSpecific()
        self.selectAccessibilityIndicatorsAccessModesAuditory()
        self.selectAccessibilityIndicatorsControlFlexibilityFullKeyboardControl()
        self.selectAccessibilityIndicatorsHazardsSound()

    def typeInRightsCopyright(self, rightsCopyrightText):
        rightsCopyright =  self.wait.until(lambda driver : driver.find_element_by_id("id_rights_copyright"))
        rightsCopyright.clear()
        rightsCopyright.send_keys(rightsCopyrightText)
    
    def selectRightsDistribution(self):
        self.rigthsDistribution = Select(self.wait.until(lambda driver : driver.find_element_by_id("id_rights_distribution")))
        self.rigthsDistribution.select_by_visible_text("Commercial") 
        
    def getRightsDistribution(self):
        self.gettingRigthsDistribution = self.wait.until(lambda driver : driver.find_element_by_xpath("//select[@id='id_rights_distribution']/option[@selected='selected']"))
        return self.gettingRigthsDistribution.text    
        
    def selectRightsSummary(self):
        self.rightsSummary = Select(self.wait.until(lambda driver : driver.find_element_by_id("id_rights_summary")))
        self.rightsSummary.select_by_visible_text("Stream, Download and Share")    
        
    def getRightsSummary(self):
        self.gettingRightsSummary =  self.wait.until(lambda driver : driver.find_element_by_xpath("//select[@id='id_rights_summary']/option[@selected='selected']"))
        return self.gettingRightsSummary.text
    
    def selectAvailableFromDate(self):
        self.availableFromDate = self.wait.until(lambda driver : driver.find_element_by_xpath("//input[@id='id_available_from_date']/following-sibling::*/a[text()='Today']"))
        self.availableFromDate.click()
        
    def selectExpirationDate(self):
        self.expirationDate =  self.wait.until(lambda driver : driver.find_element_by_xpath("//input[@id='id_expiration_date']/following-sibling::*/a[text()='Today']")) 
        self.expirationDate.click()
        
    def completeOwnershipAndRights(self, rightsCopyrightText):
        self.clickShowHideLinkForField("Ownership and Rights")
        self.typeInRightsCopyright(rightsCopyrightText)
        self.selectRightsDistribution()
        self.selectRightsSummary()
        self.selectAvailableFromDate()
        self.selectExpirationDate()    
        
    def typeInContentFlagsDescription(self, contentFlagsDescriptionText):
        contentFlagsDescription =  self.wait.until(lambda driver : driver.find_element_by_id("id_content_flags_description"))       
        contentFlagsDescription.clear()
        contentFlagsDescription.send_keys(contentFlagsDescriptionText)
        
    def getContentFlagsDescription(self):
        gettingContentFlagsDescription = self.wait.until(lambda driver : driver.find_element_by_id("id_content_flags_description")) 
        return gettingContentFlagsDescription.text
    
    def completeAdditionalMetadata(self, sourceIdentifierText, contentFlagsDescriptionText):
        self.clickShowHideLinkForField("Additional Metadata")
        self.typeInContentFlagsDescription(contentFlagsDescriptionText)    
        
    def clickToShowHideAssetBoxes(self):
        self.clickShowHideLinkForField("Attributions")
        self.clickShowHideLinkForField("Metadata")
        self.clickShowHideLinkForField("Ownership and Rights")
        self.clickShowHideLinkForField("Additional Metadata")
                  
    def clickToSaveAsButton(self):
        saveAs =  self.wait.until(lambda driver : driver.find_element_by_xpath("//a[@class='button submitter' and text()='Save As']"))
        saveAs.click()
        return AddEditAssetPageCMS(self.driver, self.wait)
    
    def getAssetCodeValue(self):
        try:
            assetCode = self.wait.until(lambda driver : driver.find_element_by_id("id_asset_code")).get_attribute("value")
            return assetCode
        except StaleElementReferenceException:
            return False
    
    def waitUntilIsCloned(self, AssetCodeOld):
        AssedCodeNew = self.getAssetCodeValue()
        while AssetCodeOld == AssedCodeNew:
            time.sleep(1)
            AssedCodeNew = self.getAssetCodeValue()
       
    def clickAddMediaButton(self):
        addMediaButton =  self.wait.until(lambda driver : driver.find_element_by_xpath("//a[@id='add_id_asset_media_asset-0-media']"))
        addMediaButton.click()
        self.switchToNewestWindow()
        return EditAddMediaPageCMS(self.driver, self.wait)

    def clickIsPrimaryMedia(self):
        isPrimaryCheckbox = self.wait.until(lambda driver : driver.find_element_by_xpath("//input[@type='checkbox' and contains(@id,'is_primary')]"))
        if(self.isCheckboxChecked(isPrimaryCheckbox) == False):
            isPrimaryCheckbox.click()
    
    def clickDeleteMediaCheckboxByMediaName(self, media_name):
        deleteCheckbox = self.wait.until(lambda driver : driver.find_element_by_xpath("//option[text()='%s']/../../../td[@class='delete']/input" %media_name))
        if(self.isCheckboxChecked(deleteCheckbox) == False):
            deleteCheckbox.click()
    
    def getListOfAttachedMedias(self):
        attachedMedias_text = []
        attachedMedias = self.wait.until(lambda driver : driver.find_elements_by_xpath("//td[@class='field-media']/select/option[@selected='selected']"))
        for media in attachedMedias:
            attachedMedias_text.append(media.text)
        return attachedMedias_text
    
    def typeExternalLink(self, link):
        self.externalLink().send_keys(link)
    
    def getExternalLink(self):
        return self.externalLink().get_attribute("value")
    
    def typeExternalTranscript(self, link):
        self.externalTranscript().send_keys(link)
    
    def getExternalTranscript(self):
        return self.externalTranscript().get_attribute("value")
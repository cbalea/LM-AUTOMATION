'''
Created on Nov 28, 2012

@author: jseichei
'''

from selenium.selenium import selenium
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from ss.pages.base_page_ss import BasePageSS
from utils.server_related import ServerRelated



class MyFoldersPageView(BasePageSS):
    
    def __init__(self, driver, wait, notFirstPageLoad=None):
        self.driver = driver
        self.wait = wait
        if(notFirstPageLoad==None):
            self.driver.get(ServerRelated().serverToBeTested()+"favorites")
        self.myFolders = self.wait.until(lambda driver : driver.find_element_by_xpath("//div[@class='pbscustom section-head']/h5"))
        self.allFavoritesLink = self.wait.until(lambda driver : driver.find_element_by_xpath("//ul[@class='nav nav-pills nav-stacked folders']/li[1]/a[1]"))
        self.sharedWithClass = self.wait.until(lambda driver : driver.find_element_by_xpath("//ul[@class='nav nav-pills nav-stacked folders']/li[2]/a[2]"))
        self.sharedWithColleagues = self.wait.until(lambda driver : driver.find_element_by_xpath("//ul[@class='nav nav-pills nav-stacked folders']/li/a[2][contains(text(), 'Shared with Colleagues')]"))
        self.newFolder = self.wait.until(lambda driver : driver.find_element_by_xpath("//ul[@class='nav nav-pills nav-stacked folders']/li/a[@id='new-folder']"))
        self.addToFolderButton = self.wait.until(lambda driver : driver.find_element_by_id("add-to-folder"))
        self.selectAllButton = self.wait.until(lambda driver : driver.find_element_by_id("select-all"))


    def getAllFavorites(self):
        return self.allFavoritesLink.text
    
    def clickToAllFavorites(self):
        self.allFavoritesLink.click()
        return MyFoldersPageView(self.driver, self.wait, "notFirstLoad")
    
    def createNewFolder(self):
        self.newFolder.click()

    def folderNameEditField(self):
        return self.wait.until(lambda driver:driver.find_element_by_id("id_name"))

    def typeAddNewFolderName(self, folderName):
        self.folderNameEditField().send_keys(folderName)
        
    def typeAddNewFolderDescription(self, text):
        self.typeInTinymceEditor("id_description_ifr", text)
        
    def clickSharedWithClass(self):
        sharedWithClass =  self.wait.until(lambda driver : driver.find_element_by_id("id_shared_with_class")) 
        sharedWithClass.click()
        
    def clickSharedWithColleagues(self):
        sharedwithcolleagues = self.wait.until(lambda driver : driver.find_element_by_id("id_shared_with_colleagues"))    
        sharedwithcolleagues.click()
        
    def clickDeleteFolder(self):
        deleteFolder = self.wait.until(lambda driver : driver.find_element_by_id("confirm-delete-folder")) 
        deleteFolder.click() 
    
    def clickToCreateButton(self):
        self.folderNameEditField().submit()
        return MyFoldersPageView(self.driver, self.wait, "notFirstLoad")
        
    def clickToDesiredFolder(self, desiredFolderName):
        desiredFolder =  self.wait.until(lambda driver : driver.find_element_by_xpath("//ul[@class='nav nav-pills nav-stacked folders']/li/a[contains(text(), '%s')]" %desiredFolderName))
        desiredFolder.click()
        return MyFoldersPageView(self.driver, self.wait, "notFirstLoad")  
           
    
    def clickToEditFolders(self, folderName):
        folderName = self.wait.until(lambda driver : driver.find_element_by_xpath("//a[text()='%s']" %folderName))
        linkId = folderName.get_attribute("data-folder-id")
        click_edit_jquery='$(".edit", $(".folders a[data-folder-id=' + "'" + linkId +  "'" + ']").parent()).click()' 
        self.driver.execute_script(click_edit_jquery)
        self.switchToNewestWindow()
       

    def clickSave(self):
        saveButton = self.wait.until(lambda driver : driver.find_element_by_xpath("//input[@value='save']"))
        saveButton.click()
        return MyFoldersPageView(self.driver, self.wait)   


    def getCreatedFolder(self, foldarName):
        getFolder =  self.wait.until(lambda driver : driver.find_element_by_xpath("(//ul[@class='nav nav-pills nav-stacked folders']/li/a[2][@href])[contains(text(), '%s')]" %foldarName))     
        return getFolder.text


    def folderExists(self, folderName):
        return self.elementExistsByLinkText(folderName)

    
    def clickCheckboxForResource(self, resourceTitle):
        checkbox = self.wait.until(lambda driver : driver.find_element_by_xpath("//a[text()='%s']/../input[@type='checkbox']" %resourceTitle))
        checkbox.click()

    def clickRemoveButton(self):
        removeButton = self.wait.until(lambda driver:driver.find_element_by_xpath("//a[text()='remove']"))
        removeButton.click()

    def clickConfirmRemoveButton(self):
        confirmRemoveBtn = self.wait.until(lambda driver:driver.find_element_by_xpath("//a[@class='btn confirm' and text()='remove']"))
        confirmRemoveBtn.click()
        return MyFoldersPageView(self.driver, self.wait, "notFirstLoad")

    def clickAddToFolderButton(self):
        self.addToFolderButton.click()
        self.switchToNewestWindow()
        
    def clickToSelectAllButton(self):
        self.selectAllButton.click()    
    
    def isDisplayedSelectFolderWidget(self):
        return self.elementExistsByXpath("//div[@aria-labelledby='ui-dialog-title-folder-tree']")
    
    
    def selectFolder(self, folderName):
        addToFolder = self.wait.until(lambda driver : driver.find_element_by_xpath("//li/a[@class = 'folder'][contains(text(), '%s')]"%folderName))
        addToFolder.click()
        return MyFoldersPageView(self.driver, self.wait)
        
    def getFavoritesFromFolders(self):
        favInFolders = self.wait.until(lambda driver : driver.find_elements_by_xpath("//div[@class='media-body']/form/h3/a[contains(@href, '/resource/')]"))
        return favInFolders[0].text
        
    


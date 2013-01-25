'''
Created on 09.10.2012

@author: cbalea
'''
from cms.pages.base_page_cms import BasePageCMS
from cms.pages.station_site_cms.station_module_pages_cms import \
    EditAddStationModulePageCMS
from selenium.webdriver.support.select import Select
from utils.server_related import ServerRelated


class DashboardPageCMS(BasePageCMS):
    
    def __init__(self, driver, wait, noPageLoad=None):
        self.driver = driver
        self.wait = wait
        if(noPageLoad==None):
            self.driver.get(ServerRelated().serverToBeTested() + "admin/cms/contentproject/dashboard/")
        self.uploadDropdown = Select(self.wait.until(lambda driver : driver.find_element_by_id("id_upload_media")))
        self.createDropdown = Select(self.wait.until(lambda driver : driver.find_element_by_id("id_create_content")))
    
    def selectUploadMediaByText(self, media):
        self.uploadDropdown.select_by_visible_text(media)
    
    def selectCreateUser(self):
        self.createDropdown.select_by_visible_text("User")
        return OrganizationUsersPageCMS(self.driver, self.wait)
    
    def getNumberOfVisibleContentProjects(self):
        self.contProjects = self.wait.until(lambda driver : driver.find_elements_by_xpath("//li[contains(text(),'Content Projects')]/ul/li"))
        return len(self.contProjects)
    
    def clickModifyStationModule(self):
        self.clickOnLink("Modify Station Module")
        return EditAddStationModulePageCMS(self.driver, self.wait)

    def clickUsersLink(self):
        self.clickOnLink("Users")
        return OrganizationUsersPageCMS(self.driver, self.wait)

    def getTitlesFromDashboard(self):
        dashboardTitles = self.wait.until(lambda driver : driver.find_elements_by_xpath("//tbody[@id='content_items_table_body']/tr/td[@class='original']"))
        titles = []
        for element in dashboardTitles:
            titles.append(element.text)
        return titles
    


class OrganizationUsersPageCMS(BasePageCMS):
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.email = self.wait.until(lambda driver : driver.find_element_by_id("id_add_user-email"))
        self.contentAdminRadio = self.wait.until(lambda driver : driver.find_element_by_xpath("//input[@value='contributor_admin' and @name='add_user-team_contributor']"))
        self.contentEditorRadio = self.wait.until(lambda driver : driver.find_element_by_xpath("//input[@value='contributor_editor' and @name='add_user-team_contributor']"))
        self.stationAdminRadio =  self.wait.until(lambda driver : driver.find_element_by_xpath("//input[@value='station_admin' and @name='add_user-team_station']"))
        self.stationEditorRadio = self.wait.until(lambda driver : driver.find_element_by_xpath("//input[@value='station_editor' and @name='add_user-team_station']"))
    

    def typeEmail(self, email):
        self.email.send_keys(email)
    
    def clickContentAdminRadio(self):
        self.contentAdminRadio.click()
        
    def clickContentEditorRadio(self):
        self.contentEditorRadio.click()
    
    def clickStationAdminRadio(self):
        self.stationAdminRadio.click()
    
    def clickStationEditorRadio(self):
        self.stationEditorRadio.click()
    
    def clickSaveButtonAddUserForm(self):
        self.email.submit()
        return OrganizationUsersPageCMS(self.driver, self.wait)
    
    def userExists(self, userEmail):
        return self.elementExistsByXpath("//td[text()='%s']" %userEmail)
    
    def showDeletedUsers(self):
        yesLink = self.wait.until(lambda driver : driver.find_element_by_xpath("//h3[text()='Show Deleted Users']/../ul/li/a[text()='Yes']"))
        yesLink.click()
        return OrganizationUsersPageCMS(self.driver, self.wait)
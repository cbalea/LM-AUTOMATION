'''
Created on 08.10.2012

@author: cbalea
'''
from cms.pages.base_page_cms import BasePageCMS
from selenium.webdriver.support.select import Select
from utils.server_related import ServerRelated



class ContentProjectsPageCMS(BasePageCMS):

    def __init__(self, driver, wait, noFreshLoad=None):
        self.driver = driver
        self.wait = wait
        if(noFreshLoad==None):
            self.driver.get(ServerRelated().serverToBeTested() + "admin/cms/contentproject/")
    
    def clickContentProjectByIndex(self, index):
        self.clickItemInListTableByIndex(index)
        return EditContentProjectPageCMS(self.driver, self.wait)
    
    def clickContentProjectByName(self, projectName):
        self.search_in_searchbar(projectName)
        self.clickOnLink(projectName)
        return EditContentProjectPageCMS(self.driver, self.wait)
    
    def clickAddContentProject(self):
        self.clickAddButton()
        return EditContentProjectPageCMS(self.driver, self.wait)
        


class EditContentProjectPageCMS(BasePageCMS):
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.title = self.wait.until(lambda driver : driver.find_element_by_id("id_title"))
        self.organization = Select(self.wait.until(lambda driver : driver.find_element_by_id("id_organization")))
    
    def selectStatusFilter(self, status):
        self.statusFilter = Select(self.wait.until(lambda driver : driver.find_element_by_id("content_item_search_status")))
        self.statusFilter.select_by_visible_text(status)
    
    def itemExistsByStatus(self, status):
        return self.elementExistsByXpath("//tbody[@id='content_items_table_body']/tr/td[text()='%s']" %status).is_displayed()
    
    def typeTitle(self, title):
        self.title.send_keys(title)
    
    def getTitle(self):
        return self.title.get_attribute("value")
    
    def clickSaveAndContinueEditingButton(self):
        self.clickSaveAndContinueEditing()
        return EditContentProjectPageCMS(self.driver, self.wait)
    
    def clickShowHideBrandAndRequiredAttributionsLink(self):
        link = self.wait.until(lambda driver : driver.find_element_by_xpath("//h2[contains(text(), 'Brand and Required Attributions')]/a"))
        link.click()

    def roleCombobox(self):
        return Select(self.wait.until(lambda driver : driver.find_element_by_xpath("//select[@class='role_select']")))

    def selectRoleByIndex(self, index):
        self.roleCombobox().select_by_index(index)
    
    def entityCombobox(self):
        return Select(self.wait.until(lambda driver : driver.find_element_by_xpath("//select[@class='entity_select']")))

    def selectEntityByValue(self, value):
        self.entityCombobox().select_by_visible_text(value)
    
    def selectOrganizationByValue(self, organizationName):
        self.organization.select_by_visible_text("------ %s" %organizationName)
    
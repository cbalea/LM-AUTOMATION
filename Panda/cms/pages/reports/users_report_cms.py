'''
Created on 28.11.2012

@author: cbalea
'''
from cms.pages.reports.reports_base_cms import ReportsBaseCMS
from selenium.webdriver.support.select import Select
from utils.server_related import ServerRelated


class UsersReportCMS(ReportsBaseCMS):
    
    organization_dropdown_id = "id_team__organization__name"
    
    def __init__(self, driver, wait, report=None):
        self.driver = driver
        self.wait = wait
        if(report == None):
            self.driver.get(ServerRelated().serverToBeTested() + "admin/reports/user-report/")
        self.groupByField = Select(self.wait.until(lambda driver : driver.find_element_by_id("id_groupby")))
        self.contentProjectDropdown = Select(self.wait.until(lambda driver : driver.find_element_by_id("id_team__organization__contentproject__title")))


    def selectGroupByField(self, option):
        self.groupByField.select_by_visible_text(option)
        
    def selectOrganizationByValue(self, text):
        organization = Select(self.wait.until(lambda driver : driver.find_element_by_id("id_team__organization__name")))
        organization.select_by_visible_text(text)
    
    def clickGetResultsButton(self):
        self.clickGetResults()
        return UsersReportCMS(self.driver, self.wait, "report")    
    
    def getContentProjectOptions(self):
        options = self.getOptionsTextInCombobox(self.contentProjectDropdown)
        options.remove("---------")
        return options
        
'''
Created on 28.11.2012

@author: cbalea
'''
from cms.pages.reports.reports_base_cms import ReportsBaseCMS
from selenium.webdriver.support.select import Select
from utils.server_related import ServerRelated


class ResourceReportCMS(ReportsBaseCMS):
    
    def __init__(self, driver, wait, report=None):
        self.driver = driver
        self.wait = wait
        if(report == None):
            self.driver.get(ServerRelated().serverToBeTested() + "admin/reports/resource-report/")
        self.typeFilter = Select(self.wait.until(lambda driver : driver.find_element_by_id("id_type")))
        self.contentProjFilter = Select(self.wait.until(lambda driver : driver.find_element_by_id("id_content_project__title")))
        

    def selectType(self, option):
        self.typeFilter.select_by_visible_text(option)
    
    def selectContentProject(self, index):
        self.contentProjFilter.select_by_index(index)
    
    def clickGetResultsButton(self):
        self.clickGetResults()
        return ResourceReportCMS(self.driver, self.wait, "report")

    def clickPdfButton(self):
        self.clickPdf()
        return ResourceReportCMS(self.driver, self.wait, "report")
    
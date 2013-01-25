'''
Created on 28.11.2012

@author: cbalea
'''
from cms.pages.reports.reports_base_cms import ReportsBaseCMS
from selenium.webdriver.support.select import Select
from utils.server_related import ServerRelated


class AssetsReportCMS(ReportsBaseCMS):
    
    def __init__(self, driver, wait, report=None):
        self.driver = driver
        self.wait = wait
        if(report == None):
            self.driver.get(ServerRelated().serverToBeTested() + "admin/reports/asset-report/")
        self.mediaTypeGeneralFilter = Select(self.wait.until(lambda driver : driver.find_element_by_id("id_media_type_general__name")))

    def selectMediaTypeGeneral(self, option):
        self.mediaTypeGeneralFilter.select_by_visible_text(option)
    
    def clickGetResultsButton(self):
        self.clickGetResults()
        return AssetsReportCMS(self.driver, self.wait, "report")    
    
    def clickExcelButton(self):
        self.clickExcel()
        return AssetsReportCMS(self.driver, self.wait, "report")
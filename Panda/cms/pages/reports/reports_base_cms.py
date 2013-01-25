'''
Created on 28.11.2012

@author: cbalea
'''
from cms.pages.base_page_cms import BasePageCMS
from selenium.webdriver.support.select import Select

class ReportsBaseCMS(BasePageCMS):
    
    def selectGroupByField(self, option):
        groupByField = Select(self.wait.until(lambda driver : driver.find_element_by_id("id_groupby")))
        groupByField.select_by_visible_text(option)
    
    def clickShowOnlyTotalsCheckbox(self):
        showOnlyTotalsCheckbox = self.wait.until(lambda driver : driver.find_element_by_id("id_onlytotals"))
        showOnlyTotalsCheckbox.click()
    
    def clickGetResults(self):
        getResultsButton = self.wait.until(lambda driver : driver.find_element_by_xpath("//button[text()='Get results']"))
        getResultsButton.click()
    
    def getReportTable(self):
        reportTable = self.wait.until(lambda driver : driver.find_elements_by_xpath("//table[@class='report table table-bordered']/tbody/tr[not(contains(@class,'row-hidden'))]"))
        return reportTable
    
    def getTotalResultsInReport(self):
        total = self.wait.until(lambda driver : driver.find_element_by_xpath("//tr[@class='total ']/td"))
        return total.text

    def clickPdf(self):
        pdfButton = self.wait.until(lambda driver : driver.find_element_by_xpath("//button[text()='Pdf']"))
        pdfButton.click()
    
    def clickExcel(self):
        excelButton = self.wait.until(lambda driver : driver.find_element_by_xpath("//button[text()='Excel']"))
        excelButton.click()
    
    def clickColapseButtonInResultsTable(self, buttonIndex):
        collapseButtons = self.wait.until(lambda driver : driver.find_elements_by_xpath("//span[@class='result-collapsable expanded btn btn-mini']"))
        collapseButtons[buttonIndex].click()
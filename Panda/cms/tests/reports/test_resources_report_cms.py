#'''
#Created on 28.11.2012
#
#@author: cbalea
#'''
#from cms.pages.reports.resources_report_cms import ResourceReportCMS
#from cms.pages.resource.resources_pages_cms import ResourcesPagesCMS
#from cms.tests.base_cms_tests import SeleniumTestBaseCMS
#
#
#class TestResourcesReportCMS(SeleniumTestBaseCMS):
#    
#    resType = "Lesson Plan"
#
#    def generateReport(self):
#        resReport = ResourceReportCMS(self.driver, self.wait)
#        resReport.selectType(self.resType)
#        resReport.selectContentProject(1)
#        resReport = resReport.clickGetResultsButton()
#        return resReport
#
#
#
#
#    def test_generate_resources_report(self):
#        resReport = self.generateReport()
#        self.assertTrue(resReport.getReportTable(), "Report table not displayed")
#    
#    def test_download_pdf_report(self):
#        resReport = self.generateReport()
#        resReport.clickPdfButton()
#        self.assertFileIsDownloaded("resource-report.pdf")
#
#    def test_filter_report_results_by_type(self):
#        resPage = ResourcesPagesCMS(self.driver, self.wait)
#        resPage = resPage.filterViewBy(self.resType)
#        nbOfResources = resPage.getNumberOfResultsNextToPaginator()
#        resReport = ResourceReportCMS(self.driver, self.wait)
#        resReport.selectType(self.resType)
#        resReport = resReport.clickGetResultsButton()
#        self.assertEqual(resReport.getTotalResultsInReport(), nbOfResources, "Total resources displayed in report and resources page are not equal.")
#    
#'''
#Created on 28.11.2012
#
#@author: cbalea
#'''
#from cms.pages.asset.add_asset import AssetsPageCMS
#from cms.pages.reports.assets_report_cms import AssetsReportCMS
#from cms.tests.base_cms_tests import SeleniumTestBaseCMS
#from utils.server_related import ServerRelated
#import os
#
#
#class TestAssetsReportCMS(SeleniumTestBaseCMS):
#    
#    mediaType = "Audio"
#    
#    def generateReport(self):
#        assetReport = AssetsReportCMS(self.driver, self.wait)
#        assetReport.selectMediaTypeGeneral(self.mediaType)
#        assetReport = assetReport.clickGetResultsButton()
#        return assetReport
#
#
#
#    def test_generate_assets_report(self):
#        assetReport = self.generateReport()
#        self.assertTrue(assetReport.getReportTable(), "Report table not displayed")
#
#    def test_filter_report_results_by_media_type_general(self):
#        assetsPage = AssetsPageCMS(self.driver, self.wait)
#        assetsPage = assetsPage.filterViewBy(self.mediaType)
#        nbOfAssets = assetsPage.getNumberOfResultsNextToPaginator()
#        assetReport = self.generateReport()
#        self.assertEqual(assetReport.getTotalResultsInReport(), nbOfAssets, "Total assets displayed in report and assets page are not equal.")
#    
#    
#    def test_download_excel_report(self):
#        assetReport = self.generateReport()
#        assetReport.clickExcelButton()
#        self.assertFileIsDownloaded("asset-report.csv")
#'''
#Created on 28.11.2012
#
#@author: cbalea
#'''
#from cms.pages.reports.users_report_cms import UsersReportCMS
#from cms.tests.base_cms_tests import SeleniumTestBaseCMS
#
#
#groupByOption = "Organization"
#
#class TestUsersReportCMS(SeleniumTestBaseCMS):
#    
#    def generateReport(self):
#        userReport = UsersReportCMS(self.driver, self.wait)
#        userReport.selectGroupByField(groupByOption)
#        userReport.selectOrganizationByValue("PBS")
#        userReport = userReport.clickGetResultsButton()
#        return userReport
#
#
#
#    def test_generate_users_report(self):
#        userReport = self.generateReport()
#        self.assertTrue(userReport.getReportTable(), "Report table not displayed")
#
#    def test_colapsing_results_table(self):
#        userReport = self.generateReport()
#        tableRowsBeforeColapse = len(userReport.getReportTable())
#        userReport.clickColapseButtonInResultsTable(0)
#        userReport = UsersReportCMS(self.driver, self.wait, "report")
#        tableRowsAfterColapse = len(userReport.getReportTable())
#        self.assertTrue(tableRowsAfterColapse < tableRowsBeforeColapse, "Table not colapsed")
#        
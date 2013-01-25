'''
Created on 26.11.2012

@author: cbalea
'''
from cms.pages.bulk_csv_cms import BulkCSVsPage
from cms.pages.dashboard_page_cms import DashboardPageCMS
from cms.tests.base_cms_tests import SeleniumTestBaseCMS
from utils.server_related import ServerRelated


class TestBulkUpload(SeleniumTestBaseCMS):
    incorrectFile = "bulk_upload_incorrect_spreadsheet.csv"
    correctFile = "bulk_upload_correct_spreadsheet.csv"
    path = "fixtures/"
    contProj = "PBS LearningMedia"
    

    def add_csv(self, contProj, filePath):
        bulksPage = BulkCSVsPage(self.driver, self.wait)
        addCsvPage = bulksPage.clickAddBulkCSVFile()
        addCsvPage.selectContentProjectByIndex(5)
        addCsvPage.typeSourceFile(ServerRelated().getFilePathInProjectFolder(filePath))
        editCsvPage = addCsvPage.clickSaveAndContinueEditingButton()
        return editCsvPage



    def test_add_bulk_csv_file(self):
        editCsvPage = self.add_csv(self.contProj, self.path+self.incorrectFile)
        self.assertTrue("---------" not in editCsvPage.getContentProject(), "Content Project not saved")
        self.assertTrue(self.incorrectFile in editCsvPage.getCurrentSourceFile(), "CSV File not uploaded")

    def test_do_import_on_correct_bulk_csv_file(self):
        editCsvPage = self.add_csv(self.contProj, self.path+self.correctFile)
        editCsvPage = editCsvPage.clickImportItButton()
        self.assertTrue("Successfully Uploaded" in editCsvPage.getUploadStatus(), "File was not imported")
    
    def test_do_import_on_incorrect_bulk_csv_file(self):
        bulksPage = BulkCSVsPage(self.driver, self.wait)
        editCsvPage = bulksPage.openCsvFile(self.incorrectFile)
        editCsvPage = editCsvPage.clickImportItButton()
        self.assertTrue("CSV File Failed Validation" in editCsvPage.getUploadStatus(), "Errors not printed in the status")

    def test_filter_files_by_file_failed_validation(self):
        bulksPage = BulkCSVsPage(self.driver, self.wait)
        bulksPage = bulksPage.filterCsvFileFailedValidation()
        self.assertTrue(bulksPage.countRowsInResultsTable() >= 1, "No file dispalyed after filtering")
    
    def test_items_imported_from_csv(self):
        dashboard = DashboardPageCMS(self.driver, self.wait)
        self.assertTrue("HeatherBrooke_2012G" in dashboard.getTitlesFromDashboard(), "Media not uploaded from CSV")
        self.assertTrue("TED: Heather Brooke: My Battle to expose government corruption." in dashboard.getTitlesFromDashboard(), "Asset not uploaded from CSV")
    
    def test_remove_bulk_csv_files(self):
        bulksPage = BulkCSVsPage(self.driver, self.wait)
        bulksPage.clickCheckboxForItem(self.incorrectFile, "noSearch")
        bulksPage.clickCheckboxForItem(self.correctFile, "noSearch")
        deletePage = bulksPage.selectDeleteAction()
        newPage = deletePage.clickConfirmationButton()
        self.assertFalse(newPage.elementExistsByLinkText(self.correctFile), "CSV file not deleted")
        self.assertFalse(newPage.elementExistsByLinkText(self.correctFile), "CSV file not deleted")
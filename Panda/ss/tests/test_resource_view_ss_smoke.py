'''
Created on 07.11.2012

@author: cbalea
'''
from common.uua_login_page import UuaLoginPage
from ss.pages.resource_view_page_ss import ResourceViewPageSS
from ss.tests.base_ss_tests import SeleniumTestBaseNoLoginSS
import time

resourceId = "wa10.socst.global.20cent.israpal"
flash_interactive_asset_resourceId = "lsps07.sci.life.oate.nowherehide"
html_interactive_asset_resourceId = "tdc02.sci.life.reg.dancebee"

class TestResourceViewSS(SeleniumTestBaseNoLoginSS):
    
    def test_resourceViewDisplaysCorrectly(self):
        title = "The Israeli Palestinian Conflict"
        grades = "9-12"

        resPage = ResourceViewPageSS(self.driver, self.wait, resourceId)  
        self.assertEqual(title, resPage.getTitle(), "Title not displayed")
        self.assertTrue(grades in resPage.getGrades(), "Grades not displayed")
        self.assertTrue(resPage.getSupportMaterialContent(0) != "", "First Support material text not displayed or is empty")
#        self.assertTrue(resPage.getNumberOfStandards() > 0, "Standards not displayed")
        self.assertTrue(resPage.getNumberOfRelatedResources() > 0, "Related resources not displayed")
        self.assertEqual(self.driver.title, title + " : PBS LearningMedia", "HTML title is incorrect")
    
#    def test_download_document_support_material_from_resoruce(self):
#        resPage = ResourceViewPageSS(self.driver, self.wait, resourceId)
#        documentLink = resPage.getSupportMaterialContent(0)
#        resPage.clickOnLink(documentLink)
#        downloadedFile = "wa10_doc_israpal.doc"
#        time.sleep(3) #wait for download
#        self.assertFileIsDownloaded(downloadedFile)
    
    def test_flash_interractive_asset_plays_from_resource(self):
        resPage = ResourceViewPageSS(self.driver, self.wait, flash_interactive_asset_resourceId)
        new_page = resPage.clickInterractiveAsset()
        self.assertTrue(new_page.elementExistsById("flash"), "Pop-up contains no interactive flash")
    
    def test_html_interractive_asset_plays_from_resource(self):
        resPage = ResourceViewPageSS(self.driver, self.wait, html_interactive_asset_resourceId)
        resPage.clickInterractiveAsset()
        firstPageTitle = self.driver.title
        resPage.clickLinkOnPageByIndex(2)
        secondPageTitle = self.driver.title
        self.assertNotEqual(firstPageTitle, secondPageTitle, "No interaction was performed with the asset")
            
    
    def test_free_resource_views_count_for_unregistered_user(self):
        resPage = ResourceViewPageSS(self.driver, self.wait, resourceId)
        initialCount = resPage.get_number_of_resource_views_left_before_neeting_to_login()
        self.driver.refresh()
        self.driver.refresh()
        uuaLoginPopup = UuaLoginPage(self.driver, self.wait)
        self.assertEqual(initialCount, 2, "Initial count not equal to 2.")
        self.assertTrue(uuaLoginPopup.uua_login_page_is_displayed(), "UUA Login popup not displayed after 3 views")
        
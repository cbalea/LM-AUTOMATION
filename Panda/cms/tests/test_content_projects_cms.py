'''
Created on 09.10.2012

@author: cbalea
'''
from cms.pages.content_project_pages_cms import ContentProjectsPageCMS
from cms.tests.base_cms_tests import SeleniumTestBaseCMS


class TestContentProjectCMS(SeleniumTestBaseCMS):
    
    def test_searchOneStatusInContentProjectReturnsOnlyThatStatus(self):
        contProjListPage = ContentProjectsPageCMS(self.driver, self.wait)
        contProj = contProjListPage.clickContentProjectByName("PBST Forgotten Americans")
        if (contProj.itemExistsByStatus("uploaded") != None):      
            contProj.selectStatusFilter("In Progress")
            self.assertFalse(contProj.itemExistsByStatus("uploaded"), "Although In-Progress filter is selected, Uploaded items still appear in list")


    def test_search_content_projects(self):
        contProjPg = ContentProjectsPageCMS(self.driver, self.wait)
        contProjPg.search_in_searchbar("a")
        contProjPg = ContentProjectsPageCMS(self.driver, self.wait, "noFreshLoad")
        self.assertTrue(contProjPg.countRowsInResultsTable() > 0, "Search results not displayed")
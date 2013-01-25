'''
Created on 06.12.2012

@author: cbalea
'''
from ss.pages.browse_by_standards_page_ss import BrowseByStandardsPageSS
from ss.pages.home_profile_login_pages_ss import HomePageSS
from ss.tests.base_ss_tests import SeleniumTestBaseNoLoginSS


class TestBrowseByCategoriesSS(SeleniumTestBaseNoLoginSS):
    
    def test_selecting_type_of_standards_populates_document_list(self):
        standardsPg = BrowseByStandardsPageSS(self.driver, self.wait, "0")
        standardsPg.selectTypeOfStandardsByIndex(2)
        self.assertTrue(standardsPg.getNumberOfSelectableDocuments() > 0, "Document list not populated")
    
#    def test_search_standards_by_grade(self):
#        standardsPg = BrowseByStandardsPageSS(self.driver, self.wait, "1")
#        standardsPg.selectDocumentByIndex(1)
#        standardsPg.checkGradeCheckbox("4")
#        standardsPg.clickBrowseButton()
#        standardsPg.waitForResultsToLoad()
#        self.assertTrue(standardsPg.getNumberOfDisplayedStandardsSections() > 0, "No standards displayed")
#    
#    def test_search_standards_by_keyword(self):
#        standardsPg = BrowseByStandardsPageSS(self.driver, self.wait, "1")
#        standardsPg.selectDocumentByIndex(1)
#        standardsPg.typeKeyword("a")
#        standardsPg.clickBrowseButton()
#        standardsPg.waitForResultsToLoad()
#        self.assertTrue(standardsPg.getNumberOfDisplayedStandardsSections() > 0, "No standards displayed")
#        self.assertTrue(standardsPg.getNumberOfStandardsForStatement("CCRA.R Reading") > 0, "No number displayed for statements")
        

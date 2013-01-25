'''
Created on 06.12.2012

@author: cbalea
'''
from ss.pages.browse_by_standards_page_ss import BrowseByStandardsPageSS
from ss.pages.home_profile_login_pages_ss import HomePageSS
from ss.tests.base_ss_tests import SeleniumTestBaseNoLoginSS


class TestBrowseByCategoriesSS(SeleniumTestBaseNoLoginSS):
    
    def test_browse_by_section_displayed_under_feature_well(self):
        homePage = HomePageSS(self.driver, self.wait)
        homePage.expand_browse_sections()
        self.assertTrue(homePage.browseByAllGradesSectionHeader.is_displayed(), "Browse by All Grades not displayed")
        self.assertTrue(homePage.browseByAllSubjectsSectionHeader.is_displayed(), "Browse by All Subjects not displayed")
        self.assertTrue(homePage.browseByCollectionsSectionHeader.is_displayed(), "Browse by All Standards not displayed")
        self.assertTrue(homePage.browseByStandardsSectionHeader.is_displayed(), "Browse by All Collections not displayed")
        self.assertTrue(homePage.browse_section_is_displayed_under_feature_well(), "Browse section is not displayed under the feature well")
        
#    def test_browse_by_standards_link_opens_correct_page(self):
#        homePage = HomePageSS(self.driver, self.wait)
#        homePage.expand_browse_sections()
#        browseByStandPg = homePage.clickBrowseByStandardsLink()
#        self.assertEqual(browseByStandPg.getPageTitle(), "Browse by Standards", "Browse by Standards page not opened")
    
    def test_browse_by_grade_level_displayes_only_results_in_that_range(self):
        homePage = HomePageSS(self.driver, self.wait)
        homePage.expand_browse_sections()
        searchResultsPg = homePage.clickGradeIntervalInBrowseByGradeLevels("6-8")
        self.assertTrue("6" in searchResultsPg.getDisplayedGradeFacets(), "Needed grade doesn't have facet")
        self.assertTrue("7" in searchResultsPg.getDisplayedGradeFacets(), "Needed grade doesn't have facet")
        self.assertTrue("8" in searchResultsPg.getDisplayedGradeFacets(), "Needed grade doesn't have facet")
        self.assertEqual(searchResultsPg.getNumberOfDisplayedGradeFacets(), 3, "More grade facets than needed")
        
        
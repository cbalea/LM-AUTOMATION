'''
Created on 09.11.2012

@author: cbalea
'''
from ss.pages.base_page_ss import BasePageSS
from ss.pages.browse_by_standards_page_ss import BrowseByStandardsPageSS
from ss.pages.home_profile_login_pages_ss import HomePageSS
from ss.pages.search_pages_ss import SearchResultsPageSS
from ss.tests.base_ss_tests import SeleniumTestBaseNoLoginSS


class TestSearchSS(SeleniumTestBaseNoLoginSS):
    

    def initiateSearch(self, key):
        homePage = HomePageSS(self.driver, self.wait)
        homePage.searchByKeyword(key)
        resultsPage = SearchResultsPageSS(self.driver, self.wait)
        return resultsPage


    def test_gradeFacetsFilterResults(self):
        resultsPage = self.initiateSearch("test")
        allSearchResults = resultsPage.getNumberOfSearchRestuls()
        resultsPage = resultsPage.clickFirstFacetWithFewerResultsThanFullSearch(resultsPage.gradeFacets, resultsPage.gradeFacetsLinks)
        self.assertNotEquals(allSearchResults, resultsPage.getNumberOfSearchRestuls(), "Results not filtered by grade")
        
    def test_searchKeyword(self):
        resultsPage = self.initiateSearch("test")
        self.assertTrue(resultsPage.getNumberOfSearchRestuls() > 0, "No search results displayed")
        
    def test_searchKeyphrase(self):
        resultsPage = self.initiateSearch('"day of"')
        self.assertTrue(resultsPage.getNumberOfSearchRestuls() > 0, "No search results displayed")
        
    def test_searchResultsDispalyAllFields(self):
        searchWord = "test"
        resultsPage = self.initiateSearch(searchWord)
        self.assertTrue(resultsPage.getResultTitle(0) != "", "Result title not displayed")
        self.assertTrue(resultsPage.getResultDescription(0) != "", "Result description not displayed")
        self.assertTrue(resultsPage.getResultGrades(0) != "", "Result grades not displayed")
        self.assertEqual(self.driver.title, "Search for %s : PBS LearningMedia" %searchWord, "HTML title is incorrect")
    
    def test_search_from_a_different_page_than_home(self):
        standardsPg = BrowseByStandardsPageSS(self.driver, self.wait, "0")
        standardsPg.searchByKeyword("a")
        resultsPage = SearchResultsPageSS(self.driver, self.wait)
        self.assertTrue(resultsPage.getNumberOfSearchRestuls() > 0, "No search results displayed")
    
    def test_search_with_no_keyword_doesnt_crash(self):
        homePage = HomePageSS(self.driver, self.wait)
        homePage.searchByKeyword("")
        self.assertTrue(BasePageSS(self.driver, self.wait).isHeaderImageDisplayed(), "Crash when searching for a void keyword")
    
    def test_search_by_vildcard(self):
        resultsPage = self.initiateSearch("*")
        self.assertTrue(resultsPage.getNumberOfSearchRestuls() > 0, "No search results displayed")
'''
Created on 31.10.2012

@author: cbalea
'''
from ss.pages.home_profile_login_pages_ss import HomePageSS
from ss.pages.resource_view_page_ss import ResourceViewPageSS
from ss.pages.search_pages_ss import SearchResultsPageSS
from ss.tests.base_ss_tests import SeleniumTestBaseSS
import time


class TestFavoriteSS(SeleniumTestBaseSS):
    
    def test_favoriteInResourcePage(self):
        resourceId = "wa10.socst.global.20cent.israpal"
        
        resource = ResourceViewPageSS(self.driver, self.wait, resourceId)
        resource.clickFavoriteStar()
        time.sleep(1)
        resource = ResourceViewPageSS(self.driver, self.wait)
        self.assertTrue(resource.isFavorited(), "Favorite status (fav-ed) not kept after refresh")
        resource.clickFavoriteStar()
        time.sleep(1)
        resource = ResourceViewPageSS(self.driver, self.wait, resourceId)
        self.assertFalse(resource.isFavorited(), "Favorite status (fav-ed) not kept after refresh")


    def test_favoriteInSearchResults(self):
        homePage = HomePageSS(self.driver, self.wait)
        homePage.searchByKeyword("abc")
        resultsPage = SearchResultsPageSS(self.driver, self.wait)
        resultsPage.clickFavoriteStarForResult(1)
        time.sleep(2)
        self.driver.refresh()
        resultsPage = SearchResultsPageSS(self.driver, self.wait)
        self.assertTrue(resultsPage.isFavorited(1), "Favorite status (fav-ed) not recorded")
        resultsPage.clickFavoriteStarForResult(1)
        time.sleep(2)
        self.driver.refresh()
        resultsPage = SearchResultsPageSS(self.driver, self.wait)
        self.assertFalse(resultsPage.isFavorited(1), "Resource is marked as favorite, although it was removed from Favorites")
        
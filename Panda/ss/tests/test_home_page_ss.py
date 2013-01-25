'''
Created on 16.10.2012

@author: cbalea
'''
from cms.tests.station_site_cms import test_station_module_cms
from ss.pages.home_profile_login_pages_ss import HomePageSS
from ss.tests.base_ss_tests import SeleniumTestBaseNoLoginSS

class TestHomePageSS(SeleniumTestBaseNoLoginSS):
    
    def test_userSeesLocalAndNationalContentFragments(self):
        homePage = HomePageSS(self.driver, self.wait)
        mainSiteContFragments = homePage.getContentFragmentsTitle()
        homePage.clickLoginButton().login("aetn@aetn.com", "Aetnaetn")
        stationSitePage = HomePageSS(self.driver, self.wait)
        stationSiteContFragments = stationSitePage.getContentFragmentsTitle()
        self.assertTrue(stationSitePage.sublistExistsInList(mainSiteContFragments, stationSiteContFragments), "Main site content fragments not included in Station Site visible content fragments")
    
    def test_display_of_station_module(self):
        moduleTitle = test_station_module_cms.title
        subhead = test_station_module_cms.subhead
        link = test_station_module_cms.link
        imageLink = test_station_module_cms.imageLink
        
        homePage = HomePageSS(self.driver, self.wait)
        self.assertTrue(homePage.station_module_exists_by_title(moduleTitle), "Module title is not the one set in CMS")
        self.assertEqual(homePage.get_stat_mod_subhead().text, subhead, "Subhead text is not the one set in CMS")
        self.assertTrue(link in homePage.get_stat_mod_subhead().get_attribute("href"), "Link is not the one set in CMS")
        self.assertEqual(homePage.get_stat_mod_image(), imageLink, "Displayed image is not the one defined in CMS")
     
    def test_remove_station_module_from_cms(self):   
        test_station_module_cms.remove_station_module(self.driver, self.wait)
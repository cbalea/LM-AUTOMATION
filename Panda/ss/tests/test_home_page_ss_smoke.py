'''
Created on 17.01.2013

@author: cbalea
'''
from common.uua_login_page import UuaLoginPage
from ss.pages.home_profile_login_pages_ss import HomePageSS
from ss.tests.base_ss_tests import SeleniumTestBaseNoLoginSS
from utils.server_related import ServerRelated
import time

class TestHomePageSS(SeleniumTestBaseNoLoginSS):
    
    def test_featureWellDisplaysCorrectly(self):
        homePage = HomePageSS(self.driver, self.wait)
        self.assertTrue(homePage.getFeatureWellTitle()!=None, "Feature well not present")
        self.assertTrue(len(homePage.getFeatureWellSlides()) > 0, "Feature well contains no slides")
    
    def test_redirectToStationSiteAccordingToZipCode(self):
        homePage = HomePageSS(self.driver, self.wait)
        loginPage = homePage.clickLoginButton()
        loginPage.login("aetn@aetn.com", "Aetnaetn")
        time.sleep(3)
        redirectUrl = self.getAddressWithSubdomain("aetn")
        self.assertEquals(redirectUrl, self.driver.current_url, "URL not redirected when switching to station site")
    
    def test_feature_well_plays_carousel(self):
        homePage = HomePageSS(self.driver, self.wait)
        activeSlide1 = homePage.getFeatureWellSlides()[0].get_attribute("class")
        inactiveSlide1 = homePage.getFeatureWellSlides()[1].get_attribute("class")
        time.sleep(9) #wait for carousel to switch slides
        inactiveSlide2 = homePage.getFeatureWellSlides()[0].get_attribute("class")
        activeSlide2 = homePage.getFeatureWellSlides()[1].get_attribute("class")
        self.assertEqual(activeSlide1, activeSlide2, "Slide not switched")
        self.assertEqual(inactiveSlide1, inactiveSlide2, "Slide not switched")
    
    def test_footer_links_point_to_correct_pages(self):
        homePage = HomePageSS(self.driver, self.wait)
        homePage.clickOnLink("Terms of Use")
        terms_of_use_link = self.driver.current_url
        homePage.clickOnLink("Privacy Policy")
        privacy_policy_link = self.driver.current_url
        self.assertEqual(terms_of_use_link, ServerRelated().serverToBeTested()+"help/terms-of-use/", "Terms of Use link doesn't point to correct page")
        self.assertEqual(privacy_policy_link, ServerRelated().serverToBeTested()+"help/privacy-policy/", "Privacy Policy link doesn't point to correct page")
    
    def test_clicking_signup_for_free_link_dispalyes_login_popup(self):
        homePage = HomePageSS(self.driver, self.wait)
        homePage.clickOnLink("Sign up for FREE")
        uuaLoginPage = UuaLoginPage(self.driver, self.wait)
        self.assertTrue(uuaLoginPage.uua_login_page_is_displayed(), "Login pop-up not displayed!")
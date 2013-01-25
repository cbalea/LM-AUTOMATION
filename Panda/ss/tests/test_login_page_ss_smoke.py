'''
Created on 19.09.2012

@author: cbalea
'''
from ss.pages.home_profile_login_pages_ss import HomePageSS
from ss.tests.base_ss_tests import SeleniumTestBaseNoLoginSS


class TestLoginPageSS(SeleniumTestBaseNoLoginSS):
    
    def test_clicking_login_button_dispalyes_login_page(self):
        uuaLoginPage = HomePageSS(self.driver, self.wait).clickLoginButton()
        self.assertTrue(uuaLoginPage.uua_login_page_is_displayed(), "Login pop-up not displayed!")

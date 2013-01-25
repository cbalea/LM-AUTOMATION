'''
Created on 18.09.2012

@author: cbalea
'''
from cms.pages.home_page_cms import HomePageCMS
from cms.tests.base_cms_tests import SeleniumTestBaseNoLoginCMS
from utils.server_related import ServerRelated


class TestLoginPageCMS(SeleniumTestBaseNoLoginCMS):

    def test_login_into_cms(self):
        self.waitUntilLoginPerformed(ServerRelated().admin_username(), ServerRelated().admin_password(), 30)
        self.assertFalse("Log in" in self.driver.title, "Login not correct!")


#    def test_login_into_cms_via_uua(self):
#        self.login_to_cms_via_uua(self.superuser_email, self.superuser_password)
#        self.save_existing_cookies_to_files()
#        homePg = HomePageCMS(self.driver, self.wait)
#        self.assertTrue(homePg.logoutLink.is_displayed(), "Not logged in via UUA")
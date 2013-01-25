'''
Created on 31.10.2012

@author: cbalea
'''
from cms.pages.dashboard_page_cms import DashboardPageCMS
from cms.tests.base_cms_tests import SeleniumTestBaseNoLoginCMS, \
    SeleniumTestBaseCMS
from ss.pages.home_profile_login_pages_ss import HomePageSS
from utils.random_generators import RandomGenerators
from utils.server_related import ServerRelated

user = "aetn_station_admin"
email = "aetnstationadmin@aetnstationadmin.com"
password = "admin123"

contFragmentText = RandomGenerators().generateRandomString(10)
contFragm = contFragmentText

class TestUserPermissionsCMS(SeleniumTestBaseNoLoginCMS):
    
    def test_stationAdminSeesStationSiteMenuAndNoContentProjects(self):
        self.login_to_cms_via_uua(email, password)
        dashboard = DashboardPageCMS(self.driver, self.wait)
        self.assertTrue(dashboard.elementExistsByLinkText("Modify Site Design"), "Modify Site Design link not displayed")
        self.assertTrue(dashboard.elementExistsByLinkText("Modify Station Module"), "Modify Station Module link not displayed")
        self.assertFalse(dashboard.elementExistsByXpath("//li[contains(text(), 'Content Projects')]"), "Content Projects section is displayed and should not be")
    
    
    def test_stationAdminCanModifyStationModule(self):
        new_subhead = RandomGenerators().generateRandomString(10)

        self.login_to_cms_via_uua(email, password)
        dashboard = DashboardPageCMS(self.driver, self.wait)
        module = dashboard.clickModifyStationModule()
        module.clickEndOnTodayLink()
        module.typeSubhead(0, new_subhead)
        module.clickSave()
        self.driver.get(self.getAddressWithSubdomain("aetn"))
        ssHomePage = HomePageSS(self.driver, self.wait)
        ssHomePage.getContentFragmentContent()
        self.assertTrue(new_subhead in ssHomePage.getContentFragmentContent(), "Content fragment body not updated")


class TestSuperadminPermissions(SeleniumTestBaseCMS):
    
    def test_user_admin_navigates_from_af_site_to_cms(self):
        homePage = HomePageSS(self.driver, self.wait)
        homePage.clickAdminLinkInNavigationBar()
        self.assertEqual(self.driver.current_url, ServerRelated().serverToBeTested()+"admin/", "Could not navigate from AF site to CMS via Admin link")
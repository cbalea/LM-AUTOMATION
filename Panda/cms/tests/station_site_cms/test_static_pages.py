'''
Created on 11.01.2013

@author: cbalea
'''
from cms.pages.station_site_cms.static_pages_cms import StaticPagesCMS
from cms.tests.base_cms_tests import SeleniumTestBaseCMS
from ss.pages.help_page_ss import HelpPageSS
from utils.random_generators import RandomGenerators

class TestStaticPages(SeleniumTestBaseCMS):
    
    randomString = RandomGenerators().generateRandomString(5)
    text = randomString
    
    main_text = text + "-main"
    footer_text = text + "-footer"

    def add_static_page_and_go_to_help_in_ss(self, text, placeholder):
        allStatPgs = StaticPagesCMS(self.driver, self.wait)
        staticPg = allStatPgs.clickAddStaticPage()
        staticPg.typeTitle(text)
        staticPg.typeContent(text)
        staticPg.selectPlaceholder(placeholder)
        staticPg.clickSaveAndContinueEditingButton()
        ssHelpPage = HelpPageSS(self.driver, self.wait)
        return ssHelpPage

    def if_footer_page_already_exists_delete_it(self):
        ssHelpPage = HelpPageSS(self.driver, self.wait)
        if(ssHelpPage.footerExists()):
            footer_content = ssHelpPage.getFooterContent()
            allStatPgs = StaticPagesCMS(self.driver, self.wait)
            item_name = allStatPgs.getFromTableTheNameOfItemThatContainsText(footer_content)
            allStatPgs.clickCheckboxForItem(item_name)
            deletePage = allStatPgs.selectDeleteAction()
            deletePage.clickConfirmationButton()
            

    def test_add_footer_static_page(self):
        self.if_footer_page_already_exists_delete_it()
        ssHelpPage = self.add_static_page_and_go_to_help_in_ss(self.footer_text, "Footer Static Page")
        self.assertEqual(ssHelpPage.getFooterContent(), self.footer_text, "Footer is incorrectly saved")

    def test_add_main_static_page(self):
        ssHelpPage = self.add_static_page_and_go_to_help_in_ss(self.main_text, "Main Static Page")
        ssHelpPage = ssHelpPage.clickTopic(self.main_text)
        self.assertEqual(ssHelpPage.getPageTitle(), self.main_text, "Page title is incorrectly saved")
        self.assertEqual(ssHelpPage.getPageContent(), self.main_text, "Page content is incorrectly saved")
    
    def test_remove_static_pages(self):
        allStatPgs = StaticPagesCMS(self.driver, self.wait)
        allStatPgs.clickCheckboxForItem(self.main_text, "noSearch")
        allStatPgs.clickCheckboxForItem(self.footer_text, "noSearch")
        deletePage = allStatPgs.selectDeleteAction()
        newPage = deletePage.clickConfirmationButton()
        self.assertFalse(newPage.elementExistsByLinkText(self.main_text), "Static Pages not deleted")
        self.assertFalse(newPage.elementExistsByLinkText(self.footer_text), "Static Pages not deleted")
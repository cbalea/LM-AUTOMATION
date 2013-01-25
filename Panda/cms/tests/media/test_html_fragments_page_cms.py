'''
Created on Nov 9, 2012

@author: jseichei
'''
from cms.pages.media.html_fragments_page_cms import HtmlFragmentsPageCMS
from cms.tests.base_cms_tests import SeleniumTestBaseCMS
from utils.random_generators import RandomGenerators





class TestHtmlFragments(SeleniumTestBaseCMS):
    
    htmlFragmentText = RandomGenerators().generateRandomString(6)
    contentText = RandomGenerators().generateRandomString(20)
    language = "English"
    
    def test_addHtmlFragment(self):
        addHtmlFragment = HtmlFragmentsPageCMS(self.driver, self.wait)
        editHtmlFragments = addHtmlFragment.clickToAddHtmlFragmentsButton()
        editHtmlFragments.typeInNameField(self.htmlFragmentText)
        editHtmlFragments.selectLanguage("English")
        editHtmlFragments.typeInContentFields(self.contentText)
        htmlFragmentsReloadElements = editHtmlFragments.clickToHtmlFragmentSaveAndContinue()
        self.assertEqual(htmlFragmentsReloadElements.getHtmlFragmentName(), self.htmlFragmentText, "Html fragment not saved")
        self.assertEqual(htmlFragmentsReloadElements.getSelectedLanguage(), self.language, "Language not selected")
        self.assertEqual(htmlFragmentsReloadElements.getContentFieldsContext(), self.contentText, "Content text not saved")
        
        
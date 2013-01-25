'''
Created on 27.09.2012

@author: cbalea
'''

from cms.pages.station_site_cms.content_fragment_pages_cms import \
    ContentFragmentsPageCMS
from cms.tests.base_cms_tests import SeleniumTestBaseCMS
from ss.pages.home_profile_login_pages_ss import HomePageSS
from utils.random_generators import RandomGenerators
from utils.server_related import ServerRelated

class TestContentFragmentsCMS(SeleniumTestBaseCMS):
    
    contentFragmentTitle = RandomGenerators().generateRandomString(5)
    fragmentTitle = contentFragmentTitle
    
    def test_addContentFragment(self):
        lmSite = "PBS Learning Media: www"
        bodyText = "body text"
        placeholder = "Right Rail"
        
        contFragmPage = ContentFragmentsPageCMS(self.driver, self.wait)
        addContFragmPage = contFragmPage.clickAddContentFragment()
        addContFragmPage.selectLmSite(lmSite)
        addContFragmPage.typeTitle(self.fragmentTitle)
        addContFragmPage.typeBody(bodyText)
        addContFragmPage.selectStartOnTomorrow()
        addContFragmPage.selectPlaceholder(placeholder)
        editContFragmPage = addContFragmPage.clickSaveAndContinueEditingButton()
        self.assertEquals(editContFragmPage.getTitle(), self.fragmentTitle, "Title not saved correctly")
        self.assertEquals(editContFragmPage.getSelectedLmSite(), lmSite, "LM Site not selected correctly")
        self.assertEquals(editContFragmPage.getBody(), bodyText, "Body text not saved correctly")
        self.assertEquals(editContFragmPage.getSelectedPlaceholder(), placeholder, "Placeholder not saved correctly")
    
    def test_futureContentFragmentNotDisplayedInStationSite(self):
        self.driver.get(ServerRelated().serverToBeTested())
        ssHomePage = HomePageSS(self.driver, self.wait)
        self.assertFalse(ssHomePage.contentFragmentExistsByTitle(self.fragmentTitle))
    
    def test_removeContentFragment(self):
        contFragmPage = ContentFragmentsPageCMS(self.driver, self.wait)
        contFragmPage.clickCheckboxForItem(self.fragmentTitle)
        deletePage = contFragmPage.selectDeleteAction()
        newPage = deletePage.clickConfirmationButton()
        self.assertFalse(newPage.elementExistsByLinkText(self.fragmentTitle), "Content Fragment not deleted")

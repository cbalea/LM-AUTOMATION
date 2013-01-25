'''
Created on 27.09.2012

@author: cbalea
'''
from cms.pages.home_page_cms import HomePageCMS
from cms.tests.base_cms_tests import SeleniumTestBaseCMS
from utils.random_generators import RandomGenerators
from utils.server_related import ServerRelated

class TestLmSitesCMS(SeleniumTestBaseCMS):
    
    lmSiteName = RandomGenerators().generateRandomString(5)
    lmSite = lmSiteName
    headerFilePath = "fixtures/desert.png"
    
    
#    def test_addLmSite(self):
#        county = "Salinas"
#        
#        homePage = HomePageCMS(self.driver, self.wait)
#        lmSitesPage = homePage.clickLmSitesLink()
#        addLmSitePage = lmSitesPage.clickAddLmSiteButton()
#        addLmSitePage.typeName(self.lmSite)
#        addLmSitePage.typeSubdomain(self.lmSite)
#        addLmSitePage.clickDefaultLmSiteCheckbox()
#        addLmSitePage.typeInCountySearch(county)
#        addLmSitePage.selectFirstCountyFromSuggestions()
#        print "hidden field: " + self.driver.find_element_by_xpath("//input[contains(@name, 'lmsite_county_id')]").get_attribute("value")
#        editLmSitePage = addLmSitePage.clickSaveAndContinueEditingButton()
#        self.assertEquals(editLmSitePage.getName(), self.lmSite, "LM Site name not added correctly")
#        self.assertEquals(editLmSitePage.getSubdomain(), self.lmSite, "LM Site subdomain not added correctly")
#        self.assertTrue(editLmSitePage.isDefaultLmSiteChecked(), "Default lm site checkbox not checked.")


    def test_previewLmSite(self):
        homePage = HomePageCMS(self.driver, self.wait)
        lmSitesPage = homePage.clickLmSitesLink()
        sitePage = lmSitesPage.openLmSiteByIndex(2)
        sitePage.clickPreviewButton()
        sitePage.switchToNewestWindow()
        title = self.wait.until(lambda driver : driver.find_element_by_xpath("//title"))
        self.assertTrue("PBS LearningMedia" in title.text, "Preview window not opened!")
    
    
#    def test_removeLmSite(self):
#        homePage = HomePageCMS(self.driver, self.wait)
#        lmSitesPage = homePage.clickLmSitesLink()
#        lmSitesPage.clickCheckboxForItem(self.lmSite)
#        deletePage = lmSitesPage.selectDeleteAction()
#        newPage = deletePage.clickConfirmationButton()
#        self.assertFalse(newPage.elementExistsByLinkText(self.lmSite), "LM Site not deleted")
    
    
    def test_setMainSiteAsDefaultLmSiteAndTypeWellcomeText(self):
        homePage = HomePageCMS(self.driver, self.wait)
        lmSitesPage = homePage.clickLmSitesLink()
        editLmSitePage = lmSitesPage.openLmSiteByName("PBS Learning Media")
        editLmSitePage.clickDefaultLmSiteCheckbox()
        wellcomeText = "Welcome to PBS Learning Media home site!"
        editLmSitePage.typeWellcomeText(wellcomeText)
        editLmSitePage = editLmSitePage.clickSaveAndContinueEditingButton()
        self.assertTrue(editLmSitePage.isDefaultLmSiteChecked(), "Default lm site checkbox not checked.")
        self.assertEquals(editLmSitePage.getWellcomeText(), wellcomeText, "Wellcome text not saved.")
    
    
    def test_setCustomHeaderImageToStationSite(self):
        homePage = HomePageCMS(self.driver, self.wait)
        lmSitesPage = homePage.clickLmSitesLink()
        editLmSitePage = lmSitesPage.openLmSiteByName("AETN Learning Media")
        editLmSitePage.typeHeaderFilePath(ServerRelated().getFilePathInProjectFolder(self.headerFilePath))
        editLmSitePage = editLmSitePage.clickSaveAndContinueEditingButton()
        self.assertEquals(editLmSitePage.getCurrentHeaderImage(), "station_site/lmsite_headers/desert.png", "Station site header not added correctly")
            
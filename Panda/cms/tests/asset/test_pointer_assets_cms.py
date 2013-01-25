'''
Created on 22.01.2013

@author: cbalea
'''
from cms.pages.asset.assets_pages_cms import AddEditAssetPageCMS
from cms.tests.base_cms_tests import SeleniumTestBaseCMS
from utils.random_generators import RandomGenerators

assetTitle = RandomGenerators().generateRandomString(5)
asset = assetTitle
externalLink = "http://serc.carleton.edu/images/eslabs/drought/hoover_dam.jpg"
externalTranscript = "http://wordpress.org/extend/plugins/about/readme.txt"

class TestPointerAssetsCMS(SeleniumTestBaseCMS):
    
    def test_add_pointer_asset(self):
        addAssetPage = AddEditAssetPageCMS(self.driver, self.wait, "loadFromUrl")
        addAssetPage.selectContentProjectAssetByIndex(1)
        addAssetPage.typeTitle(asset)
        addAssetPage.selectTypeByLabel("Pointer")
        addAssetPage = addAssetPage.clickToSaveAndContinueButton()
        addAssetPage.clickShowHideLinkForField("Media File & Transcript")
        addAssetPage.typeExternalLink(externalLink)
        addAssetPage.typeExternalTranscript(externalTranscript)
        addAssetPage = addAssetPage.clickToSaveAndContinueButton()
        addAssetPage.clickShowHideLinkForField("Media File & Transcript")
        self.assertEqual(addAssetPage.getExternalLink(), externalLink, "External link not saved")
        self.assertEqual(addAssetPage.getExternalTranscript(), externalTranscript, "External transcript not saved")
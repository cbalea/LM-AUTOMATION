
'''
Created on Sep 25, 2012

@author: jseichei
'''

from cms.pages.asset.assets_pages_cms import AddEditAssetPageCMS, AssetsPageCMS
from cms.tests.base_cms_tests import SeleniumTestBaseCMS
from utils.random_generators import RandomGenerators
from utils.server_related import ServerRelated
    



class TestRegularAssetsCMS(SeleniumTestBaseCMS):
    
    assetText =  RandomGenerators().generateRandomString(10)
    text = assetText
    assetTitle = RandomGenerators().generateRandomString(5)
    asset = assetTitle
    posterImagePath = "fixtures/image_sample.jpg" 
    audioFilePath = "fixtures/audio_sample.wav"
    
    
    
    def test__addAssetPage1(self):
        self.driver.get(ServerRelated().serverToBeTested() + "admin/cms/asset/add/")
        addAsset = AddEditAssetPageCMS(self.driver, self.wait)
        addAsset.selectContentProjectAssetByIndex(1)
        addAsset.typeTitle(self.asset)
        reloadelement = addAsset.clickToSaveButton()
        self.assertEqual(reloadelement.getTitleAsset(), self.asset, "Asset not added ")
        
    
    def test__addAssetPage2(self):
        self.driver.get(ServerRelated().serverToBeTested() + "admin/cms/asset")
        allAssetsPg = AssetsPageCMS(self.driver, self.wait)
        assetPage = allAssetsPg.clickOnAsset(self.asset)
        assetPage.completeAttribution("Funder", self.text)
        assetPage.addMediaByText("a")
        assetPage.clickShowHideLinkForField("Metadata")
        assetPage.addPosterImage(ServerRelated().getFilePathInProjectFolder(self.posterImagePath)) 
        assetPage = assetPage.clickToSaveAndContinueButton()
        assetPage.clickToHideShowAttribution()
        assetPage.clickShowHideLinkForField("Metadata")
        self.assertTrue(assetPage.getMediaObjectType(), "Asset Media object not added")
        self.assertEqual(assetPage.getAttributionRole(), "Funder", "Attribution role not saved")
        self.assertTrue("image_sample.jpg" in assetPage.getPosterImage(), "Poster image not saved")
        
    
    def test_clickSaveButtonThreeTimesKeepsAttributions(self):
        self.driver.get(ServerRelated().serverToBeTested() + "admin/cms/asset")
        assetsPage = AssetsPageCMS(self.driver, self.wait)
        asset = assetsPage.clickOnAsset(self.asset)
        asset = asset.clickToSaveAndContinueButton()
        asset = asset.clickToSaveAndContinueButton()
        asset = asset.clickToSaveAndContinueButton()
        asset.clickToHideShowAttribution()
        self.assertEqual(asset.getAttributionRole(), "Funder", "Attribution role was lost while saving")
        
    
    def test__editAssetPage(self):
        self.driver.get(ServerRelated().serverToBeTested() + "admin/cms/asset")
        allAssetsPg = AssetsPageCMS(self.driver, self.wait)
        assetPage = allAssetsPg.clickOnAsset(self.asset)
        assetPage.completeMetadaFields(self.text, self.text)   
        assetPage.completeOwnershipAndRights(self.text)
        assetPage.completeAdditionalMetadata(self.text, self.text)
        assetPage = assetPage.clickToSaveAndContinueButton()
        assetPage.clickToShowHideAssetBoxes()
        self.assertEqual(assetPage.getAttributionRole(), "Funder", "Attribution role not saved")
        self.assertTrue("image_sample.jpg" in assetPage.getPosterImage(), "Poster image not saved")
        self.assertTrue(assetPage.getMediaObjectType(), "Asset Media object not added")
        self.assertEqual(assetPage.getDescriptionBoxMetadata(), self.text, "No description saved")
        self.assertEqual(assetPage.getAssetType(), self.text, "No asset type added")
        self.assertEqual(assetPage.getMediaTypeGeneral(), "Video", "No media type general selected")
        self.assertEqual(assetPage.getMediaTypeSpecific(), "Real or Animated Demo or Visualization", "No media type specific selected")
        self.assertTrue(assetPage.getAccessibilityIndicatorsAccessModesAuditory(), "Auditory not selected")
        self.assertTrue(assetPage.getAccessibilityIndicatorsControlFlexibilityFullKeyboardControl(), "Full Keyboard Control Not selected")
        self.assertEqual(assetPage.getRightsDistribution(), "Commercial", "Rights distribution not selected")
        self.assertEqual(assetPage.getRightsSummary(), "Stream, Download and Share", "Rights summary not selected")
        self.assertEqual(assetPage.getContentFlagsDescription(), self.text, "Content flags description not saved")
        
        
    def test__saveAsToCloningAsset(self):
        self.driver.get(ServerRelated().serverToBeTested() + "admin/cms/asset")
        allAssetsPg = AssetsPageCMS(self.driver, self.wait)
        assetPg = allAssetsPg.clickOnAsset(self.asset)
        valueOfOldAssetCode = assetPg.getAssetCodeValue()
        clone = assetPg.clickToSaveAsButton()
        clone.waitUntilIsCloned(valueOfOldAssetCode)
        clone.clickToShowHideAssetBoxes()
        self.assertFalse(clone.getMediaObjectType(), "Asset Media object not added")
        self.assertEqual(clone.getAttributionRole(), "Funder", "Attribution role not saved")
        self.assertTrue("image_sample.jpg" in clone.getPosterImage(), "Poster image not saved")
        self.assertEqual(clone.getDescriptionBoxMetadata(), self.text, "No description saved")
        self.assertEqual(clone.getAssetType(), self.text, "No asset type added")
        self.assertEqual(clone.getMediaTypeGeneral(), "Video", "No media type general selected")
        self.assertEqual(clone.getMediaTypeSpecific(), "Real or Animated Demo or Visualization", "No media type specific selected")
        self.assertTrue(clone.getAccessibilityIndicatorsAccessModesAuditory(), "Auditory not selected")
        self.assertTrue(clone.getAccessibilityIndicatorsControlFlexibilityFullKeyboardControl(), "Full Keyboard Control Not selected")
        self.assertEqual(clone.getRightsDistribution(), "Commercial", "Rights distribution not selected")
        self.assertEqual(clone.getRightsSummary(), "Stream, Download and Share", "Rights summary not selected")
        self.assertEqual(clone.getContentFlagsDescription(), self.text, "Content flags description not saved")

    
    def test_mediaTypeGeneralAutomaticallyCalculated(self):
        self.driver.get(ServerRelated().serverToBeTested() + "admin/cms/asset/add/")
        addAssetPg = AddEditAssetPageCMS(self.driver, self.wait)
        addAssetPg.selectContentProjectAssetByIndex(1)
        addAssetPg.typeTitle("%s1" %self.asset)
        editAssetPg = addAssetPg.clickToSaveAndContinueButton()
        addMediaPg = editAssetPg.clickAddMediaButton()
        addMediaPg.typeName(self.asset)
        addMediaPg.typeFilePath(ServerRelated().getFilePathInProjectFolder(self.audioFilePath))
        addMediaPg.clickSaveButton()
        self.driver.close()
        addMediaPg.switchToNewestWindow()
        self.driver.refresh()
        editAssetPg = AddEditAssetPageCMS(self.driver, self.wait)
        editAssetPg.addMediaByText(self.asset)
        editAssetPg.clickIsPrimaryMedia()
        editAssetPg = editAssetPg.clickToSaveAndContinueButton()
        editAssetPg.clickShowHideLinkForField("Metadata")
        self.assertEqual(editAssetPg.getMediaTypeGeneral(), "Audio", "Media type general not automatically calculated")
    
    
    def test_media_can_be_removed_from_asset(self):
        self.driver.get(ServerRelated().serverToBeTested() + "admin/cms/asset/")
        all_assets_page = AssetsPageCMS(self.driver, self.wait)
        assetPage = all_assets_page.clickAssetByIndex(1)
        original_media_list = assetPage.getListOfAttachedMedias()
        assetPage.addMediaByText("a")
        assetPage = assetPage.clickToSaveAndContinueButton()
        intermediate_media_list = assetPage.getListOfAttachedMedias()
        last_added_media_name = "".join(list(set(intermediate_media_list) - set(original_media_list)))
        assetPage.clickDeleteMediaCheckboxByMediaName(last_added_media_name)
        assetPage = assetPage.clickToSaveAndContinueButton()
        final_media_list = assetPage.getListOfAttachedMedias()
        self.assertEquals(original_media_list, final_media_list, "The newly added media was not removed form asset")


    def test_removeAsset(self):
        self.driver.get(ServerRelated().serverToBeTested() + "admin/cms/asset")
        assetsPage = AssetsPageCMS(self.driver, self.wait)
        assetsPage.clickCheckboxForItem(self.asset)
        deletePage = assetsPage.selectDeleteAction()
        newPage = deletePage.clickConfirmationButton()
        self.assertFalse(newPage.elementExistsByLinkText(self.asset), "Asset not deleted")
        
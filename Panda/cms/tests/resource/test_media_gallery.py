#'''
#Created on 14.11.2012
#
#@author: cbalea
#'''
#from cms.pages.resource.resources_pages_cms import EditAddResourcePageCMS, \
#    ResourcesPagesCMS
#from cms.tests.base_cms_tests import SeleniumTestBaseCMS
#from utils.random_generators import RandomGenerators
#from utils.server_related import ServerRelated
#
#class TestMediaGalleryCMS(SeleniumTestBaseCMS):
#    
#    resourceName = RandomGenerators().generateRandomString(5)
#    resource = resourceName
#    
#    def test_addMediaGalleryResource(self):
#        res_type = "Media Gallery"
#    
#        self.driver.get(ServerRelated().serverToBeTested() + "/admin/cms/resource/add/")
#        addResourcePage = EditAddResourcePageCMS(self.driver, self.wait)
#        addResourcePage.typeTitle(self.resource)
#        addResourcePage.selectContentProjectByIndex(1)
#        addResourcePage.selectType(res_type)
#        editResourcePage = addResourcePage.clickSaveAndContinueEditingButton()
#        editResourcePage.showHidePrimaryAssets()
#        assetSelectPage = editResourcePage.searchForAsset("a")
#        assetSelectPage.clickCheckboxByIndex(1)
#        assetSelectPage.clickCheckboxByIndex(2)
#        editResourcePage = assetSelectPage.clickAddAssetButton()
#        editResourcePage = editResourcePage.clickSaveAndContinueEditingButton()
#        editResourcePage.showHidePrimaryAssets()
#        editResourcePage.setAssetOrder(1, 1)
#        editResourcePage.setAssetOrder(2, 0)
#        editResourcePage = editResourcePage.clickSaveAndContinueEditingButton()
#        editResourcePage.showHidePrimaryAssets()
#        self.assertEquals(editResourcePage.getSelectedType(), res_type, "Media Gallery type not selected")
#        self.assertEquals(editResourcePage.getAssetOrder(1), "0", "Asset order not correctly saved")
#        self.assertEquals(editResourcePage.getAssetOrder(2), "1", "Asset order not correctly saved")
#        
#    def test_removeMediaGallery(self):
#        resourcesPage = ResourcesPagesCMS(self.driver, self.wait)
#        resourcesPage.clickCheckboxForItem(self.resource)
#        deletePage = resourcesPage.selectDeleteAction()
#        newPage = deletePage.clickConfirmationButton()
#        self.assertFalse(newPage.elementExistsByLinkText(self.resource), "Resource not deleted")
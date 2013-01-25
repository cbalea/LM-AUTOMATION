# -*- coding: utf-8 -*-

'''
Created on 24.09.2012

@author: cbalea
'''


from cms.pages.asset.add_asset import AddAssetPageCMS
from cms.pages.resource.resources_pages_cms import ResourcesPagesCMS, \
    EditAddResourcePageCMS
from cms.tests.base_cms_tests import SeleniumTestBaseCMS
from ss.pages.resource_view_page_ss import ResourceViewPageSS
from utils.random_generators import RandomGenerators
from utils.server_related import ServerRelated


class TestResourcesPagesCMS(SeleniumTestBaseCMS):
    
    resourceName = RandomGenerators().generateRandomString(5)
    resource = resourceName
    
    def navigateToCHNode(self, editResourcePage):
        editResourcePage.clickCHExpandLink()
        editResourcePage.selectCHNodesRoot("English Language Arts and Literacy")
        editResourcePage.clickCHTreeExpanderByLabel("English Language Arts and Literacy")
        editResourcePage.clickCHTreeExpanderByLabel("Speaking and Listening")
        editResourcePage.clickCHTreeExpanderByLabel("Presentation of Knowledge and Ideas")
        editResourcePage.clickCHTreeExpanderByLabel("Presenting Information")

    def openResource(self):
        resourcesPage = ResourcesPagesCMS(self.driver, self.wait)
        editResourcePage = resourcesPage.clickOnResource(self.resource)
        return editResourcePage


    def add_resource_with_title(self, title):
        self.driver.get(ServerRelated().serverToBeTested() + "/admin/cms/resource/add/")
        addResourcePage = EditAddResourcePageCMS(self.driver, self.wait)
        addResourcePage.typeTitle(title)
        addResourcePage.selectContentProjectByIndex(1)
        editResourcePage = addResourcePage.clickSaveButton()
        return editResourcePage

   
    
    
    def test_addResource(self):
        editResourcePage = self.add_resource_with_title(self.resource)
        self.assertEqual(editResourcePage.getTitle(), self.resource, "Resource not added correctly")


    def test_addSupportMaterials(self):
        editResourcePage = self.openResource()
        editResourcePage.clickShowSupportMaterialsLink()
        htmlFragment = editResourcePage.clickAddBackgroundEssayButton()
        htmlFragment.typeInNameField(self.resource)
        htmlFragment.typeInContentFields(self.resource)
        htmlFragment.selectFragmentType("Background Essay")
        htmlFragment.clickSave()
        htmlFragment.switchToNewestWindow()
        editResourcePage = EditAddResourcePageCMS(self.driver, self.wait)
        editResourcePage = editResourcePage.clickSaveAndContinueEditingButton()
        editResourcePage.clickShowSupportMaterialsLink()
        self.assertTrue(editResourcePage.isBackgroundEssayAttached(self.resource), "Support material not added!")


    def test_defineCHNodeForResource(self):
        node = "People, Places, Things, and Events (Grade K)"
#        state = "Georgia"

        editResourcePage = self.openResource()
        self.navigateToCHNode(editResourcePage)
        editResourcePage.clickCHCheckboxByLabel(node)
        editResourcePage.clickAddButton()
        editResourcePage = editResourcePage.clickSaveAndContinueEditingButton()
        self.navigateToCHNode(editResourcePage)
#        editResourcePage.selectStandardsAlignmentState(state)
        self.assertTrue(editResourcePage.getCHCheckboxStatusByLabel(node), "Checkbox not checked")
        self.assertEquals(editResourcePage.getCHAttachedNode(), "People, Places, Things, and Events (Grade K) English Language Arts and Literacy > Speaking and Listening > Presentation of Knowledge and Ideas > Presenting Information", "Attached node not displayed in table")
#        self.assertEquals(editResourcePage.getNumberOfAttachedStandards(), 1, "Number of attached standards is not correct")
    
    
    def test_definablePDCHNodes(self):
        root = "Professional Development"
        
        editResourcePage = self.openResource()
        editResourcePage.clickCHExpandLink()
        editResourcePage.selectCHNodesRoot(root)
        editResourcePage.clickCHTreeExpanderByLabel(root)
        editResourcePage.clickCHTreeExpanderByLabel("Planning & Preparation")
        editResourcePage.clickCHTreeExpanderByLabel("The Brain & Learning")
        editResourcePage.clickCHCheckboxByLabel("Achievement Gap")
        editResourcePage.clickAddButton()
        editResourcePage = editResourcePage.clickSaveAndContinueEditingButton()
        editResourcePage.clickCHExpandLink()
        self.assertEquals(editResourcePage.getCHAttachedNode(), "Achievement Gap Professional Development > Planning & Preparation > The Brain & Learning", "Attached node not displayed in table")

        
    def test_removeResource(self):
        resourcesPage = ResourcesPagesCMS(self.driver, self.wait)
        resourcesPage.clickCheckboxForItem(self.resource)
        deletePage = resourcesPage.selectDeleteAction()
        newPage = deletePage.clickConfirmationButton()
        self.assertFalse(newPage.elementExistsByLinkText(self.resource), "Resource not deleted")
    
    
    def test_resourceAccessingViaPerssistentUrl(self):
        resourcesPage = ResourcesPagesCMS(self.driver, self.wait)
        resourcesPage.search_in_searchbar("The Israeli Palestinian Conflict")
        resourcesPage.clickOnLink("The Israeli Palestinian Conflict")
        res = EditAddResourcePageCMS(self.driver, self.wait)
        code = res.getResourceCode()
        slug = res.getResourceSlug()
        title = res.getTitle()
        resView = ResourceViewPageSS(self.driver, self.wait, "%s/%s" %(code, slug))
        self.assertEquals(resView.getTitle(), title, "Perssistent url didn't open the correct resource in audience facing site")
    
    
    def test_setting_asset_with_nonascii_carachter_to_resource(self):
        assetTitle = u"%sInspiration® Basics" %self.resource
        
        self.driver.get(ServerRelated().serverToBeTested() + "admin/cms/asset/add/")
        addAssetPg = AddAssetPageCMS(self.driver, self.wait)
        addAssetPg.selectContentProjectAsset()
        addAssetPg.typeTitle(assetTitle)
        addAssetPg.clickSave()
        editResourcePage = self.add_resource_with_title(self.resource)
        editResourcePage.showHidePrimaryAsset()
        assetSelectPage = editResourcePage.searchForAsset(assetTitle)
        assetSelectPage.clickCheckboxByIndex(1)
        editResourcePage = assetSelectPage.clickAddAssetButton()
        editResourcePage = editResourcePage.clickSaveAndContinueEditingButton()
        editResourcePage.showHidePrimaryAsset()
        self.assertTrue(assetTitle in editResourcePage.getPrimaryAssetSectionContent(), "Asset with non-ascii carachter not attached / Saving crashed with an error")
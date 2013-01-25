'''
Created on 19.11.2012

@author: cbalea
'''
from cms.pages.collections_pages_cms import CollectionsPage, \
    EditCollectionPageCMS
from cms.tests.base_cms_tests import SeleniumTestBaseCMS
from ss.pages.collection_view_page_ss import CollectionViewPageSS
from utils.random_generators import RandomGenerators
from utils.selenium_test_base import SeleniumTestBase
from utils.server_related import ServerRelated

collName = "collection1-2-3"
credits = "Credits to PBS."
longDescr = "long description"
bannerImage = "banner_1170_150.jpg"


def removeCollection(driver, wait):
#   this function will be triggered after the view-collection tests will be ran in TestCollectionsSS 
    driver.get(ServerRelated().serverToBeTested()+"/admin/")
    SeleniumTestBase().login_to_cms_via_uua(SeleniumTestBase().superuser_email, SeleniumTestBase().superuser_password)
    collsPage = CollectionsPage(driver, wait)
    collsPage.clickCheckboxForItem(collName)
    deletePage = collsPage.selectDeleteAction()
    newPage = deletePage.clickConfirmationButton()
    assert not(newPage.elementExistsByLinkText(collName)), "Collection not deleted"

def updated_collection_url_maps_to_correct_page(driver, wait):
    driver.get(ServerRelated().serverToBeTested()+"/admin/")
    SeleniumTestBase().login_to_cms_via_uua(SeleniumTestBase().superuser_email, SeleniumTestBase().superuser_password)
    collsPage = CollectionsPage(driver, wait)
    collection = collsPage.openCollection(collName)
    colUrl = RandomGenerators().generateRandomString(5)
    collection.typeUrl(colUrl)
    collection = collection.clickSaveAndContinueEditingButton()
    driver.get(ServerRelated().serverToBeTested() + "collection/%s" %collection.getUrl())
    collectionView = CollectionViewPageSS(driver, wait)
    assert bannerImage in collectionView.getBannerImage(), "Collection display page not opened"



class TestCollectionsCMS(SeleniumTestBaseCMS):
    
    def test_addCollection(self):
        template = "Single Collection"
        
        collsPage = CollectionsPage(self.driver, self.wait)
        collection = collsPage.clickAddCollection()
        collection.typeTitle(collName)
        collection.selectCollectionTemplate(template)
        collection = collection.clickSaveAndContinueEditingButton()
        self.assertTrue( ('"%s" was added successfully' %collName) in collection.getSuccessfullyEditMessage(), "Collection not added")
        self.assertEqual(collection.getTitle(), collName, "Title not added")
        self.assertEqual(collection.getUrl(), collName, "URL not added")
        self.assertEqual(collection.getSelectedCollectionTemplate(), template, "Collection Template not added")
    
    
    def test_editCollectionMetadata(self):
        shortDescr = "short description"
        keywords = "keyword1, keyword2"
        
        collsPage = CollectionsPage(self.driver, self.wait)
        collection = collsPage.openCollection(collName)
        collection.clickExpandLinkFor("Metadata")
        collection.typeShortDescription(shortDescr)
        collection.typeLongDescription(longDescr)
        collection.typeKeywords(keywords)
        collection.clickCategoryCheckbox(0)
        collection.clickCategoryCheckbox(2)
        collection.clickSubjectCheckbox(0)
        collection.clickSubjectCheckbox(3)
        collection = collection.clickSaveAndContinueEditingButton()
        collection.clickExpandLinkFor("Metadata")
        categoryBoxes = collection.getClickedCategoryCheckboxes()
        subjectBoxes = collection.getClickedSubjectCheckboxes()
        self.assertEqual(collection.getShortDescription(), shortDescr, "Short description not added")
        self.assertEqual(collection.getLongDescription(), longDescr, "Long description not added")
        self.assertEqual(collection.getKeywords(), keywords, "Keywords not added")
        self.assertTrue( (0 in categoryBoxes) and (2 in categoryBoxes), "Category checkboxes not checked")
        self.assertTrue( (0 in subjectBoxes) and (3 in subjectBoxes), "Subject checkboxes not checked")
        
        
    def test_editCollectionRelatedResources(self):
        collsPage = CollectionsPage(self.driver, self.wait)
        collection = collsPage.openCollection(collName)
        collection.clickExpandLinkFor("Related Resources")
        
        resPage = collection.searchForResource("a")
        resPage.clickCheckboxByIndex(1)
        resPage.clickCheckboxByIndex(2)
        resPage.selectAddResourcesToCollection()
        collection = EditCollectionPageCMS(self.driver, self.wait)
        
        collection = collection.clickSaveAndContinueEditingButton()
        collection.clickExpandLinkFor("Related Resources")
        collection.typeInOrderBoxWithIndex(0, 1)
        collection.typeInOrderBoxWithIndex(1, 2)
        collection = collection.clickSaveAndContinueEditingButton()
        collection.clickExpandLinkFor("Related Resources")
        self.assertEqual(collection.getNumberOfAttachedResources(), 2, "Not all resources attached")
        self.assertEqual(collection.getResourceOrderNumber(0), "1", "Order not correctly set")
        self.assertEqual(collection.getResourceOrderNumber(1), "2", "Order not correctly set")
    
    
    def test_editCollectionGraphics(self):
        thumbnailFilePath = "fixtures/thumbnail_90_90.jpg"
        bannerFilePath = "fixtures/" + bannerImage
        
        collsPage = CollectionsPage(self.driver, self.wait)
        collection = collsPage.openCollection(collName)
        collection.clickExpandLinkFor("Collection Graphics")
        collection.typeThumbnailFilePath(ServerRelated().getFilePathInProjectFolder(thumbnailFilePath))
        collection.typeBannerFilePath(ServerRelated().getFilePathInProjectFolder(bannerFilePath))
        collection = collection.clickSaveAndContinueEditingButton()
        collection.clickExpandLinkFor("Collection Graphics")
        self.assertEqual(collection.getCurrentThumbnail(), "collections/thumbnail_90_90.jpg", "Thumbnail is not attached")
        self.assertEqual(collection.getCurrentBanner(), "collections/"+bannerImage, "Banner is not attached")
        
        
    def test_editCollectionAttributions(self):
        role = "Funder"
        text = "text"
        
        collsPage = CollectionsPage(self.driver, self.wait)
        collection = collsPage.openCollection(collName)
        collection.clickExpandLinkFor("Attributions")
        collection.selectRoleByVisibleText(role)
        collection.selectEntityByIndex(2)
        collection.typeAttributionsText(text)
        collection = collection.clickSaveAndContinueEditingButton()
        collection.clickExpandLinkFor("Attributions")
        self.assertEqual(collection.getSelectedRole(), role, "Role not added")
        self.assertTrue(collection.getSelectedEntity()!=None, "Entity not added")
        self.assertEqual(collection.getAttributionsText(), text, "Attributions text not added")

    
    def test_editCollectionCredits(self):
        collsPage = CollectionsPage(self.driver, self.wait)
        collection = collsPage.openCollection(collName)
        collection.clickExpandLinkFor("Collection Credit")
        collection.typeCredits(credits)
        collection = collection.clickSaveAndContinueEditingButton()
        collection.clickExpandLinkFor("Collection Credit")
        self.assertEqual(collection.getCredits(), credits, "Credits text not added")



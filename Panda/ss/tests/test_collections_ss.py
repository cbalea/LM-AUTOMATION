'''
Created on 27.11.2012

@author: cbalea
'''
from cms.tests import test_collections_cms
from ss.pages.collection_view_page_ss import CollectionViewPageSS
from ss.tests.base_ss_tests import SeleniumTestBaseNoLoginSS

class TestCollectionsSS(SeleniumTestBaseNoLoginSS):
    
    collectionCode = test_collections_cms.collName
    
    def test_collection_display_page(self):
        collectionCredits = test_collections_cms.credits
        description = test_collections_cms.longDescr
        banner = test_collections_cms.bannerImage
        
        collection = CollectionViewPageSS(self.driver, self.wait, self.collectionCode)
        self.assertTrue(banner in collection.getBannerImage(), "Banner immage not displayed")
        self.assertEqual(collection.getNumberOfResources(), 2, "Resources not displayed")
        self.assertEqual(collection.getCredits(), collectionCredits, "Credits not displayed correctly")
        self.assertEqual(collection.getDescription(), description, "Description not displayed correctly")
        self.assertEqual(self.driver.title, self.collectionCode + " : PBS LearningMedia", "HTML title is incorrect")
        
        
    def test_clicking_collection_resource_opens_view_page(self):
        collection = CollectionViewPageSS(self.driver, self.wait, self.collectionCode)
        resourceName = collection.getResourceName(0)
        resource = collection.clickResource(0)
        self.assertEqual(resource.getTitle(), resourceName, "Resource not opened correctly")
        
    def test_updated_collection_url_maps_to_correct_page(self):
        test_collections_cms.updated_collection_url_maps_to_correct_page(self.driver, self.wait)
        
    def test_remove_collection_from_cms(self):
        test_collections_cms.removeCollection(self.driver, self.wait)
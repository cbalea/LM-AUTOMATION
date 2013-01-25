'''
Created on 16.10.2012

@author: cbalea
'''

from cms.pages.station_site_cms.feature_well_pages_cms import \
    FeatureWellsPageCMS
from cms.tests.base_cms_tests import SeleniumTestBaseCMS


class TestFeatureWellsCMS(SeleniumTestBaseCMS):
    
    def test_feature_well_content(self):
        featureWellsPage = FeatureWellsPageCMS(self.driver, self.wait)
        featureWelEditPage = featureWellsPage.clickFeatureWellByIndex(1)
        original_number_of_items = len(featureWelEditPage.getAttachedFeatureWellItems())
        featureWelEditPage.selectNewItemByIndex(2)
        featureWelEditPage = featureWelEditPage.clickSaveAndContinueEditingButton()
        final_number_of_items = len(featureWelEditPage.getAttachedFeatureWellItems())
        self.assertEqual(final_number_of_items, original_number_of_items+1, "New item not added!")        
    
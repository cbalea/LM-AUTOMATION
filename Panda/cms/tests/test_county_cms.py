'''
Created on 14.11.2012

@author: cbalea
'''
from cms.pages.county_pages_cms import CountiesPageCMS
from cms.tests.base_cms_tests import SeleniumTestBaseCMS

class TestCountyCMS(SeleniumTestBaseCMS):
    
    def test_savingCountyWorks(self):
        countiesPage = CountiesPageCMS(self.driver, self.wait)
        editCountyPg = countiesPage.clickCountyByIndex(1)
        countiesPage = editCountyPg.clickSaveButton()
        self.assertTrue(countiesPage.getNumberOfDisplayedCounties()!=0, "Counties not displayed")
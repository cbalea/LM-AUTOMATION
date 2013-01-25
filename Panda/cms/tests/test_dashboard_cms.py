'''
Created on 09.10.2012

@author: cbalea
'''
from cms.pages.dashboard_page_cms import DashboardPageCMS
from cms.tests.base_cms_tests import SeleniumTestBaseCMS


class TestDashboardCMS(SeleniumTestBaseCMS):
    
    def test_uploadMediaFromDashboard(self):
        dashboard = DashboardPageCMS(self.driver, self.wait)
        dashboard.selectUploadMediaByText("Audio")
        self.assertTrue(self.wait.until(lambda driver : driver.find_element_by_xpath("//h1[text()='Add audio media']"))!=None, 
                        "Audio upload form not opened")
        
        dashboard = DashboardPageCMS(self.driver, self.wait)
        dashboard.selectUploadMediaByText("Video")
        self.assertTrue(self.wait.until(lambda driver : driver.find_element_by_xpath("//h1[text()='Add video media']"))!=None, 
                        "Video upload form not opened")
        
        dashboard = DashboardPageCMS(self.driver, self.wait)
        dashboard.selectUploadMediaByText("Image")
        self.assertTrue(self.wait.until(lambda driver : driver.find_element_by_xpath("//h1[text()='Add image media']"))!=None, 
                        "Image upload form not opened")
        
        dashboard = DashboardPageCMS(self.driver, self.wait)
        dashboard.selectUploadMediaByText("Document")
        self.assertTrue(self.wait.until(lambda driver : driver.find_element_by_xpath("//h1[text()='Add document media']"))!=None, 
                        "Document upload form not opened")
        
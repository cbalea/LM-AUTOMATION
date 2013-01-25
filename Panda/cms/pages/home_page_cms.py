'''
Created on 20.09.2012

@author: cbalea
'''
from cms.pages.content_project_pages_cms import ContentProjectsPageCMS
from cms.pages.media.video_pages_cms import VideosPageCMS
from cms.pages.station_site_cms.lm_site_pages_cms import LMSitesPageCMS


class HomePageCMS(object):

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.logoutLink = self.wait.until(lambda driver : driver.find_element_by_xpath("//a[contains(text(),'Log out')]"))

    def clickVideosLink(self):
        self.videosLink = self.wait.until(lambda driver : driver.find_element_by_xpath("//li/a[text()='Videos']"))
        self.videosLink.click()
        return VideosPageCMS(self.driver, self.wait)
    
    def clickLmSitesLink(self):
        self.lmSitesLink = self.wait.until(lambda driver : driver.find_element_by_xpath("//li/a[text()='Lm sites']"))
        self.lmSitesLink.click()
        return LMSitesPageCMS(self.driver, self.wait)

    def clickContentProjectLink(self):
        self.contentProjectLink = self.wait.until(lambda driver : driver.find_element_by_xpath("//li/a[text()='Content projects']"))
        self.contentProjectLink.click()
        return ContentProjectsPageCMS(self.driver, self.wait)
    
    def getContentProjectsListedInLeftSideBar(self):
        contProjElements = self.wait.until(lambda driver : driver.find_elements_by_xpath("//li[contains(text(),'Content Projects')]/ul/li/a"))
        contentProjects = []
        for proj in contProjElements:
            contentProjects.append(proj.text)
        return contentProjects
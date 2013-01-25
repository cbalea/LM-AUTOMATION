'''
Created on 11.12.2012

@author: cbalea
'''
from cms.pages.login_page_cms import LoginPageCMS
from cms.pages.station_site_cms.station_module_pages_cms import \
    StationModulesPageCMS, EditAddStationModulePageCMS
from cms.tests.base_cms_tests import SeleniumTestBaseCMS
from utils.server_related import ServerRelated

lmSite = "PBS Learning Media: www"
title = "Selenium tests lates promos"
imageLink = "http://does.dc.gov/sites/default/files/styles/callout_home_graphic/public/dc/sites/does/featured_content/images/OCOH_Callout_0.jpg"
subhead = "subhead0"
description = "description0"
promo = "promo0"
link = "www.google.com"

def remove_station_module(driver, wait):
    driver.get(ServerRelated().serverToBeTested()+"/admin/")
    LoginPageCMS(driver, wait).login("admin", ServerRelated().admin_password())
    allModulesPg = StationModulesPageCMS(driver, wait)
    allModulesPg.clickCheckboxForItem(title)
    deletePage = allModulesPg.selectDeleteAction()
    newPage = deletePage.clickConfirmationButton()
    assert not(newPage.elementExistsByLinkText(title)), "Station module not deleted"



class TestStationModuleCMS(SeleniumTestBaseCMS):
    
    def test_add_station_module(self):
        allModulesPg = StationModulesPageCMS(self.driver, self.wait)
        modulePg = allModulesPg.clickAddStationModuleButton()
        modulePg.selectLmSiteByVisibleText(lmSite)
        modulePg.typeTitle(title)
        modulePg.clickStartOnTodayLink()
        modulePg.clickEndOnTodayLink()
        modulePg.selectPlaceholderByVisibleText("Right Rail")
        modulePg = EditAddStationModulePageCMS(self.driver, self.wait)
        modulePg.typeSubhead(0, subhead)
        modulePg.typeLink(0, link)
        modulePg.typePromo(0, promo)
        modulePg.addImageInPromo(0, imageLink)
        modulePg = modulePg.clickSaveAndContinueEditingButton()
        self.assertTrue(('"%s" was added successfully' %title) in modulePg.getSuccessfullyEditMessage(), "Station module not added")
    
    

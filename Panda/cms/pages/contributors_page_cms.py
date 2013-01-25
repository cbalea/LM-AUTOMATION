'''
Created on 26.10.2012

@author: cbalea
'''
from cms.pages.dashboard_page_cms import DashboardPageCMS
from utils.server_related import ServerRelated

class ContributorsPageCMS():
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.driver.get(ServerRelated().serverToBeTested() + "/admin/cms/contentproject/dashboard/contributors/")
    
    def openDashboardForOrganization(self, org):
        self.dashboardButtonForOrg = self.wait.until(lambda driver : driver.find_element_by_xpath("//tr/td/a[contains(text(), '%s')]/../../td[1]/a" %org))
        self.dashboardButtonForOrg.click()
        return DashboardPageCMS(self.driver, self.wait)



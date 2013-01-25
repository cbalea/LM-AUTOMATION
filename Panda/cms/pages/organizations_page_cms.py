'''
Created on 26.10.2012

@author: cbalea
'''
from cms.pages.base_page_cms import BasePageCMS
from selenium.webdriver.support.select import Select
from utils.server_related import ServerRelated

class OrganizatiosPageCMS(BasePageCMS):
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.driver.get(ServerRelated().serverToBeTested() + "/admin/authorization/organization/")
    
    def clickAddOrganization(self):
        self.clickAddButton()
        return EditAddOrganiztionPageCMS(self.driver, self.wait)

    def clickOrganizationByName(self, org):
        self.clickOnLink(org)
        return EditAddOrganiztionPageCMS(self.driver, self.wait)

    def clickOrganizationByIndex(self, index):
        self.clickItemInListTableByIndex(index)
        return EditAddOrganiztionPageCMS(self.driver, self.wait)



class EditAddOrganiztionPageCMS(BasePageCMS):
     
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.name = self.wait.until(lambda driver : driver.find_element_by_id("id_name"))
        self.parent = Select(self.wait.until(lambda driver : driver.find_element_by_id("id_parent")))
        self.lmSite = Select(self.wait.until(lambda driver : driver.find_element_by_id("id_lmsite")))
    
    def typeName(self, name):
        self.name.send_keys(name)
        
    def selectParent(self, parent):
        self.parent.select_by_visible_text(parent)
    
    def selectLmSite(self, site):
        self.lmSite.select_by_visible_text(site)
    
    def clickSaveAndContinueEditingButton(self):
        self.clickSaveAndContinueEditing()
        return EditAddOrganiztionPageCMS(self.driver, self.wait)
    
    def getName(self):
        return self.name.get_attribute("value")
    
    def getSelectedParent(self):
        return self.parent.first_selected_option.text
    
    def getSelectedLmSite(self):
        return self.lmSite.first_selected_option.text
    
    def clickObjectPermissions(self):
        self.clickOnLink("Object permissions")
        return OrganizationObjectPermissionsCMS(self.driver, self.wait)




class OrganizationObjectPermissionsCMS():
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.username = self.wait.until(lambda driver : driver.find_element_by_id("id_user"))
        self.manageUserButton = self.wait.until(lambda driver : driver.find_element_by_xpath("//input[@name='submit_manage_user']"))
    
    def enterUsername(self, userName):
        self.username.send_keys(userName)
        self.manageUserButton.click()
        return OrganizationPermissionsUserManageCMS(self.driver, self.wait)
    
    def getPermissionsForUser(self, user):
        self.userRow = self.wait.until(lambda driver : driver.find_element_by_xpath("//table[@id='user-permissions']/tbody/tr/td[text()='%s']/../" %user))
        return self.userRow.text




class OrganizationPermissionsUserManageCMS(BasePageCMS):
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.permissions = Select(self.wait.until(lambda driver : driver.find_element_by_id("id_permissions")))
    
    def selectUserPermission(self, permission):
        self.permissions.select_by_visible_text(permission)
    
    def clickSaveButton(self):
        self.clickSave()
        return OrganizationPermissionsUserManageCMS(self.driver, self.wait)
    
    def getNumberOfUserPermissions(self):
        return len(self.permissions.all_selected_options)
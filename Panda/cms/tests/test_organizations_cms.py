'''
Created on 26.10.2012

@author: cbalea
'''
from cms.pages.auth_users_pages_cms import AuthUsersPageCMS
from cms.pages.contributors_page_cms import ContributorsPageCMS
from cms.pages.dashboard_page_cms import DashboardPageCMS, \
    OrganizationUsersPageCMS
from cms.pages.home_page_cms import HomePageCMS
from cms.pages.organizations_page_cms import OrganizatiosPageCMS
from cms.pages.reports.users_report_cms import UsersReportCMS
from cms.tests.base_cms_tests import SeleniumTestBaseCMS, \
    SeleniumTestBaseNoLoginCMS
from utils.random_generators import RandomGenerators


orgName = RandomGenerators().generateRandomString(5)
org = orgName


parent = "--- PBS"
orgAdminEmail = "orgadmin@orgadmin.com"
orgAdminUsername = "orgAdmin"
orgUserEmail = "orguser@orguser.com"
orgUserName = "orgUser"
orgPass = "admin123"


def fillUserForm(createUserPage, email):
    createUserPage.typeEmail(email)


class TestOrganizationAddingCMS(SeleniumTestBaseCMS):
    
    def test_addOrganization(self):
        lmSite = ": az"
        orgsPage = OrganizatiosPageCMS(self.driver, self.wait)
        addOrgPage = orgsPage.clickAddOrganization()
        addOrgPage.typeName(org)
        addOrgPage.selectParent(parent)
        addOrgPage.selectLmSite(lmSite)
        editOrgPage = addOrgPage.clickSaveAndContinueEditingButton()
        self.assertEquals(editOrgPage.getName(), org, "Organization name not added correctly")
        self.assertEquals(editOrgPage.getSelectedParent(), parent, "Parent not added correctly")
        self.assertTrue(lmSite in editOrgPage.getSelectedLmSite(), "LM Site not added correctly")
    
    
    def test_addOrganizationContentProject(self):
        contributorsPage = ContributorsPageCMS(self.driver, self.wait)
        contributorsPage.openDashboardForOrganization(org)
        contentProjPage = HomePageCMS(self.driver, self.wait).clickContentProjectLink()
        addContProj = contentProjPage.clickAddContentProject()
        addContProj.typeTitle("%s content project" %org)
        addContProj.selectOrganizationByValue(org)
        addContProj.clickSaveAndContinueEditingButton()
        contributorsPage = ContributorsPageCMS(self.driver, self.wait)
        dashboard = contributorsPage.openDashboardForOrganization(org)
        self.assertTrue(dashboard.elementExistsByLinkText("%s content project" %org), "Content project not asigned to Organization")
        
    
    def test_defaultContentProjectCreatedForNewOrganization(self):
        contributorsPage = ContributorsPageCMS(self.driver, self.wait)
        dashboard = contributorsPage.openDashboardForOrganization(org)
        self.assertTrue(dashboard.elementExistsByLinkText("%s Default" %org), "Default content project not created for new organization")
    

    def test_defineAdminUserForOrganization(self):
        contributorsPage = ContributorsPageCMS(self.driver, self.wait)
        dashboard = contributorsPage.openDashboardForOrganization(org)
        orgUsersPage = dashboard.selectCreateUser()
        fillUserForm(orgUsersPage, orgAdminEmail)
        orgUsersPage.clickStationAdminRadio()
        orgUsersPage.clickContentAdminRadio()
        orgUsersPage = orgUsersPage.clickSaveButtonAddUserForm()
        self.assertTrue(orgUsersPage.userExists(orgAdminEmail), "Admin not added")
    
    
class TestOrganizationPermissionsForUsersCMS(SeleniumTestBaseNoLoginCMS):
   
    def test_loggedinAsOrganizationAdminDefineOrganizationUser(self):
        self.login_to_cms_via_uua(orgAdminEmail, orgPass)
        dashboard = DashboardPageCMS(self.driver, self.wait)
        orgUsersPage = dashboard.selectCreateUser()
        fillUserForm(orgUsersPage, orgUserEmail)
        orgUsersPage.clickContentEditorRadio()
        orgUsersPage = orgUsersPage.clickSaveButtonAddUserForm()
        self.assertTrue(orgUsersPage.userExists(orgUserEmail), "User not added")
    
    def test_loggedinAsOrganizationAdminValidateUserReportForm(self):
        self.login_to_cms_via_uua(orgAdminEmail, orgPass)
        userReport = UsersReportCMS(self.driver, self.wait)
        leftSidePanel = HomePageCMS(self.driver, self.wait)
        self.assertFalse(userReport.elementExistsById(userReport.organization_dropdown_id), 
                         "Organization dropdown is displayed, although it should not be.")
        self.assertEquals(userReport.getContentProjectOptions(), leftSidePanel.getContentProjectsListedInLeftSideBar(), 
                          "Content projects selectable from dropdown are not exactly the ones displayed in the left-side-bar.")
    
    def test_loggedinAsOrganizationUserSeeOnlyOrganizationContentProjects(self):
        self.login_to_cms_via_uua(orgUserEmail, orgPass)
        dashboard = DashboardPageCMS(self.driver, self.wait)
        self.assertEquals(dashboard.getNumberOfVisibleContentProjects(), 2, "User doesn't see only 2 content projects, as he is supposed to.")

    def test_organizationAdminCanRemoveOrganizationUser(self):
        self.login_to_cms_via_uua(orgAdminEmail, orgPass)
        dashboard = DashboardPageCMS(self.driver, self.wait)
        usersPage = dashboard.clickUsersLink()
        usersPage.clickCheckboxForItem(orgUserEmail, "noSearch")
        deletePage = usersPage.selectDeleteAction()
        deletePage.clickConfirmationButton()
        usersPage = OrganizationUsersPageCMS(self.driver, self.wait)
        usersPage = usersPage.showDeletedUsers()
        self.assertTrue(usersPage.userExists(orgUserEmail), "Organization user not deleted")


class TestOrganizationRemovalCMS(SeleniumTestBaseCMS):
    
    def reactivateOrganizationUser(self):
        authUsersPg = AuthUsersPageCMS(self.driver, self.wait)
        authUsersPg.search_in_searchbar(orgUserName)
        editUserPg = authUsersPg.openPageForUser(orgUserName)
        editUserPg.checkActiveCheckbox()
        editUserPg.clickSaveAndContinueEditingButton()
    
    def test_removeOrganization(self):
        self.reactivateOrganizationUser()
        orgsPage = OrganizatiosPageCMS(self.driver, self.wait)
        orgsPage.clickCheckboxForItem(org)
        deletePage = orgsPage.selectDeleteAction()
        newPage = deletePage.clickConfirmationButton()
        self.assertFalse(newPage.elementExistsByLinkText(org), "Organization not deleted")
    
    
class TestParentDefiningForOrganization(SeleniumTestBaseCMS):
    
    def test_currentOrganizationCannotBeParent(self):
        orgsPage = OrganizatiosPageCMS(self.driver, self.wait)
        orgPage = orgsPage.clickOrganizationByIndex(3)
        currentOrgName = orgPage.getName()
        self.assertFalse(orgPage.elementExistsByXpath("//select[@name='parent']/option[contains(text(), '%s')]" %currentOrgName), 
                                                      "Current organization can be selected as it's self parent.")
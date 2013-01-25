'''
Created on 19.09.2012

@author: cbalea
'''
from ss.pages.home_profile_login_pages_ss import MyProfilePageSS
from ss.tests.base_ss_tests import SeleniumTestBaseSS

class TestMyProfilePagesSS(SeleniumTestBaseSS):
    

    def goToEditProfilePage(self):
        myProfilePage = MyProfilePageSS(self.driver, self.wait)
        editProfilePage = myProfilePage.clickEditProfileLink()
        return editProfilePage

    def test_changePassword(self):
        myProfilePage = MyProfilePageSS(self.driver, self.wait)
        changePassPage = myProfilePage.clickChangePsswordLink()
        confirmPage = changePassPage.fillForm(self.superuser_password, "%s1" %self.superuser_password)
        profilePage = confirmPage.clickContinueButton()
        changePassPage = profilePage.clickChangePasswordButton()
        confirmPage = changePassPage.fillForm("%s1" %self.superuser_password, self.superuser_password)
        self.assertEquals(confirmPage.getConfirmationMessage(), "Your password was successfully changed","Password not changed!")

    def test_selectUserRolePreferredSubjectsGradeRangeSchool(self):
        role = "Informal Educator"
        gradeRange = "6-8"
        school = "KING COVE SCHOOL"
        subject = "Science"
        postalCode = "99612"

        editProfilePage = self.goToEditProfilePage()
        editProfilePage.selectUserRoleByVisibleText(role)
        editProfilePage.selectGradeRange(gradeRange)
        editProfilePage.selectSchool(school)
        editProfilePage.selectFirstPreferredSubject()
        homePage = editProfilePage.clickSubmit()
        myProfilePage = MyProfilePageSS(self.driver, self.wait)
        self.assertTrue(role in myProfilePage.getProfileDetails(), "User role not updated")
        self.assertTrue(subject in myProfilePage.getProfileDetails(), "Preferred subjects not updated")
        self.assertTrue(gradeRange in myProfilePage.getProfileDetails(), "Grade range not updated")
        self.assertTrue(school in myProfilePage.getProfileDetails(), "School not updated")
        
        
    def test_emptyPostalCodeDisplaiesValidationMessage(self):
        editProfilePage = self.goToEditProfilePage()
        editProfilePage.typeInPostalCode("")
        editProfilePage.clickSubmitAndReload()
        self.assertTrue(editProfilePage.postalCodeValidationMessageIsDisplayed(), "Validation message not displayed")
        
        
    def test_selectableRolesSubjectsAndGradeRanges(self):
        editProfilePage = self.goToEditProfilePage()
        self.assertEquals(editProfilePage.getNumberOfAvailableSubjects(), 9, "Number of printed preffered subject checkboxes is not what it is supposed to be: 8.")
        self.assertTrue(self.findOptionByText("id_user_role", "Administrator/Media Specialist"), "Administrator/Media Specialist disappeared from the available user roles")
        self.assertTrue(self.findOptionByText("id_user_role", "Learner"), "Learner disappeared from the available user roles")
        self.assertTrue(self.findOptionByText("id_user_role", "Homeschooler"), "Homeschooler disappeared from the available user roles")
        self.assertTrue(self.findOptionByText("id_user_role", "Informal Educator"), "Informal Educator disappeared from the available user roles")
        self.assertTrue(self.findOptionByText("id_user_role", "Other"), "Other disappeared from the available user roles")
        self.assertTrue(self.findOptionByText("id_user_role", "K-12/Post-Secondary Educator"), "K-12/Post-Secondary Educator disappeared from the available user roles")
        self.assertTrue(self.findOptionByText("id_user_role", "Informal Educator"), "Informal Educator disappeared from the available user roles")
        self.assertTrue(self.findOptionByText("id_user_role", "Early Childhood Educator"), "Early Childhood Educator disappeared from the available user roles")
        self.assertTrue(self.findOptionByText("id_grade_range", "Pre-k"), "This grade option disappeared from the available user roles")
        self.assertTrue(self.findOptionByText("id_grade_range", "K-2"), "This grade option disappeared from the available user roles")
        self.assertTrue(self.findOptionByText("id_grade_range", "3-5"), "This grade option disappeared from the available user roles")
        self.assertTrue(self.findOptionByText("id_grade_range", "6-8"), "This grade option disappeared from the available user roles")
        self.assertTrue(self.findOptionByText("id_grade_range", "9-12"), "This grade option disappeared from the available user roles")
        self.assertTrue(self.findOptionByText("id_grade_range", "13+"), "This grade option disappeared from the available user roles")


    def findOptionByText(self, selecter_id, option_text):
        xpath = "//select[@id='%s']/option[text()='%s']" %(selecter_id, option_text)
        return self.driver.find_element_by_xpath(xpath).is_displayed()
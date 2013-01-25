'''
Created on 19.09.2012

@author: cbalea
'''
from common.uua_login_page import UuaLoginPage
from common.uua_password_change_pages import PasswordChangePageUUA
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from ss.pages.base_page_ss import BasePageSS
from ss.pages.browse_by_standards_page_ss import BrowseByStandardsPageSS
from ss.pages.search_pages_ss import SearchResultsPageSS
from utils.server_related import ServerRelated

#    !!! These classes need to be in the same module so that !!! 
#    !!! we avoid circular imports due to the fact the one returns the other !!!



class HomePageSS(BasePageSS):
    
    loginButton = WebElement(None, None)

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.driver.get(ServerRelated().serverToBeTested())
        self.browseByAllGradesSectionHeader = self.wait.until(lambda driver : driver.find_element_by_xpath("//p[text()='Grade Levels']"))
        self.browseByAllSubjectsSectionHeader = self.wait.until(lambda driver : driver.find_element_by_xpath("//p[text()='Subjects']"))
        self.browseByStandardsSectionHeader = self.wait.until(lambda driver : driver.find_element_by_xpath("//p[text()='Standards (Coming soon)']"))
        self.browseByCollectionsSectionHeader = self.wait.until(lambda driver : driver.find_element_by_xpath("//p[text()='Collections']"))
        self.browseSectionsExpanders = self.wait.until(lambda driver : driver.find_elements_by_xpath("//span[@class='opener']/i"))
        
    
    def expand_browse_sections(self):
        for expander in self.browseSectionsExpanders:
            expander.click()
        
    def browse_section_is_displayed_under_feature_well(self):
        return self.elementExistsByXpath("//section/div/h2/../../../section/div/h3[text()='Browse PBS LearningMedia']")
    
    def clickBrowseByStandardsLink(self):
        self.browseByStandardsSectionHeader.click()
        return BrowseByStandardsPageSS(self.driver, self.wait)

    def clickGradeIntervalInBrowseByGradeLevels(self, interval):
        link = self.wait.until(lambda driver : driver.find_element_by_xpath("//p[text()='Grade Levels']/../div/a[text()='%s']" %interval))
        link.click()
        return SearchResultsPageSS(self.driver, self.wait)

    def myProfileButton(self):
        return self.wait.until(lambda driver : driver.find_element_by_xpath("//a[contains(text(),'My Profile')]"))
        
    def clickLoginButton(self):
        self.driver.find_element_by_id("loginButton").click()
        return UuaLoginPage(self.driver, self.wait)
    
    def clickSignupButton(self):
        signupButton= self.wait.until(lambda driver : driver.find_element_by_id("signupButton"))
        signupButton.click()
        return UuaLoginPage(self.driver, self.wait)
    
    def myProfileButtonButtonExists(self):
        return self.myProfileButton().is_displayed()
    
#    def login(self):
#        uuaLoginPg = self.clickLoginButton()
#        uuaLoginPg.login("guest@guest.com", "Guestguest")
#        return HomePageSS(self.driver, self.wait)
        
    def greenAlertBoxExists(self):
        return self.elementExistsByClassName("green-alert-box")
    
    def contentFragmentExistsByTitle(self, contentFragmentTitle):
        return self.elementExistsByXpath("//div[@class='pbscustom section-head']/h3[text()='%s']" %contentFragmentTitle)
    
    def getContentFragmentsTitle(self):
        titles = []
        contentFragmentsTitle = self.wait.until(lambda driver : driver.find_elements_by_xpath("//div[@id='homepage-right-pane']/section/div[@class='pbscustom section-head']/h3"))
        for contFragm in contentFragmentsTitle:
            titles.append(contFragm.text)
        return titles
    
    def getContentFragmentContent(self):
        return self.wait.until(lambda driver : driver.find_element_by_xpath("//div[@id='homepage-right-pane']/section/div[@class='pbscustom section-content']")).text
    
    def getFeatureWellTitle(self):
        return self.wait.until(lambda driver : driver.find_element_by_xpath("//div[@id='homepage-left-pane']/section/div/h2")).text
    
    def getFeatureWellSlides(self):
        slides = self.wait.until(lambda driver : driver.find_elements_by_xpath("//div[@id='homepage-image-carousel']/div/ul[@class='slides']/li"))
        return slides
    
    def get_stat_mod_subhead(self):
        subhead = self.wait.until(lambda driver : driver.find_element_by_xpath("//span[@class='promo_subhead']/a"))
        return subhead
    
    def get_stat_mod_image(self):
        image = self.wait.until(lambda driver : driver.find_element_by_xpath("//span[@class='promo_subhead']/../p/img"))
        return image.get_attribute("src")
    
    def station_module_exists_by_title(self, moduleTitle):
        return self.elementExistsByXpath("//div[@class='pbscustom section-head']/h3[text()='%s']" %moduleTitle)
    
    def clickAdminLinkInNavigationBar(self):
        link = self.wait.until(lambda driver : driver.find_element_by_xpath("//a[@href='/admin/']"))
        link.click()
        
    

class MyProfilePageSS(BasePageSS):
    editProfileLink = WebElement(None, None)
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.driver.get(ServerRelated().serverToBeTested() + "/profile/")
        self.editProfileLink = self.wait.until(lambda driver : driver.find_element_by_xpath("//a[text()='Edit Profile']"))
        self.profileDetails = self.wait.until(lambda driver : driver.find_element_by_xpath("//span[text()='My Profile']/../.."))
        
    def clickEditProfileLink(self):
        self.editProfileLink.click()
        return EditProfilePageSS(self.driver, self.wait)

    def getProfileDetails(self):
        return self.profileDetails.text
    
    def clickChangePsswordLink(self):
        self.clickOnLink("Change Password")
        self.switchToNewestWindow()
        return PasswordChangePageUUA(self.driver, self.wait)
    
    

class EditProfilePageSS(BasePageSS):
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.firstName = self.wait.until(lambda driver : driver.find_element_by_id("id_first_name"))
        self.lastName = self.wait.until(lambda driver : driver.find_element_by_id("id_last_name"))
        self.username = self.wait.until(lambda driver : driver.find_element_by_id("id_username"))
        self.email = self.wait.until(lambda driver : driver.find_element_by_id("id_email"))
        self.userRole = Select(self.wait.until(lambda driver : driver.find_element_by_id("id_user_role")))
        self.postalCode = self.wait.until(lambda driver : driver.find_element_by_id("id_postal_code"))
        self.submitButton = self.wait.until(lambda driver : driver.find_element_by_xpath("//input[@value='Submit']"))
        self.school = Select(self.wait.until(lambda driver : driver.find_element_by_id("id_user_school")))
        self.subjects = self.wait.until(lambda driver : driver.find_elements_by_xpath("//ul[@class='preferred_subjects_checks']/li/label/input"))
        
    def selectUserRoleByVisibleText(self, text):
        self.userRole.select_by_visible_text(text)
    
    def getSelectedUserRole(self):
        return self.userRole.first_selected_option.text
    
    def getSelectableUserRoles(self):
        return self.userRole.options.text
        
    def clickSubmit(self):
        self.submitButton.click()
        return HomePageSS(self.driver, self.wait)
    
    def selectGradeRange(self, gradeRange):
        self.gradeRange = Select(self.wait.until(lambda driver : driver.find_element_by_id("id_grade_range")))
        self.gradeRange.select_by_visible_text(gradeRange)
    
    def getSelectedGradeRange(self):
        self.gradeRange = Select(self.wait.until(lambda driver : driver.find_element_by_id("id_grade_range")))
        return self.gradeRange.first_selected_option.text
    
    def getNumberOfAvailableSubjects(self):
        return len(self.subjects)     
    
    def selectFirstPreferredSubject(self):
        if(self.isCheckboxChecked(self.subjects[0])):
            self.subjects[0].click()
        self.subjects[0].click()

    def typeInPostalCode(self, zipcode):
        self.postalCode.clear()
        self.postalCode.send_keys(zipcode)
    
    def selectSchool(self, school):
        self.school.select_by_visible_text(school)
    
    def getSelectedSchool(self):
        return self.school.first_selected_option.text
    
    def clickSubmitAndReload(self):
        self.submitButton.click()
        return EditProfilePageSS(self.driver, self.wait)
    
    def postalCodeValidationMessageIsDisplayed(self):
        return self.elementExistsByXpath("//label[text()='Postal code']/../ul[@class='errorlist']/li[text()='This field is required.']")

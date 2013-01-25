'''
Created on 13.11.2012

@author: cbalea
'''

class PasswordChangePageUUA():
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.oldPassField = self.wait.until(lambda driver : driver.find_element_by_id("id_old_password"))
        self.newPassField = self.wait.until(lambda driver : driver.find_element_by_id("id_password"))
        self.confirmPassField = self.wait.until(lambda driver : driver.find_element_by_id("id_password_confirm"))
        self.saveButtonField = self.wait.until(lambda driver : driver.find_element_by_xpath("//button/span[text()='Save']"))
        
    def fillForm(self, oldPass, newPass):
        self.oldPassField.send_keys(oldPass)
        self.newPassField.send_keys(newPass)
        self.confirmPassField.send_keys(newPass)
        self.saveButtonField.click()
        return PasswordChangeConfirmationPageUUA(self.driver, self.wait)



class PasswordChangeConfirmationPageUUA():
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.confirmMessage = self.wait.until(lambda driver : driver.find_element_by_xpath("//h2"))
        self.continueButton = self.wait.until(lambda driver : driver.find_element_by_xpath("//button/span[text()='Continue']"))

    def getConfirmationMessage(self):
        return self.confirmMessage.text

    def clickContinueButton(self):
        self.continueButton.click()
        return ProfileViewPageUUA(self.driver, self.wait)



class ProfileViewPageUUA():
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.changePassButton = self.wait.until(lambda driver : driver.find_element_by_xpath("//button/span[text()='Change Password']"))
    
    def clickChangePasswordButton(self):
        self.changePassButton.click()
        return PasswordChangePageUUA(self.driver, self.wait)
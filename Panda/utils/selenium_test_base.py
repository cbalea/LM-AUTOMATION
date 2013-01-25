'''
Created on 22.10.2012

@author: cbalea
'''
from cms.pages.login_page_cms import LoginPageCMS
from utils.driver_factory import DriverFactory
from utils.server_related import ServerRelated
import glob
import os
import pickle
import time
import unittest

class SeleniumTestBase(unittest.TestCase):
    
    cookie_filename_root = "lm-selenium-cookie"
    superuser_username = "lmadmin"
    superuser_email = "lmadmin@lmadmin.com"
    superuser_password = "lmadmin123"
    
    
    def setup_wit_cookies_load(self):
        self.driver = DriverFactory().initializeDriver()
        self.wait = DriverFactory().initializeWait(self.driver)
        self.driver.maximize_window()
        self.driver.get(ServerRelated().serverToBeTested()+"/admin/")
        self.driver.delete_all_cookies()
        self.load_cookies_from_files()

    def delete_all_cookie_files(self):
        all_cookie_files = glob.glob(ServerRelated().download_directory() + '/' + self.cookie_filename_root +'*.txt')
        for cookie_file in all_cookie_files:
            return os.remove(cookie_file)

    def save_existing_cookies_to_files(self):
        self.delete_all_cookie_files()
        
        i = 0
        for cookie in self.driver.get_cookies():
            origin_file = ServerRelated().download_directory() + "/" + self.cookie_filename_root + str(i) + ".txt"
            with open(origin_file, "w") as origin_file:
                origin_file.write(pickle.dumps(cookie))
            i += 1


    def load_cookies_from_files(self):
        nb_of_saved_cookies = len(glob.glob(ServerRelated().download_directory() + '/' + self.cookie_filename_root +'*.txt'))
        new_cookies = []
        for i in xrange(nb_of_saved_cookies):
            file_to_read = ServerRelated().download_directory() + "/" + self.cookie_filename_root + str(i) + ".txt"
            file_readed = open(file_to_read)
            new_cookies.append(pickle.loads(file_readed.read()))
            file_readed.close()
        for cookie in new_cookies:
            self.driver.add_cookie(cookie)
    
    
    def takeScreenshot(self, fileName):
        self.driver.get_screenshot_as_file("/tmp/%s.png" %fileName)
    
    
    def waitUntilLoginPerformed(self, username, password, timeout):
        seconds = 0
        self.wait.until(lambda driver : driver.find_element_by_xpath("//title"))
        while "Log in" in self.driver.title and seconds <= timeout:
            self.driver.get(ServerRelated().serverToBeTested() + "/admin/")
            LoginPageCMS(self.driver, self.wait).login(username, password)
            time.sleep(1)
            print "Waiting %ds for logging-in with %s" %( (timeout - seconds), username)
            seconds += 1
        if(seconds>=timeout):
            raise Exception ("Login not performed!")
    
    
    def login_to_cms_via_uua(self, username, password):
        loginPg = LoginPageCMS(self.driver, self.wait)
        uuaLoginPg = loginPg.clickLoginWithYourPbsAccountLink()
        uuaLoginPg.login(username, password)
    
    
    def getAddressWithSubdomain(self, subdomain):
        return ("http://%s." %subdomain) + ServerRelated().serverToBeTested().partition("//")[2]
        
        
    def assertFileIsDownloaded(self, fileName):
        downloadedFile = ServerRelated().download_directory() + "/" + fileName
        try:
            with open(downloadedFile) as f: pass
            self.assertTrue(True)   # assertTrue if file exists
            os.remove(downloadedFile)
        except IOError:
            self.assertTrue(False, "File was not downloaded.")
    
    
    
    def tearDown(self):
        self.driver.quit()
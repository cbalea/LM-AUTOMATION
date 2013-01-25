'''
Created on 14.09.2012

@author: cbalea
'''
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from utils.server_related import ServerRelated
import os
import sys


class DriverFactory(object):
    

    def initializeFirefoxDriver(self):
        fp = webdriver.FirefoxProfile()
        fp.set_preference("browser.download.folderList", 2)
        fp.set_preference("browser.download.manager.showWhenStarting", False)
        fp.set_preference("browser.download.dir", ServerRelated().download_directory())
        fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf, text/csv, application/msword")
        
        driver = webdriver.Firefox(firefox_profile=fp)
        return driver
        
    
    def initializeChromeDriver(self):
        o_s = sys.platform
        if("win" in o_s):
            chromedriver = ServerRelated().getFilePathInProjectFolder("drivers/chromedriver.exe")
        elif("linux" in o_s):
            chromedriver = ServerRelated().getFilePathInProjectFolder("drivers/chromedriver")
        print chromedriver
        os.environ["webdriver.chrome.driver"] = chromedriver
        driver = webdriver.Chrome(chromedriver)
        return driver
    
    
    def initializeDriver(self):
        try:
            browser = os.environ["BROWSER"]
            if (browser=="firefox"):
                return self.initializeFirefoxDriver()
            elif (browser=="chrome"):
                return self.initializeChromeDriver()
        except KeyError: 
            return self.initializeFirefoxDriver()
    
    
    def initializeWait(self, driver):
        try:
            timeout = int(os.environ["IMPLICIT_TIMEOUT"])
        except KeyError: 
            timeout = 30
        wait = WebDriverWait(driver, timeout)
        return wait
   
   

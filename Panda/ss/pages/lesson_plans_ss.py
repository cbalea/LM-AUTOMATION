'''
Created on 09.01.2013

@author: cbalea
'''
from ss.pages.resource_view_page_ss import ResourceViewPageSS
import time

class LessonPlanPageSS(ResourceViewPageSS):
    
    def __init__(self, driver, wait, lessonPlanId):
        self.driver = driver
        self.wait = wait
        super(LessonPlanPageSS, self).__init__(driver, wait, lessonPlanId)

    
    def clickOveriviewTab(self):
        self.clickOnLink("Overview")
    
    def clickProcedureTab(self):
        self.clickOnLink("Procedure")
        time.sleep(1)
    
    def getLessonSummary(self):
        lessonSummary = self.wait.until(lambda driver : driver.find_element_by_xpath("//p[@class='sub-title' and text()='Lesson Summary']/following-sibling::p"))
        return lessonSummary.text
    
    def getTimeAllotment(self):
        timeAllotment = self.wait.until(lambda driver : driver.find_element_by_xpath("//p[@class='sub-title' and text()='Time Allotment']/following-sibling::p"))
        return timeAllotment.text
    
    def getLearningObjectives(self):
        learningObj = self.wait.until(lambda driver : driver.find_element_by_xpath("//div[contains(@class,'active')]/p[@class='sub-title' and text()='Learning Objectives']/following-sibling::p"))
        return learningObj.text
    
    def getSupplies(self):
        supplies = self.wait.until(lambda driver : driver.find_element_by_xpath("//div[contains(@class,'active')]/p[@class='sub-title' and text()='Supplies']/following-sibling::p"))
        return supplies.text
    
    def getPrepForTeachers(self):
        prepForTeachers = self.wait.until(lambda driver : driver.find_element_by_xpath("//div[contains(@class,'active')]/p[@class='sub-title' and text()='Prep for Teachers']/following-sibling::p"))
        return prepForTeachers.text
    
    def getIntoductoryActivity(self):
        introActivity = self.wait.until(lambda driver : driver.find_element_by_xpath("//p[@class='sub-title' and text()='Introductory Activity']/following-sibling::p"))
        return introActivity.text
    
    def getLearningActivities(self):
        learningAct = self.wait.until(lambda driver : driver.find_element_by_xpath("//p[@class='sub-title' and text()='Learning Activities']/following-sibling::p"))
        return learningAct.text 
        
    
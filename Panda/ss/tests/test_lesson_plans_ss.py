#'''
#Created on 09.01.2013
#
#@author: cbalea
#'''
#from ss.pages.lesson_plans_ss import LessonPlanPageSS
#from ss.tests.base_ss_tests import SeleniumTestBaseNoLoginSS
#
#lessonPlanId = "wa08.socst.world.glob.lptheroad"
#
#class TestLessonPlansSS(SeleniumTestBaseNoLoginSS):
#    
#    def test_overview_tab_content_displaies_correctly(self):
#        lessPlanPg = LessonPlanPageSS(self.driver, self.wait, lessonPlanId)
#        lessPlanPg.clickOveriviewTab()
#        self.assertTrue(lessPlanPg.getLessonSummary()!='', "Lesson Summary not displayed")
#        self.assertTrue(lessPlanPg.getTimeAllotment()!='', "Time Allotment not displayed")
##        self.assertTrue(lessPlanPg.getLearningObjectives()!='', "Learning Objectives not displayed")
#        self.assertTrue(lessPlanPg.getSupplies()!='', "Supplies not displayed")
#        self.assertTrue(lessPlanPg.getPrepForTeachers()!='', "Prep for Teachers not displayed")
#    
#    def test_procedure_tab_content_displaies_correctly(self):
#        lessPlanPg = LessonPlanPageSS(self.driver, self.wait, lessonPlanId)
#        lessPlanPg.clickProcedureTab()
#        self.assertTrue(lessPlanPg.getIntoductoryActivity()!='', "Intoructory Activity not displayed")
##        self.assertTrue(lessPlanPg.getLearningActivities()!='', "Learning Activities not displayed")
##        self.assertTrue(lessPlanPg.getLearningObjectives()!='', "Learning Objectives not displayed")
#        self.assertTrue(lessPlanPg.getSupplies()!='', "Supplies not displayed")
#        self.assertTrue(lessPlanPg.getPrepForTeachers()!='', "Prep for Teachers not displayed")
        
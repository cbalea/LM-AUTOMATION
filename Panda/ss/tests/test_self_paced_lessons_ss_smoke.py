'''
Created on 29.11.2012

@author: cbalea
'''
from ss.pages.self_paced_lessons_ss import SelfPacedLessons
from ss.tests.base_ss_tests import SeleniumTestBaseNoLoginSS
import sys


class TestSelfPacedLessonsSS(SeleniumTestBaseNoLoginSS):
    
    resourceId = "midlit10.soc.splerie/building-the-erie-canal/"
    
    def test_spl_navigation(self):
        spl = SelfPacedLessons(self.driver, self.wait, self.resourceId)
        spl.clickNext()
        page2Title = spl.getSectionTitle()
        spl.clickNext()
        page3Title = spl.getSectionTitle()
        spl.clickBack()
        page2TitleRefreshed = spl.getSectionTitle()
        spl.clickFinalAssignment()
        finalAsTitle = spl.getSectionTitle()
        self.assertNotEqual(page2Title, page3Title, "Page not changed on navigation")
        self.assertEqual(page2Title, page2TitleRefreshed, "Page not changed on navigation")
        self.assertEqual(finalAsTitle, "Final Assignment", "Page not changed on navigation")
        
    def test_spl_credits_in_out_navigation(self):
        spl = SelfPacedLessons(self.driver, self.wait, self.resourceId)
        spl.clickPage(2)
        page2Title = spl.getSectionTitle()
        spl.clickCredits()
        spl.clickBackToLesson()
        page2TitleRefreshed = spl.getSectionTitle()
        self.assertEqual(page2Title, page2TitleRefreshed, "Navigating back from credits doesn't lead to the same page")
    
    def test_spl_definition_tooltip(self):
        spl = SelfPacedLessons(self.driver, self.wait, self.resourceId)
        spl.clickPage(3)
        spl.clickWordToOpenDefinition("canal")
        self.assertEqual(spl.getTooltipDefinition(), "A human-made waterway built for boats to travel from one body of water to another.", "Definition tooltip not loaded")
    
    def test_is_spl_frame_displayed(self):
        spl = SelfPacedLessons(self.driver, self.wait, self.resourceId)
        self.assertTrue(spl.isSplFrameDisplayed(), "SPL not displayed")
    
    def test_open_document_in_spl(self):
        docName = "midlit10_doc_spleriereading.pdf"
        spl = SelfPacedLessons(self.driver, self.wait, self.resourceId)
        spl.clickPage(9)
        spl.clickViewButton()
        o_s = sys.platform
        if("win" in o_s):
            self.assertEqual(self.driver.title, docName + " (application/pdf Object)", "Pdf document not opened")
        elif("linux" in o_s):
            self.assertFileIsDownloaded(docName)
    
    def test_open_video_in_spl(self):
        spl = SelfPacedLessons(self.driver, self.wait, self.resourceId)
        spl.clickPage(7)
        new_page = spl.clickViewButton()
        self.assertTrue(new_page.elementExistsById("mediaplayer"), "Pop-up contains no video")
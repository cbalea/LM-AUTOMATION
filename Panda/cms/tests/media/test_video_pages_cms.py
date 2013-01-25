'''
Created on 18.09.2012

@author: cbalea
'''
from cms.pages.media.video_pages_cms import EditAddVideoPageCMS, VideosPageCMS
from cms.tests.base_cms_tests import SeleniumTestBaseCMS
from utils.random_generators import RandomGenerators
from utils.server_related import ServerRelated

class TestVideoPagesCMS(SeleniumTestBaseCMS):
    
    videoFilePath = "fixtures/video_sample.avi"
    videoFilePathForEdit = "fixtures/video_sample1.avi"
    transcriptFilePath = "fixtures/text_sample.txt"
    transcriptFilePathForEdit = "fixtures/text_sample1.txt"
    captionFilePath = "fixtures/text_sample.txt"
    captionFilePathForEdit = "fixtures/text_sample1.txt"
    videoName = RandomGenerators().generateRandomString(5)
    video = videoName
    
    
    
    def test_addVideo(self):
        lang = "French"
        w_h = "10"
        aspectRatio = "16:9"
        embeddedCode = "embedded code"
        transcriptTxt = "transcript text"
        
        self.driver.get(ServerRelated().serverToBeTested() + "/admin/cms/videomedia/add/")
        addVideoPage = EditAddVideoPageCMS(self.driver, self.wait)
        addVideoPage.typeName(self.video)
        addVideoPage.selectContentProjectByIndex(1)
        addVideoPage.typeVideoFilePath(ServerRelated().getFilePathInProjectFolder(self.videoFilePath))
        addVideoPage.selectLanguageByVisibleText(lang)
        addVideoPage.typeWidth(w_h)
        addVideoPage.typeHeight(w_h)
        addVideoPage.typeAspectRatio(aspectRatio)
        addVideoPage.typeEmbedCode(embeddedCode)
        addVideoPage.clickIsExternal()
        addVideoPage.clickShowTranscriptsLink()
        addVideoPage.typeTranscriptFilePath(ServerRelated().getFilePathInProjectFolder(self.transcriptFilePath))
        addVideoPage.clickAddTextButton()
        addVideoPage.typeTranscriptText(transcriptTxt)
        addVideoPage.clickShowCaptionsLink()
        addVideoPage.typeCaptionFilePath(ServerRelated().getFilePathInProjectFolder(self.captionFilePath))
        editVideoPage = addVideoPage.clickSaveAndContinueEditingButton()
        editVideoPage.clickShowCaptionsLink()
        editVideoPage.clickShowTranscriptsLink()
        self.assertEqual(editVideoPage.getName(), self.video, "Name not added correctly")
        self.assertTrue("---------" not in editVideoPage.getSelectedContentProject(), "Content project not added correctly")
        self.assertEqual(editVideoPage.getCurrentVideoFile(), "media_files/video_sample.avi", "Video file not uploaded correctly")
        self.assertEqual(editVideoPage.getSelectedLanguage(), lang, "Language not added correctly")
#        self.assertEqual(editVideoPage.getSize(), "148992", "File size not correct")
        self.assertEqual(editVideoPage.getWidth(), w_h, "Width not added correctly")
        self.assertEqual(editVideoPage.getHeight(), w_h, "Height not added correctly")
        self.assertEqual(editVideoPage.getAspectRatio(), aspectRatio, "Aspect ratio not added correctly")
        self.assertEqual(editVideoPage.getEmbeddedCode(), embeddedCode, "Embedded code not added correctly")
        self.assertTrue(editVideoPage.isExternalChecked(), "Is external not added correctly (checked)")
        self.assertEqual(editVideoPage.getCurrentTranscriptFile(), "transcripts/text_sample.txt", "Transcript file not uploaded correctly")
        self.assertEqual(editVideoPage.getTranscriptText(), transcriptTxt, "Transcript file not uploaded correctly")
        self.assertEqual(editVideoPage.getCurrentCaptionFile(), "captions/text_sample.txt", "Caption file not uploaded correctly")
#        self.assertTrue(editVideoPage.getContentOfStatusBox().count(self.getCurrentDate())==2, "Date Created or Last Modified is not the current date")
#        self.assertTrue(editVideoPage.getContentOfStatusBox().index("Triggered") !=0 , "Status is not Triggered")
    
    
    def test_editVideo(self):
        lang = "German"
        w_h = "11"
        aspectRatio = "4:3"
        embeddedCode = "new embedded code"
        transcriptTxt = "new text 1"
        
        videosPage = VideosPageCMS(self.driver, self.wait)
        editVideoPage = videosPage.clickOnVideo(self.video)
        editVideoPage.typeName("%s1" %self.video)
        editVideoPage.typeVideoFilePath(ServerRelated().getFilePathInProjectFolder(self.videoFilePathForEdit))
        editVideoPage.selectLanguageByVisibleText(lang)
        editVideoPage.typeWidth(w_h)
        editVideoPage.typeHeight(w_h)
        editVideoPage.typeAspectRatio(aspectRatio)
        editVideoPage.typeEmbedCode(embeddedCode)
        editVideoPage.clickShowCaptionsLink()
        editVideoPage.clickShowTranscriptsLink()
        editVideoPage.typeCaptionFilePath(ServerRelated().getFilePathInProjectFolder(self.captionFilePathForEdit))
        editVideoPage.typeTranscriptFilePath(ServerRelated().getFilePathInProjectFolder(self.transcriptFilePathForEdit))
        editVideoPage.typeTranscriptText(transcriptTxt)
        editVideoPage = editVideoPage.clickSaveAndContinueEditingButton()
        editVideoPage.clickShowCaptionsLink()
        editVideoPage.clickShowTranscriptsLink()
        self.assertEqual(editVideoPage.getName(), "%s1" %self.video, "Name not updated")
        self.assertEqual(editVideoPage.getCurrentVideoFile(), "media_files/video_sample1.avi", "Video file missing")
        self.assertEqual(editVideoPage.getSelectedLanguage(), lang, "Language not updated")
        self.assertEqual(editVideoPage.getWidth(), w_h, "Width not updated")
        self.assertEqual(editVideoPage.getHeight(), w_h, "Height not updated")
        self.assertEqual(editVideoPage.getAspectRatio(), aspectRatio, "Aspect ratio not updated")
        self.assertEqual(editVideoPage.getEmbeddedCode(), embeddedCode, "Embedded code not updated")
        self.assertEqual(editVideoPage.getTranscriptText(), transcriptTxt, "Transcript file not uploaded correctly")
        self.assertEqual(editVideoPage.getCurrentTranscriptFile(), "transcripts/text_sample1.txt", "Transcript file not modified correctly")
        self.assertEqual(editVideoPage.getCurrentCaptionFile(), "captions/text_sample1.txt", "Caption file not modified correctly")
    
    
    def test_removeVideo(self):
        videosPage = VideosPageCMS(self.driver, self.wait)
        videosPage.clickCheckboxForItem("%s1" %self.video)
        deletePage = videosPage.selectDeleteAction()
        newPage = deletePage.clickConfirmationButton()
        self.assertFalse(newPage.elementExistsByLinkText("%s1" %self.video), "Video not deleted")
    
    
#    def test_verifyIngestionStatusForVideo(self):
#        videosPage = VideosPageCMS(self.driver, self.wait)
#        editVideoPage = videosPage.openFirstVideoOlderThanYesterday()
#        self.assertTrue( ("Failed"  in editVideoPage.getContentOfStatusBox()) or  
#                         ("Success" in editVideoPage.getContentOfStatusBox()) , "Status is not Failed or Success!")
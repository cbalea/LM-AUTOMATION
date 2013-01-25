'''
Created on 18.09.2012

@author: cbalea
'''
from cms.pages.media.audio_pages_cms import AudiosPageCMS
from cms.tests.base_cms_tests import SeleniumTestBaseCMS
from utils.random_generators import RandomGenerators
from utils.server_related import ServerRelated



class TestAudioPagesCMS(SeleniumTestBaseCMS):
    
    audioFilePath = "fixtures/audio_sample.wav"
    audioFilePathForEdit = "fixtures/audio_sample1.wav"
    transcriptFilePath = "fixtures/text_sample.txt"
    transcriptFilePathForEdit = "fixtures/text_sample1.txt"
    audioName = RandomGenerators().generateRandomString(5)
    audio = audioName

    
    def test_addAudio(self):
        transcriptText = "transcript text"
        embeddedCode = "code"

        audiosPage = AudiosPageCMS(self.driver, self.wait)
        addAudioPage = audiosPage.clickAddAudioButton()
        addAudioPage.typeName(self.audio)
        addAudioPage.selectContentProjectByIndex(1)
        addAudioPage.typeAudioFilePath(ServerRelated().getFilePathInProjectFolder(self.audioFilePath))
        addAudioPage.clickIsExternal()
        self.takeScreenshot("1before_type_embedded_code")
        addAudioPage.typeEmbedCode(embeddedCode)
        addAudioPage.clickShowTranscriptsLink()
        addAudioPage.typeTranscriptFilePath(ServerRelated().getFilePathInProjectFolder(self.transcriptFilePath))
        addAudioPage.clickAddTextButton()
        addAudioPage.typeTranscriptText(transcriptText)
        editAudioPage = addAudioPage.clickSaveAndContinueEditingButton()
        editAudioPage.clickShowTranscriptsLink()
        self.assertEquals(editAudioPage.getName(), self.audio, "Name not added correctly")
        self.assertTrue(editAudioPage.getSelectedContentProject() != "---------", "Content project not added correctly")
        self.assertEquals(editAudioPage.getCurrentAudioFile(), "media_files/audio_sample.wav", "Audio file not added correctly")
        self.assertEquals(editAudioPage.getSelectedLanguage(), "English", "Language not correctly set by default (English)")
#        self.assertEquals(editAudioPage.getSize(), "47210", "File size not correct")
        self.assertTrue(editAudioPage.isExternalChecked(), "Is External checkbox not checked")
        self.takeScreenshot("2before_assert_embedded_code")
        self.assertEquals(editAudioPage.getEmbeddedCode(), embeddedCode, "Embeded code not correct")
        self.assertEquals(editAudioPage.getCurrentTranscriptFile(), "transcripts/text_sample.txt", "Transcript file not added correctly")
        self.assertEquals(editAudioPage.getTranscriptText(), transcriptText, "Transcript text not added correctly")
#        self.assertTrue(editAudioPage.getContentOfStatusBox().count(self.getCurrentDate())==2, "Date Created or Last Modified is not the current date")
#        self.assertTrue(editAudioPage.getContentOfStatusBox().index("Triggered") !=0 , "Status is not Triggered")
    
    
    def test_editAudio(self):
        language = "French"
        embeddedCode = "code1"
        transcriptText = "transcript text 1"
        unasignContentProject = "---------"
        
        audiosPage = AudiosPageCMS(self.driver, self.wait)
        editAudioPage = audiosPage.clickOnAudio(self.audio)
        editAudioPage.typeName("%s1" %self.audio)
        editAudioPage.selectContentProjectByVisibleText(unasignContentProject)
        editAudioPage.typeAudioFilePath(ServerRelated().getFilePathInProjectFolder(self.audioFilePathForEdit))
        editAudioPage.selectLanguageByVisibleText(language)
        editAudioPage.clickIsExternal()
        editAudioPage.typeEmbedCode(embeddedCode)
        editAudioPage.clickShowTranscriptsLink()
        editAudioPage.typeTranscriptFilePath(ServerRelated().getFilePathInProjectFolder(self.transcriptFilePathForEdit))
        editAudioPage.typeTranscriptText(transcriptText)
        editAudioPage = editAudioPage.clickSaveAndContinueEditingButton()
        editAudioPage.clickShowTranscriptsLink()
        self.assertEquals(editAudioPage.getName(), "%s1" %self.audio, "Name not updated")
        self.assertEquals(editAudioPage.getSelectedContentProject(), unasignContentProject, "Content project not unassigned")
        self.assertEquals(editAudioPage.getCurrentAudioFile(), "media_files/audio_sample1.wav", "Audio file not updated")
        self.assertEquals(editAudioPage.getSelectedLanguage(), language, "Language not updated")
#        self.assertEquals(editAudioPage.getSize(), "47210", "File size not correct")
        self.assertFalse(editAudioPage.isExternalChecked(), "Is External checkbox is checked and sould be unchecked")
        self.assertEquals(editAudioPage.getEmbeddedCode(), embeddedCode, "Embeded code not updated")
        self.assertEquals(editAudioPage.getCurrentTranscriptFile(), "transcripts/text_sample1.txt", "Transcript file not updated")
        self.assertEquals(editAudioPage.getTranscriptText(), transcriptText, "Transcript text not updated correctly")
    
    
    def test_removeAudio(self):
        audiosPage = AudiosPageCMS(self.driver, self.wait)
        audiosPage.clickCheckboxForItem("%s" %self.audio)
        deletePage = audiosPage.selectDeleteAction()
        newPage = deletePage.clickConfirmationButton()
        self.assertFalse(newPage.elementExistsByLinkText(self.audio), "Audio not deleted")

'''
Created on 10.10.2012

@author: cbalea
'''
from cms.pages.media.media_pages_cms import MediasPageCMS
from cms.tests.base_cms_tests import SeleniumTestBaseCMS
from utils.random_generators import RandomGenerators
from utils.server_related import ServerRelated


class TestMediaPagesCMS(SeleniumTestBaseCMS):
    
    filePath = "fixtures/audio_sample.wav"
    fileName = RandomGenerators().generateRandomString(5)
    file = fileName

    def test_addMedia(self):
        mediasPage = MediasPageCMS(self.driver, self.wait)
        addMediaPage = mediasPage.clickAddMediaButton()
        addMediaPage.typeName(self.file)
        addMediaPage.selectContentProjectByIndex(1)
        addMediaPage.typeFilePath(ServerRelated().getFilePathInProjectFolder(self.filePath))
        mediasPage = addMediaPage.clickSaveButton()
        editMediaPage = mediasPage.clickMedia(self.file)
        self.assertEqual(editMediaPage.getName(), self.file, "Name not added correctly")
        self.assertEqual(editMediaPage.getCurrentMediaFile(), "media_files/audio_sample.wav", "Current file not displayed")


    def test_removeMedia(self):
        mediaPage = MediasPageCMS(self.driver, self.wait)
        mediaPage.clickCheckboxForItem("%s" %self.file)
        deletePage = mediaPage.selectDeleteAction()
        newPage = deletePage.clickConfirmationButton()
        self.assertFalse(newPage.elementExistsByLinkText("%s" %self.file), "Media file not deleted")
        
        
    def test_search_media(self):
        mediaPage = MediasPageCMS(self.driver, self.wait)
        mediaPage.search_in_searchbar("a")
        mediaPage = MediasPageCMS(self.driver, self.wait, "noFreshLoad")
        self.assertTrue(mediaPage.countRowsInResultsTable() > 0, "Search results not displayed")
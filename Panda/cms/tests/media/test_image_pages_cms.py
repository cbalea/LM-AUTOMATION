'''
Created on 18.09.2012

@author: cbalea
'''
from cms.pages.media.image_pages_cms import ImagesPageCMS
from cms.tests.base_cms_tests import SeleniumTestBaseCMS
from utils.random_generators import RandomGenerators
from utils.server_related import ServerRelated


class TestImagePagesCMS(SeleniumTestBaseCMS):
    
    imageFilePath = "fixtures/image_sample.jpg"
    imageFilePathForEdit = "fixtures/image_sample1.jpg"
    imageName = RandomGenerators().generateRandomString(5)
    image = imageName

    
    def test_addImage(self):
        caption = "caption"
        h_w = "10"

        imagesPage = ImagesPageCMS(self.driver, self.wait)
        addImagePage = imagesPage.clickAddImageButton()
        addImagePage.typeName(self.image)
        addImagePage.typeImageFilePath(ServerRelated().getFilePathInProjectFolder(self.imageFilePath))
        addImagePage.typeHeight(h_w)
        addImagePage.typeWidth(h_w)
        addImagePage.clickShowCaptionsLink()
        addImagePage.typeCaptions(caption)
        editImagePage = addImagePage.clickSaveAndContinueEditingButton()
        editImagePage.clickShowCaptionsLink()
        self.assertEqual(editImagePage.getCurrentImageFile(), "media_files/image_sample.jpg", "Image file not uploaded correctly")
#        self.assertEqual(editImagePage.getMetaSize(), "32553", "File size not correct")
        self.assertEqual(editImagePage.getMetaWidth(), h_w, "Width not correct")
        self.assertEqual(editImagePage.getMetaHeight(), h_w, "Height not correct")
        self.assertEqual(editImagePage.getCaption(), caption, "Caption not added correctly")
#        self.assertTrue(editImagePage.getContentOfStatusBox().count(self.getCurrentDate())==2, "Date Created or Last Modified is not the current date")
#        self.assertTrue(editImagePage.getContentOfStatusBox().index("Triggered") !=0 , "Status is not Triggered")
        
        
    def test_editImage(self):
        h_w = "11"
        caption = "caption1"

        imagesPage = ImagesPageCMS(self.driver, self.wait)
        editImagePage = imagesPage.clickOnImage(self.image)
        editImagePage.typeName("%s1" %self.image)
        editImagePage.typeImageFilePath(ServerRelated().getFilePathInProjectFolder(self.imageFilePathForEdit))
        editImagePage.typeHeight(h_w)
        editImagePage.typeWidth(h_w)
        editImagePage.clickShowCaptionsLink()
        editImagePage.typeCaptions(caption)
        editImagePage = editImagePage.clickSaveAndContinueEditingButton()
        editImagePage.clickShowCaptionsLink()
        self.assertEqual(editImagePage.getName(), "%s1" %self.image, "Name not updated")
        self.assertEqual(editImagePage.getCurrentImageFile(), "media_files/image_sample1.jpg", "Image file not updated")
        self.assertEqual(editImagePage.getCaption(), caption, "Caption not updated")
#        self.assertEqual(editImagePage.getMetaSize(), "32553", "File size not correct")
        self.assertEqual(editImagePage.getMetaWidth(), h_w, "Width not updated")
        self.assertEqual(editImagePage.getMetaHeight(), h_w, "Height not updated")
    
    
    def test_removeImage(self):
        imagesPage = ImagesPageCMS(self.driver, self.wait)
        imagesPage.clickCheckboxForItem("%s1" %self.image)
        deletePage = imagesPage.selectDeleteAction()
        newPage = deletePage.clickConfirmationButton()
        self.assertFalse(newPage.elementExistsByLinkText("%s1" %self.image), "Image not deleted")
    
    
#    def test_verifyIngestionStatusForImage(self):
#        imagesPage = ImagesPageCMS(self.driver, self.wait)
#        editImagePage = imagesPage.openFirstImageOlderThanYesterday()
#        self.assertTrue(   ("Failed"  in editImagePage.getContentOfStatusBox() ) or 
#                           ("Success" in editImagePage.getContentOfStatusBox() ) , "Status is not Failed or Success!")
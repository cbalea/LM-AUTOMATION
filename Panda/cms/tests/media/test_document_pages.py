'''
Created on Oct 24, 2012

@author: jseichei
'''
from cms.pages.media.document_page_cms import DocumentMediaPageCMS
from cms.tests.base_cms_tests import SeleniumTestBaseCMS
from utils.random_generators import RandomGenerators
from utils.server_related import ServerRelated


class TestDocumentMediaCMS(SeleniumTestBaseCMS):
    
    documentFilePath = "fixtures/text_sample.txt"   
    documentName =  RandomGenerators().generateRandomString(8) 
    title = documentName
    
    def test_addDocument(self):
        
        documentPage = DocumentMediaPageCMS(self.driver, self.wait)
        addDocumentPage = documentPage.clickToAddDocumentMediaButton()
        addDocumentPage.typeInDocumentNameField(self.documentName)
        addDocumentPage.addDocumentFilePath(ServerRelated().getFilePathInProjectFolder(self.documentFilePath))
        addDocumentPage.selectLanguage("French")
        editDocumentPage = addDocumentPage.clickToSaveAndContinue()
        self.assertEqual(editDocumentPage.getDocumentName(), self.title, "Name is not added")
        self.assertEqual(editDocumentPage.getDocumentFile(), "media_files/text_sample.txt", "Document file not uploaded correctly")
        
        
        
        
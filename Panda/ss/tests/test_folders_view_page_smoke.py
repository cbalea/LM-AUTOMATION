'''
Created on Nov 28, 2012

@author: jseichei
'''

from ss.pages.folders_view_page import MyFoldersPageView
from ss.pages.home_profile_login_pages_ss import HomePageSS
from ss.pages.search_pages_ss import SearchResultsPageSS
from ss.pages.shared_public_favorites_pages_ss import SharedPublicFavoritesPages
from ss.tests.base_ss_tests import SeleniumTestBaseSS
from utils.random_generators import RandomGenerators


folderNameClass = RandomGenerators().generateRandomString(8)
folderNameColleagues = RandomGenerators().generateRandomString(8)
text = RandomGenerators().generateRandomString(10)


class TestFoldersSS(SeleniumTestBaseSS):
    
    def removeFolder(self, foldersPg, folderName):
        foldersPg.clickToEditFolders(folderName)
        foldersPg.clickDeleteFolder()
        foldersPg = foldersPg.clickSave()
        return foldersPg
     
    def test_click_add_to_folder_when_disabled(self):
        folders = MyFoldersPageView(self.driver, self.wait)
        folders.clickAddToFolderButton()
        self.assertFalse(folders.isDisplayedSelectFolderWidget(), "Select a folder widget displayed although no resource selected when clicking Add To Folder")

    def test_createFolderSharedWithClass(self):
        folders = MyFoldersPageView(self.driver, self.wait)
        folders.createNewFolder()
        folders.typeAddNewFolderName(folderNameClass)
        folders.typeAddNewFolderDescription(text)
        folders.clickSharedWithClass()
        folders = folders.clickToCreateButton()
        self.assertTrue(folders.folderExists(folderNameClass), "folder not created")
        
    def test_createFolderSharedWithColleagues(self):
        folders = MyFoldersPageView(self.driver, self.wait)
        folders.createNewFolder()
        folders.typeAddNewFolderName(folderNameColleagues)
        folders.typeAddNewFolderDescription(text)
        folders.clickSharedWithColleagues()
        folders = folders.clickToCreateButton()
        self.assertTrue(folders.folderExists(folderNameColleagues), "folder not created")
    
    def test_moveFavoritesToFolders(self):
        homePage = HomePageSS(self.driver, self.wait)
        homePage.searchByKeyword("test")
        searchResults = SearchResultsPageSS(self.driver, self.wait)
        searchResults.clickFavoriteStarForResult(1)
        searchResults.clickFavoriteStarForResult(2)
        searchResults.clickFavoriteStarForResult(3)
        searchResults.clickFavoriteStarForResult(4)
        favorited = MyFoldersPageView(self.driver, self.wait)
        favorited.clickToSelectAllButton()
        favorited.clickAddToFolderButton()
        favorited.selectFolder(folderNameClass)
        self.assertTrue(favorited.getFavoritesFromFolders(), "No Favorites saved to folder")
        
    def test_open_shared_with_class_public_page(self):
        sharedWithClassPg = SharedPublicFavoritesPages(self.driver, self.wait, self.superuser_username, "shared-with-class")
        sharedWithClassPg = sharedWithClassPg.openSubfolder(folderNameClass)
        self.assertEqual(sharedWithClassPg.getFolderTitle(), "Shared with Class", "Folder title (Shared with Class) not displayed")
        self.assertEqual(sharedWithClassPg.getSubfolderTitle(), folderNameClass, "Subfolder title (%s) not displayed" %folderNameClass)
        self.assertEqual(sharedWithClassPg.getSubfolderDescription(), text, "Subfolder description (%s) not displayed" %text)
        self.assertTrue(sharedWithClassPg.getNumberOfFavoritesInFolder()>0, "Folder contains not favorites")
    
    def test_open_shared_with_colleagues_public_page(self):
        sharedWithCollPg = SharedPublicFavoritesPages(self.driver, self.wait, self.superuser_username, "shared-with-colleagues")
        sharedWithCollPg = sharedWithCollPg.openSubfolder(folderNameColleagues)
        self.assertEqual(sharedWithCollPg.getFolderTitle(), "Shared with Colleagues", "Folder title (Shared with Colleagues) not displayed")
        self.assertEqual(sharedWithCollPg.getSubfolderTitle(), folderNameColleagues, "Subfolder title (%s) not displayed" %folderNameColleagues)
        self.assertEqual(sharedWithCollPg.getSubfolderDescription(), text, "Subfolder description (%s) not displayed" %text)
        
    def test_removeFolders(self):
        folders = MyFoldersPageView(self.driver, self.wait)
        folders = self.removeFolder(folders, folderNameClass)
        folders = self.removeFolder(folders, folderNameColleagues)
        self.assertFalse(folders.folderExists(folderNameColleagues), "folder not deleted")
        self.assertFalse(folders.folderExists(folderNameClass), "folder not deleted")

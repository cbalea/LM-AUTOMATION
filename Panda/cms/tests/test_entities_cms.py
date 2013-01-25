'''
Created on 14.11.2012

@author: cbalea
'''
from cms.pages.content_project_pages_cms import ContentProjectsPageCMS
from cms.pages.entities_pages_cms import EntitiesPageCMS
from cms.tests.base_cms_tests import SeleniumTestBaseCMS
from utils.random_generators import RandomGenerators


class TestEntitiesCMS(SeleniumTestBaseCMS):
    
    entityName = RandomGenerators().generateRandomString(5)
    entity = entityName
    
    def test_attachingEntityWithNoLogoWorks(self):
        entitiesPage = EntitiesPageCMS(self.driver, self.wait)
        entity = entitiesPage.clickAddEntity()
        entity.typeName(self.entity)
        entity.clickSaveButton()
        contProjs = ContentProjectsPageCMS(self.driver, self.wait)
        project = contProjs.clickContentProjectByIndex(1)
        project.clickShowHideBrandAndRequiredAttributionsLink()
        project.selectRoleByIndex(1)
        project.selectEntityByValue(self.entity)
        project = project.clickSaveAndContinueEditingButton()
        self.assertTrue(project.getTitle()!=None, "Project with no-logo-entity not added correctly")
    
    
    def test_removeEntity(self):
        entitiesPage = EntitiesPageCMS(self.driver, self.wait)
        entitiesPage.search_in_searchbar(self.entity)
        entitiesPage = EntitiesPageCMS(self.driver, self.wait, "noReload")
        entitiesPage.clickCheckboxForItem(self.entity)
        deletePage = entitiesPage.selectDeleteAction()
        newPage = deletePage.clickConfirmationButton()
        self.assertFalse(newPage.elementExistsByLinkText(self.entity), "Entity not deleted")
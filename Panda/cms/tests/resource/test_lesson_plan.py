#'''
#Created on Nov 14, 2012
#
#@author: jseichei
#'''
#from cms.pages.resource.resources_pages_cms import EditAddResourcePageCMS
#from cms.tests.base_cms_tests import SeleniumTestBaseCMS
#from utils.random_generators import RandomGenerators
#from utils.server_related import ServerRelated
#
#
#class TestLessonPlanCMS(SeleniumTestBaseCMS):  
#    
#    title = RandomGenerators().generateRandomString(5)   
#    res_type = "Lesson Plan"
#    
#    
#    def test_addLessonPlan(self):
#        role_level_1 = "Contributor"
#        entity_level_1 = "PBS LearningMedia"
#        asset = 'a'
#        
#        self.driver.get(ServerRelated().serverToBeTested() + "/admin/cms/resource/add/")
#        lessonPlan = EditAddResourcePageCMS(self.driver, self.wait) 
#        lessonPlan.selectContentProjectByIndex(1)
#        lessonPlan.typeTitle(self.title)
#        lessonPlan.selectType(self.res_type)
#        editLessonPlan = lessonPlan.clickSaveAndContinueEditingButton()
#        editLessonPlan.showHideAttribution()
#        editLessonPlan.selectAttributionRole(1, role_level_1)
#        editLessonPlan.selectAttributionEntity(1, entity_level_1)
#        editLessonPlan.showHidePrimaryAssets()
#        addAssets = editLessonPlan.searchForAsset(asset)
#        addAssets.clickCheckboxByIndex(1)
#        addAssets.clickCheckboxByIndex(2)
#        editLessonPlan = addAssets.clickAddAssetButton()
#        editLessonPlan.setAssetOrder(1, 2)
#        editLessonPlan.setAssetOrder(2, 1)
#        editLessonPlan = editLessonPlan.clickSaveAndContinueEditingButton()
#        editLessonPlan.showHidePrimaryAssets()
#        editLessonPlan.showHideAttribution()
#        self.assertEqual(editLessonPlan.getTitle(), self.title, "Lesson Plan was not saved")
#        self.assertEqual(editLessonPlan.getAttributionRole(1), role_level_1, "Attribution role was not saved")
#        self.assertEqual(editLessonPlan.getAttributionEntity(1),  entity_level_1, "Attribution entity not saved")
#        self.assertEquals(editLessonPlan.getSelectedType(), self.res_type, "Lesson Plan type not selected")
##        self.assertEquals(editLessonPlan.getAssetOrder(1), "1", "Asset order not correctly saved")
##        self.assertEquals(editLessonPlan.getAssetOrder(2), "2", "Asset order not correctly saved")
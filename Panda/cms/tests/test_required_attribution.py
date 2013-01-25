'''
Created on Oct 31, 2012

@author: jseichei
'''
from cms.pages.required_attribution_page import RequiredAttributionPageCMS
from cms.tests.base_cms_tests import SeleniumTestBaseCMS
from utils.random_generators import RandomGenerators


class TestRequiredAttributionCMS(SeleniumTestBaseCMS):
    
    role = "Funder"
    text = RandomGenerators().generateRandomString(30)
    
    def test_addRequiredAttribution(self):
        
        requiredAttribution = RequiredAttributionPageCMS(self.driver, self.wait)
        addRequiredAttribution = requiredAttribution.clickToAddRequiredAttributionButton()
        addRequiredAttribution.selectEntity()
        addRequiredAttribution.selectRole(self.role)
        addRequiredAttribution.writeInTextArea(self.text)
        saveAndContinueRequired = addRequiredAttribution.clickToSaveAndContinue()
        self.assertEqual(saveAndContinueRequired.getSelectedRole(), self.role, "role was not selected")
        self.assertTrue(saveAndContinueRequired.getSelectedEntity(), "Entity was not selected")
        
        
        
        
        
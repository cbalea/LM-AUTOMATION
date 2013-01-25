'''
Created on 24.09.2012

@author: cbalea
'''
from cms.pages.base_page_cms import BasePageCMS
from cms.pages.media.html_fragments_page_cms import EditHtmlFragmentsPage
from selenium.webdriver.support.select import Select
from utils.server_related import ServerRelated

class ResourcesPagesCMS(BasePageCMS):
    
    def __init__(self, driver, wait, filtered=None):
        self.driver = driver
        self.wait = wait
        if(filtered == None):
            self.driver.get(ServerRelated().serverToBeTested() + "/admin/cms/resource/")
        self.paginator = self.wait.until(lambda driver : driver.find_element_by_xpath("//p[@class='paginator']"))
    

    def clickOnResource(self, resource):
        self.clickLastPageInPaginatorIfExists()
        self.clickOnLink(resource)
        return EditAddResourcePageCMS(self.driver, self.wait)
    
    def clickOnResourceByIndex(self, index):
        self.clickItemInListTableByIndex(index)
        return EditAddResourcePageCMS(self.driver, self.wait)
    
    def filterViewBy(self, filterBy):
        self.clickOnLink(filterBy)
        return ResourcesPagesCMS(self.driver, self.wait, "filtered")
    
    def selectAddResourcesToCollection(self):
        action = Select(self.wait.until(lambda driver : driver.find_element_by_xpath("//select[@name='action']")))
        action.select_by_visible_text("Add resources to collection")
        goButton = self.wait.until(lambda driver : driver.find_element_by_xpath("//button[text()='Go']"))
        goButton.click()
        self.switchToNewestWindow()



class EditAddResourcePageCMS(BasePageCMS):
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.title = self.wait.until(lambda driver : driver.find_element_by_id("id_title"))
        self.contentProjectCombobox = Select(self.wait.until(lambda driver : driver.find_element_by_id("id_content_project")))
        self.typeCombobox = Select(self.wait.until(lambda driver : driver.find_element_by_id("id_type")))

    def clickCHExpandLink(self):
        self.chExpandLink = self.wait.until(lambda driver : driver.find_element_by_xpath("//h2[text()='Curriculum Hierarchy']/a"))
        self.chExpandLink.click()
    
    def selectCHNodesRoot(self, root):
        self.chNodesRootCombobox = Select(self.wait.until(lambda driver : driver.find_element_by_id("root_ch_nodes")))
        self.chNodesRootCombobox.select_by_visible_text(root)
    
    def clickCHTreeExpanderByLabel(self, label):
        xpath =  "//span/a[text()='%s']/../span[@class='dynatree-expander']" %label
        self.chTreeExpander = self.wait.until(lambda driver : driver.find_element_by_xpath(xpath)).click()
    
    def clickCHCheckboxByLabel(self, label):
        xpath = "//span/a[text()='%s']/../span[@class='dynatree-checkbox']" %label
        self.chTreeExpander = self.wait.until(lambda driver : driver.find_element_by_xpath(xpath)).click()
    
    def getCHCheckboxStatusByLabel(self, label):
        xpath = "//span/a[text()='%s']/.." %label
        self.chTreeExpander = self.wait.until(lambda driver : driver.find_element_by_xpath(xpath))
        label = self.chTreeExpander.get_attribute("class")
        return label.index("dynatree-selected")
    
    def getTitle(self):
        return self.title.get_attribute("value")
    
    def clickSaveButton(self):
        self.clickSave()
        return EditAddResourcePageCMS(self.driver, self.wait)
    
    def clickSaveAndContinueEditingButton(self):
        self.clickSaveAndContinueEditing()
        return EditAddResourcePageCMS(self.driver, self.wait)
    
    def clickAddButton(self):
        self.addButton = self.wait.until(lambda driver : driver.find_element_by_id("add_btn"))
        self.addButton.click()
    
    def getCHAttachedNode(self):
        self.attachedCHNode = self.wait.until(lambda driver : driver.find_element_by_xpath("//tbody[@id='ch_table_container']/tr"))
        return self.attachedCHNode.text
    
    def selectStandardsAlignmentState(self, state):
        self.state = Select(self.wait.until(lambda driver : driver.find_element_by_id("selectstate")))
        self.state.select_by_visible_text(state)
    
    def getNumberOfAttachedStandards(self):
        self.standards = self.wait.until(lambda driver : driver.find_elements_by_xpath("//div[@id='ch_inline_content']/table/tbody/tr[@style='']"))
        return len(self.standards)
    
    def typeTitle(self, title):
        self.title.send_keys(title)
    
    def selectContentProjectByIndex(self, index):
        self.contentProjectCombobox.select_by_index(index)
    
    def selectType(self, res_type):
        self.typeCombobox.select_by_visible_text(res_type)
    
    def showHideAttribution(self):
        linkAttribution = self.wait.until(lambda driver : driver.find_element_by_xpath(".//h2[contains(text(), 'Attributions')]/a"))
        linkAttribution.click()
    
    def selectAttributionRole(self, selectLevelRole, role):
        attributionRole = Select(self.wait.until(lambda driver : driver.find_element_by_xpath(".//tr[%d]/td[2][@class='req_attr_role']/select" %selectLevelRole)))
        attributionRole.select_by_visible_text(role)
    
    def getAttributionRole(self, levelRole):
        attributionRoleGet = Select(self.wait.until(lambda driver : driver.find_element_by_xpath(".//tr[%d]/td[2][@class='req_attr_role']/select" %levelRole)))
        return attributionRoleGet.first_selected_option.text
    
    def selectAttributionEntity(self, selectLevelEntity, entity):
        attributionEntity = Select(self.wait.until(lambda driver : driver.find_element_by_xpath("//tr[%d]/td[3]/select[@class='entity_select']" %selectLevelEntity)))
        attributionEntity.select_by_visible_text(entity)
    
    def getAttributionEntity(self, levelEntity):
        attributionEntityGet = Select(self.wait.until(lambda driver : driver.find_element_by_xpath("//tr[%d]/td[3]/select[@class='entity_select']" %levelEntity))) 
        return attributionEntityGet.first_selected_option.text
       
    def showHidePrimaryAsset(self):
        link = self.wait.until(lambda driver : driver.find_element_by_xpath("//h2[contains(text(), 'Primary Asset')]/a"))
        link.click()
        
    def searchForAsset(self, asset):
        searchBox = self.wait.until(lambda driver : driver.find_element_by_xpath("//div[@class='asset_box_primary']/div/div/input"))
        searchBox.send_keys(asset)
        self.clickOnLink("Search")
        self.switchToNewestWindow()
        return AssetSelectionInResourcePageCMS(self.driver, self.wait)
    
    def getSelectedType(self):
        return self.typeCombobox.first_selected_option.text

    def orderBox(self, assetIndex):
        return self.wait.until(lambda driver:driver.find_element_by_xpath("//tr[%d]/td[@class='field-order']/input" %assetIndex))

    def setAssetOrder(self, assetIndex, order):
        self.orderBox(assetIndex).clear()
        self.orderBox(assetIndex).send_keys(order)

    def getAssetOrder(self, assetIndex):
        return self.orderBox(assetIndex).get_attribute("value")

    def getResourceCode(self):
        code = self.wait.until(lambda driver:driver.find_element_by_id("id_resource_code"))
        return code.get_attribute("value")
    
    def getResourceSlug(self):
        slug = self.wait.until(lambda driver:driver.find_element_by_id("id_slug"))
        return slug.get_attribute("value")
    
    def clickShowSupportMaterialsLink(self):
        showSupportMaterialsLink= self.wait.until(lambda driver : driver.find_element_by_xpath("//h2[text()='Support Materials']/a"))
        showSupportMaterialsLink.click()

    def clickAddBackgroundEssayButton(self):
        addTextBtn = self.wait.until(lambda driver:driver.find_element_by_id("add_text_background-essay"))
        addTextBtn.click()
        self.switchToNewestWindow()
        return EditHtmlFragmentsPage(self.driver, self.wait)
    
    def isBackgroundEssayAttached(self, name):
        return  self.elementExistsByXpath("//tbody[@id='category_container_background-essay']/tr/td[text()='%s']" %name)
        
    def getPrimaryAssetSectionContent(self):
        content = self.wait.until(lambda driver:driver.find_element_by_id("primary_asset_display"))
        return content.text
        


class AssetSelectionInResourcePageCMS(BasePageCMS):
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
    
    def clickAddAssetButton(self):
        addAssetButton = self.wait.until(lambda driver : driver.find_element_by_id("resource_add_asset"))
        addAssetButton.click()
        self.switchToNewestWindow()
        return EditAddResourcePageCMS(self.driver, self.wait)

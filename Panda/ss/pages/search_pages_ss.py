'''
Created on 31.10.2012

@author: cbalea
'''
from ss.pages.base_page_ss import BasePageSS


class SearchResultsPageSS(BasePageSS):
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.displayedResults =  self.wait.until(lambda driver : driver.find_elements_by_xpath("//div[@class='pbscustom multiresource-single-item-content']/a[contains(@href, '/resource/')]"))
        self.descriptions =  self.wait.until(lambda driver : driver.find_elements_by_xpath("//div[@class='pbscustom multiresource-single-item-content']/a[contains(@href, '/resource/')]/../p"))
        self.gradesForEachResult = self.wait.until(lambda driver : driver.find_elements_by_xpath("//div[@class='pbscustom multiresource-single-item-content']/p[contains(text(), 'Grades')]"))
        self.gradeFacetsLinks = self.wait.until(lambda driver : driver.find_elements_by_xpath("//div/h5[contains(text(), 'Grades')]/../../div/dl/dd/a"))
        self.gradeFacets = self.wait.until(lambda driver : driver.find_elements_by_xpath("//div/h5[contains(text(), 'Grades')]/../../div/dl/dd"))
        self.resultsPanel = self.wait.until(lambda driver : driver.find_element_by_xpath("//section[@class='pbscustom panel multiresource']"))

    def favStars(self):
        return self.wait.until(lambda driver : driver.find_elements_by_xpath("//span[@class='favorites']/i"))
       

        

    def clickFavoriteStarForResult(self, index):
        self.favStars()[index-1].click()

    def isFavorited(self, index):
        return self.isFavoritedStarClicked(self.favStars()[index-1])
    
    def getNumberOfPages(self):
        whole_text = self.resultsPanel.text
        try:
            start = whole_text.index("Pages: ") + len ("Pages: ")
            numberOfPages = whole_text[start : (start+3)]
            return int(numberOfPages)
        except: # If "Pages" doesn't appear, it is the only page
            return 1

    def getNumberOfSearchRestuls(self):    
        return self.getNumberOfPages() * self.getNumberOfResultsPerPage()
    
    def getNumberOfResultsPerPage(self):
        return len(self.displayedResults)
    
    def clickFacet(self, faceteLinksList, index):
        faceteLinksList[index].click()
        return SearchResultsPageSS(self.driver, self.wait)
    
    def getNumberOfResultsForFacet(self, facetList, index):
        text = facetList[index].text
        number = text[text.find("(") + 1 : text.find(")")]
        return int(number)
    
    def clickFirstFacetWithFewerResultsThanFullSearch(self, facetsList, facetLinksList):
        i=0
        for facet in facetsList:
            if(self.getNumberOfResultsForFacet(facetsList, i) < self.getNumberOfSearchRestuls()):
                return self.clickFacet(facetLinksList, i)
            i+=1
        raise BaseException ("There are no facets which return fewer results than full search")
    
    def getResultTitle(self, index):
        return self.displayedResults[index].text

    def getResultDescription(self, index):
        return self.descriptions[index].text
    
    def getResultGrades(self, index):
        return self.gradesForEachResult[index].text
    
    def getDisplayedGradeFacets(self):
        grades = []
        for grade in self.gradeFacetsLinks:
            grades.append(grade.text)
        return grades
    
    def getNumberOfDisplayedGradeFacets(self):
        return len(self.gradeFacetsLinks)
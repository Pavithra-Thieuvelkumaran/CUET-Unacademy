from selenium.webdriver.common.by import By


class LandingPageClass:


    def __init__(self, driver):
        self.driver = driver

        # Element Locators Values
    #    self.StartLearningLinkElement = "//button[@class='e3x32mw6 aquilla-button button css-1cghvhx-StyledStartLearning']"
        self.CuetLinkElement = "//a[@class=' e1duax855 css-188v8i1-StyledAnchor-StyledLink eyp81ai0']/h4"
        self.CuetLangLinkElement="//p[@class='css-13n8k7n-P1 e5hgzks0']//span[contains(text(),'CUET (L')]"
        self.SearchLinkElement="//input[@placeholder='Search for your goal']"
        self.Educators="//a[normalize-space()='Educators']/div"
        self.Batch="//div[normalize-space()='Batch']"
        self.FreeVideosLinkElement="//h5[contains(text(),'CUET 2023 Verbal Ability | Most Expected Questions')]"
        self.ViewProfileLinkElement="//*[@id='educatorsSection']/div[3]/div[1]/a/div[1]/div/div[1]/div/img"
    #def click_startlearning_link(self):
     #   StartLearningLink = self.driver.find_element(By.XPATH, self.StartLearningLinkElement)
      #  StartLearningLink.click()

        # Clicking CUET

    def click_cuet_link(self):
        CuetLink = self.driver.find_element(By.XPATH, self.CuetLinkElement)
        #self.driver.execute_script("window.scrollBy(0,1000);")
        CuetLink.click()

    def click_cuet_lang_link(self):
        CuetLangLink = self.driver.find_element_by_xpath(self.CuetLangLinkElement)
        self.driver.execute_script("arguments[0].click();", CuetLangLink)
    def click_search_link(self,val):
        SearchLink=self.driver.find_element(By.XPATH, self.SearchLinkElement)
        SearchLink.send_keys(val)
    def click_educators_link(self):
        EducatorsLink=self.driver.find_element(By.XPATH,self.Educators)
        EducatorsLink.click()
    def click_batch_link(self):
        BatchLink=self.driver.find_element(By.XPATH,self.Batch)
        BatchLink.click()
    def click_freevideos_link(self):
        FreeVideosLink=self.driver.find_element_by_xpath(self.FreeVideosLinkElement)
        self.driver.execute_script("arguments[0].click();",FreeVideosLink)
    def click_viewprofile_link(self):
        ViewProfileLink=self.driver.find_element_by_xpath(self.ViewProfileLinkElement)
        self.driver.execute_script("arguments[0].click();",ViewProfileLink)
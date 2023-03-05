from selenium import webdriver
from features.utility.ConfigClass import ConfigClass

class UtilityClass:

    def __init__(self, driver):
        self.driver = driver

    def launch_browser(self):
        self.driver = webdriver.Chrome(ConfigClass.filePath)

    def launch_app(self):
        self.driver.get(ConfigClass.url)

    def launch_page(self):
        self.driver.get(ConfigClass.url1)

    def max_win(self):
        self.driver.maximize_window()


    def close_browser(self):
        self.driver.quit()
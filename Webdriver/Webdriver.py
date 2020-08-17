from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Webdriver:

    def __init__(self):
        self.initializeChromeWebDriver()

    def initializeChromeWebDriver(self):
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(executable_path='Webdriver\chromedriver.exe.', chrome_options=options)
        return driver

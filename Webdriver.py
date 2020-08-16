from selenium import webdriver

class Webdriver:

    def __init__(self):
        self.initializeChromeWebDriver()


    def initializeChromeWebDriver(self):
        driver = webdriver.Chrome('D://Python projects//StockMonitor//chromedriver_win32chromedriver.exe')
        return driver

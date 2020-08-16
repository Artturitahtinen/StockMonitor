from selenium import webdriver

class Webdriver:

    def __init__(self):
        self.initializeChromeWebDriver()


    def initializeChromeWebDriver(self):
        driver = webdriver.Chrome(executable_path='D:/Python projects/StockMonitor/chromedriver_win32/chromedriver.exe')
        return driver

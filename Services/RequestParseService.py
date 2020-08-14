import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import sys

class RequestParseService:

    def __init__(self, url):
        self.url = url

    def parseRequest(self):
        try:
            requests.get(self.url)
        except requests.ConnectionError:
            print('Connection error')   

        driver = webdriver.Chrome('D:\Python projects\StockMonitor\chromedriver_win32\chromedriver.exe')
        driver.get(self.url)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'lxml')
        time.sleep(2)
        try:
            accept_button_selector = driver.find_element_by_id('almacmp-modalConfirmBtn').click()
        except:
            print("Did not find accept button, exiting program")
            sys.exit()

        time.sleep(2)
        try:
            sell_price_label = driver.find_elements_by_class_name('card-label')[3].get_attribute('innerHTML')
        except:
            print("Did not find sell price label, exiting program")
            sys.exit()

        try:
            sell_price = driver.find_elements_by_class_name('card-value')[5].find_elements_by_class_name('monospace')[0].get_attribute('innerHTML')
        except:  
            print("Did not find sell price, exiting program")
            sys.exit()  

        print(sell_price_label)
        print(sell_price)

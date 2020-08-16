import requests
from bs4 import BeautifulSoup
import time
import sys

class RequestParseService:

    def __init__(self, url, driver):
        self.url = url
        self.driver = driver

    def parseRequest(self):
        try:
            requests.get(self.url)
        except requests.ConnectionError:
            print('Connection error')   

        self.driver.get(self.url)
        page_source = self.driver.page_source
        soup = BeautifulSoup(page_source, 'lxml')
        time.sleep(2)
        try:
            accept_button_selector = self.driver.find_element_by_id('almacmp-modalConfirmBtn').click()
        except:
            print("Did not find accept button, exiting program")
            sys.exit()

        time.sleep(2)
        try:
            sell_price_label = self.driver.find_elements_by_class_name('card-label')[3].get_attribute('innerHTML')
        except:
            print("Did not find sell price label, exiting program")
            sys.exit()

        try:
            sell_price = self.driver.find_elements_by_class_name('card-value')[5].find_elements_by_class_name('monospace')[0].get_attribute('innerHTML')
        except:  
            print("Did not find sell price, exiting program")
            sys.exit()  

        print(sell_price_label)
        print(sell_price)

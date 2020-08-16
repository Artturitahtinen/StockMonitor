import requests
from bs4 import BeautifulSoup
import time
import sys
import Services.LoggingService

class Request_parse_service:

    parse_requests = 0

    def __init__(self, url, driver):
        self.url = url
        self.driver = driver
        Request_parse_service.parse_requests += 1

    def parse_request(self):
        try:
            requests.get(self.url)
        except requests.ConnectionError:
            Services.LoggingService.('Connection error')   

        self.driver.get(self.url)
        page_source = self.driver.page_source
        soup = BeautifulSoup(page_source, 'lxml')
        time.sleep(2)

        if(Request_parse_service.parse_requests == 1):
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

        sell_price = sell_price.replace(',', '.')
        sell_price = float(sell_price)
        return sell_price


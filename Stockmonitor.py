from Services.Request_parse_service import Request_parse_service
from Webdriver.Webdriver import Webdriver
from Services.Mail_service import Mail_service
import numpy as np
import configparser
config= configparser.ConfigParser()
config.read(r'D:/Python projects/StockMonitor/Configs/config.ini')

sender_email = config['MAIL']['sender_email']
password = config['MAIL']['password']
recipient_email = config['MAIL']['recipient_email']
smtp_server = config['MAIL']['smtp_server']
port = config['MAIL']['port']

stock_urls = {
    'orionB_url': 'https://www.kauppalehti.fi/porssi/porssikurssit/osake/ORNBV',
    'konecranes_url': 'https://www.kauppalehti.fi/porssi/porssikurssit/osake/KCR',
    'nordeaBank_url': 'https://www.kauppalehti.fi/porssi/porssikurssit/osake/NDA%20FI',
    'outokumpu_url': 'https://www.kauppalehti.fi/porssi/porssikurssit/osake/OUT1V',
    'sampoA_url': 'https://www.kauppalehti.fi/porssi/porssikurssit/osake/SAMPO'
}
companies_sell_labels = ['Orion B sell price','Konecranes sell price','Nordea Bank sell price','Outokumpu','Sampo A']
sell_prices = []
increase = [1.40, 1.50, 1.50, 1.50, 1.50]
target_prices = [55.58, 30.33, 10.22, 3.315, 38.955]

stocks = {
    'Orion B': {
        'sell_prices': 0.0,
        'increase': 0.40,
        'target_price': 55.58
    },
    'Konecranes': {
        'sell_prices': 0.0,
        'increase': 0.50,
        'target_price': 30.33
    },
    'Nordea Bank': {
        'sell_prices': 0.0,
        'increase': 0.50,
        'target_price': 10.22
    },
    'Outokumpu': {
        'sell_prices': 0.0,
        'increase': 0.50,
        'target_price': 3.315
    },
    'Sampo A': {
        'sell_prices': 0.0,
        'increase': 0.50,
        'target_price': 38.955
    }    
}



def main():
    #Initialize chromedriver
    driver = Webdriver()
    g_driver = driver.initializeChromeWebDriver()

    #Get all sell prices from stock urls
    for key, value in stock_urls.items():
        rps = Request_parse_service(value, g_driver)
        sell_price = rps.parse_request()
        sell_prices.append(sell_price)

    sell_prices_to_dict(sell_prices, stocks)

    #if(check_mail_send_conditions(sell_prices, target_prices)):
    #   mail_service = Mail_service(stock_dict, sender_email, recipient_email, smtp_server, port)
    #   mail_service.send_email()
    
def sell_prices_to_dict(sell_prices, stocks):
    iter_sell_prices_list = iter(sell_prices)
    for key, value in stocks.items():
        print(key, value)

if __name__ == "__main__":
    main()
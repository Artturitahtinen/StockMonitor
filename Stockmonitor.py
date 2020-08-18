from Services.Request_parse_service import Request_parse_service
from Webdriver.Webdriver import Webdriver
from Services.Mail_service import Mail_service

stock_urls = {
    'orionB_url': 'https://www.kauppalehti.fi/porssi/porssikurssit/osake/ORNBV',
    'konecranes_url': 'https://www.kauppalehti.fi/porssi/porssikurssit/osake/KCR',
    'nordeaBank_url': 'https://www.kauppalehti.fi/porssi/porssikurssit/osake/NDA%20FI',
    'outokumpu_url': 'https://www.kauppalehti.fi/porssi/porssikurssit/osake/OUT1V',
    'sampoA_url': 'https://www.kauppalehti.fi/porssi/porssikurssit/osake/SAMPO'
}
stocks = {
    'Orion B': {'sell_price': 0.0, 'target_price': 5.58, 'increase': 40, 'increased_over': False},
    'Konecranes': {'sell_price': 0.0, 'target_price': 3.33, 'increase': 50, 'increased_over': False},
    'Nordea Bank': {'sell_price': 0.0, 'target_price': 10.22, 'increase': 50, 'increased_over': False},
    'Outokumpu': {'sell_price': 0.0, 'target_price': 3.315, 'increase': 50, 'increased_over': False},
    'Sampo A': {'sell_price': 0.0, 'target_price': 38.955, 'increase': 50, 'increased_over': False}    
}
#target_prices = [55.58, 30.33, 10.22, 3.315, 38.955]
sell_prices = []

def main():
    #Initialize chromedriver
    driver = Webdriver()
    g_driver = driver.initializeChromeWebDriver()

    #Get all sell prices from stock urls
    for key, value in stock_urls.items():
        rps = Request_parse_service(value, g_driver)
        sell_price = rps.parse_request()
        sell_prices.append(sell_price)

    updated_stocks = sell_prices_to_dict(sell_prices, stocks)
    filtered_stocks = filter_stocks(updated_stocks)
    is_empty_dict = not bool(filtered_stocks)

    #If stock dictionary is not empty => send email
    if not is_empty_dict:
        mail_service = Mail_service(filtered_stocks)
        mail_service.send_email()
    
def sell_prices_to_dict(sell_prices, stocks):
    sell_prices_iterator = iter(sell_prices)
    for key, value in stocks.items():
        value['sell_price'] = next(sell_prices_iterator)
    return stocks

#Set increased_over to True if sell_price is greater or equal to target_price
def filter_stocks(updated_stocks):
    for key, value in updated_stocks.items():
        if value['sell_price'] >= value['target_price']:
            value['increased_over'] = True

    #Delete dictionaries where increased_over is False
    updated_stocks = {k:v for (k, v) in updated_stocks.items() if v['increased_over'] == True}
    
    return updated_stocks

if __name__ == "__main__":
    main()
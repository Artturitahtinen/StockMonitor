from Services.Request_parse_service import Request_parse_service
from Webdriver.Webdriver import Webdriver
from Services.Mail_service import Mail_service


stock_urls = {
    'fortumUrl': 'https://www.kauppalehti.fi/porssi/porssikurssit/osake/FORTUM',
    'koneCranesUrl': 'https://www.kauppalehti.fi/porssi/porssikurssit/osake/KCR',
    'nordeaBank': 'https://www.kauppalehti.fi/porssi/porssikurssit/osake/NDA%20FI',
    'outokumpu': 'https://www.kauppalehti.fi/porssi/porssikurssit/osake/OUT1V',
    'sampoA': 'https://www.kauppalehti.fi/porssi/porssikurssit/osake/SAMPO'
}
companies_sell_labels = ['Fortum sell price','Konecranes sell price','Nordea Bank sell price','Outokumpu','Sampo A']
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

    #Dictionary of company names and its sell price values
    stock_dict = make_dict()

    mail_service = Mail_service(stock_dict)
    mail_service.send_mail()
    
    

def make_dict():
    companies_sell_prices = dict(zip(companies_sell_labels, sell_prices))
    return companies_sell_prices

if __name__ == "__main__":
    main()
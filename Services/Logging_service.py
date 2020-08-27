import logging

logging.basicConfig(filename='Logs/Stock_prices.log', level=logging.INFO, format='%(asctime)s - %(levelname)s : %(message)s', datefmt='%d.%m.%Y %I:%M:%S')

def log_prices_by_company(stocks):
    for key, value in stocks.items():
        logging.info(
        '\n{company} \n   sell price: {sell_price} € \n   target price: {target_price} € \n---------------------------------'.format(company = key, sell_price = value['sell_price'], target_price = value['target_price']))
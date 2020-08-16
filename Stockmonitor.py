from Services.RequestParseService import RequestParseService
from Webdriver import Webdriver

fortumUrl = 'https://www.kauppalehti.fi/porssi/porssikurssit/osake/FORTUM'


driver = Webdriver()
gDriver = driver.initializeChromeWebDriver()


rps = RequestParseService(fortumUrl, gDriver)
rps.parseRequest()
from Services.RequestParseService import RequestParseService

fortumUrl = 'https://www.kauppalehti.fi/porssi/porssikurssit/osake/FORTUM'

rps = RequestParseService(fortumUrl)
rps.parseRequest()
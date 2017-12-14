import requests
import json

class Wrapper(object):

	__DEFAULT_URL = 'https://api.coinmarketcap.com/v1/' # default url for coinmarketcap
	__DEFAULT_TIMEOUT = 120 # default timeout in seconds


	def __init__(self, default_url=__DEFAULT_URL, timeout=__DEFAULT_TIMEOUT):
		"""
		Initializes the variables for the program
		"""
		self.base_url = default_url
		self.timeout = timeout


	def getInfo(self, coin, info):
		"""
		Returns the specified data for a coin
		"""
		tickerInfo = self.tickers(coin)[0][info]
		print tickerInfo


	def tickerInfoAvailable(self, coin):
		"""
		Returns the type of information you can get from the ticker method
		"""
		temp = []
		for data in self.tickers(coin):
			for category in data:
				temp.append(category)
		return temp


	def tickers(self, coin, **params):
		"""
		Returns the ticker for all coins unless specified differently.


		Optional parameters:

			(int) start - return results from rank [start] and above

			(int) limit - return a maximum of [limit] results 
						  (default is 100, use 0 to return all results)

			(string) convert - return price, 24h volume, and market cap 
							   in terms of another currency. 
							   
							   Valid values are:
							   "AUD", "BRL", "CAD", "CHF", "CLP", "CNY", 
							   "CZK", "DKK", "EUR", "GBP", "HKD", "HUF", 
							   "IDR", "ILS", "INR", "JPY", "KRW", "MXN", 
							   "MYR", "NOK", "NZD", "PHP", "PKR", "PLN", 
							   "RUB", "SEK", "SGD", "THB", "TRY", "TWD", 
							   "ZAR"
		"""
		url = self.base_url + 'ticker/' # set url to ticker page

		if coin.lower() != 'all':
			url = url + coin + '/'
		
		if params:
			r = requests.get(url, params=params)
		else:
			r = requests.get(url)

		return r.json()

		
#################################### FOR TESTING ####################################
W = Wrapper()

# How to use the getInfo method
print W.getInfo('Ethereum', 'rank')

# How to use the tickerInfoAvailable method
#W.tickerInfoAvailable('Ethereum')


# How to use the tickers method
arguments = {
			#'start' : 1,
			#'limit' : 1,
			#'convert' : 'AUD'
			}
#print W.tickers('all', **(arguments))


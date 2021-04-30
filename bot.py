from binance.client import Client
import pandas as pd

apiKey = ''
secretKey = ''

client = Client(apiKey, secretKey)

#tickers = client.get_orderbook_tickers()
orderbook = client.get_avg_price(symbol='ETHUSDT')

print(orderbook['price'])
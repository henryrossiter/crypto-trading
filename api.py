import robin_stocks as r

def getTradeableCryptoList():
  data = r.crypto.get_crypto_currency_pairs()
  return [crypto for crypto in data if not crypto['display_only']]
  
def getCryptoPositions():
  positions = r.get_crypto_positions()
  return positions

def getCryptoQuote(symbol):
  quote = r.get_crypto_quote(symbol)
  return quote

def buyCrypto(symbol, usd):
  resp = r.orders.order_buy_crypto_by_price(symbol, usd)
  return resp

def sellCrypto(symbol, usd):
  resp = r.orders.order_sell_crypto_by_price(symbol, usd)
  return resp

def getHistoricals(symbol, span='year'):
  symbol_dict = {
    'BTC': '3d961844-d360-45fc-989b-f6fca761d511',
    'ETH': '76637d50-c702-4ed1-bcb5-5b0732a81f48',
    'LTC': '383280b1-ff53-43fc-9c84-f01afd0989cd',
    'BCH': '2f2b77c4-e426-4271-ae49-18d5cb296d3a',
    'DOGE': '1ef78e1b-049b-4f12-90e5-555dcf2fe204',
    'ETC': '7b577ce3-489d-4269-9408-796a0d1abb3a',
    'BSV': '086a8f9f-6c39-43fa-ac9f-57952f4a1ba6'
  }
  if span == 'year':
    data = r.helper.request_get('https://api.robinhood.com/marketdata/forex/historicals/{}/?bounds=24_7&interval=day&span=year'.format(symbol_dict[symbol]))
  elif span == 'month':
    data = r.helper.request_get('https://api.robinhood.com/marketdata/forex/historicals/{}/?bounds=24_7&interval=hour&span=month'.format(symbol_dict[symbol]))
  elif span == 'week':
    data = r.helper.request_get('https://api.robinhood.com/marketdata/forex/historicals/{}/?bounds=24_7&interval=hour&span=week'.format(symbol_dict[symbol]))
  else:
    data = None
  return data


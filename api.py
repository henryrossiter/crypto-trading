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

def getHistoricals(symbol):
  resp = r.stocks.get_historicals(symbol)
  return resp


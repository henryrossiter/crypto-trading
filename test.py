import auth
import api
import pprint
pp = pprint.PrettyPrinter(indent=4)

auth.login()

data = api.getHistoricals('BTC')
pp.pprint(data)

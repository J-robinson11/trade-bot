import alpaca_api

trade_api = alpaca_api()
# Example usage
data = trade_api.get_hist_data()
data["BTC/USD"]
# Access bars for BTC/USD
print(data["BTC/USD"])


#def trading_algo():
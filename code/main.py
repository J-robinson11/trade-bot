from alpaca_api import get_account_info
from alpaca.trading.client import TradingClient

# paper=True enables paper trading
trading_client = TradingClient('api-key', 'secret-key', paper=True)

def main():
    account_info = get_account_info()
    print(account_info)
    # Add more trading logic here

if __name__ == "__main__":
    main()
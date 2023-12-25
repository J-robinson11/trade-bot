import requests
from config import ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_PAPER_URL
from alpaca.trading.client import TradingClient
from alpaca.data import CryptoHistoricalDataClient,StockHistoricalDataClient
import pandas as pd
from alpaca.data.timeframe import TimeFrame
from datetime import datetime 
from alpaca.trading.requests import MarketOrderRequest, LimitOrderRequest, GetOrdersRequest
from alpaca.trading.enums import OrderSide, TimeInForce, QueryOrderStatus

crypto_client = CryptoHistoricalDataClient()
trade_client = TradingClient(ALPACA_API_KEY,ALPACA_SECRET_KEY, paper = True)
stock_client = StockHistoricalDataClient()


def get_account_info():
    url = f"{ALPACA_PAPER_URL}/v2/account"
    headers = {
        "APCA-API-KEY-ID": ALPACA_API_KEY,
        "APCA-API-SECRET-KEY": ALPACA_SECRET_KEY
    }
    response = requests.get(url, headers=headers)
    return response.json()


#################
## RETRIEVE DATA
#################

#def retrieve_acc_details():

def get_all_order():
    request_params = GetOrdersRequest(
                    status=QueryOrderStatus.OPEN,
                    side=OrderSide.SELL
                 )

# orders that satisfy params
    orders = trade_client.get_orders(filter=request_params)
    return orders


#def stream_trade_updates():

def get_hist_data(symb):
    request_params = crypto_client.get_crypto_bars(
        symbol_or_symbols=[symb],
        timeframe = TimeFrame.Day,
        start = datetime(2000,1,1),
        end   = datetime(2023,12,20)
    )

    data = crypto_client.get_crypto_bars(request_params)
    data.df
    return data



##########
## ORDERS
##########

def create_market_order():
    # preparing orders
    order_data = MarketOrderRequest(
                    symbol="BTC/USD",
                    qty=0.0001,
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.GTCd
                    )

    # Market order
    order = trade_client.submit_order(order_data=order_data)
    return "success"


#get_all_order_infor():


def order_kill_switch():
    cancel = trade_client.cancel_orders()
    return cancel

#cancel_order
#get_order

#############
## POSITIONS
#############

#def close_all_positions
#def close_position





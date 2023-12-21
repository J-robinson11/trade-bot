import requests
from config import ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_PAPER_URL

def get_account_info():
    url = f"{ALPACA_PAPER_URL}/v2/account"
    headers = {
        "APCA-API-KEY-ID": ALPACA_API_KEY,
        "APCA-API-SECRET-KEY": ALPACA_SECRET_KEY
    }
    response = requests.get(url, headers=headers)
    return response.json()
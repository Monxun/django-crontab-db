from django.conf import settings
import requests
import pprint
from cron.models import Stock, StockMarketData

def fetch_stock_market_data():
    headers = {
        "X_CMC_PRO_API_KEY": settings.CMC_API_KEY
    }

    resp = requests.get(settings.API_URL, headers=headers)

    data = resp.json()['data']
    pprint(data)
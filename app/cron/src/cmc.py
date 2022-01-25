import vectorbt as vbt
import requests
import pprint
import os
from django.conf import settings

def fetch_stock_market_data():
    headers = {
        "X_CMC_PRO_API_KEY": settings.CMC_API_KEY
    }

    resp = requests.get(settings.API_URL, headers=headers)

    data = resp.json()['data']
    pprint(data)
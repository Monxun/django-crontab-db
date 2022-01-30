import finnhub
from django.conf import settings
import pandas as pd
import requests
import config
from pprint import pprint

def fh_get_data(symbol):
    # Setup client
    finnhub_client = finnhub.Client(api_key=config.FINNHUB_API_KEY)

    # Stock candles
    res = finnhub_client.stock_candles(symbol, 'D', 1590988249, 1591852249)
    print(res)

    #Convert to Pandas Dataframe
    df = pd.DataFrame(res)

    return df

if __name__ == '__main__':
    df = fh_get_data('AAPL')

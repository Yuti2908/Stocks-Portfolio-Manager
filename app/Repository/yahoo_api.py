from yahoo_fin.stock_info import get_data
from datetime import datetime, timedelta
from flask import Flask

def get_yahoo_data(ticker):
    global raw_data
    app = Flask(__name__)
    current_date = datetime.now()
    yesterday = current_date + timedelta(days=-1)
    yesterday_date = (yesterday.strftime('%Y-%m-%d'))
    current_date = current_date.strftime('%Y-%m-%d')
    print("Yesterday date:", yesterday_date)
    print("Current date:", current_date)
    try:
        # Print the raw response to understand its structure
        raw_data = get_data(ticker, start_date=yesterday_date, end_date=current_date, index_as_date=True,interval='1d')
        print(type(raw_data))
        print((raw_data['close'].iloc[0]))
        return raw_data['close'].iloc[0]
    except Exception as e:
        print(e)
        return -1
    # return app


if __name__=='__main__':
    get_yahoo_data("aapl")
from app.Repository.holdings import fetch_all_holdings, insert_holding

def get_all_holdings():
    return fetch_all_holdings()

def add_holding(buyPrice, ticker, quantity):
    insert_holding(buyPrice, ticker, quantity)

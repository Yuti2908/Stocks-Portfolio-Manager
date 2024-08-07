from app.Repository.holdings import fetch_all_holdings, insert_holding

def get_all_holdings():
    return fetch_all_holdings()

def add_holding(data):
    insert_holding(data)

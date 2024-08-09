from app.Repository.transactions import fetch_all_transactions, insert_transaction

def get_all_transactions():
    return fetch_all_transactions()

def add_transaction(price, ticker, trans_type, quantity, date):
    insert_transaction(price, ticker, trans_type, quantity, date)

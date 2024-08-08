from app.Repository.watchlist import (
    fetch_all_short_term_stock_watchlists,
    fetch_all_long_term_stock_watchlists,
    insert_long_term_stock_watchlist,
    insert_short_term_stock_watchlist
)

def get_all_long_term_stock_watchlists():
    return fetch_all_long_term_stock_watchlists()

def get_all_short_term_stock_watchlists():
    return fetch_all_short_term_stock_watchlists()

def add_short_term_stock_watchlist(data):
    insert_short_term_stock_watchlist()

def add_long_term_stock_watchlist(data):
    insert_long_term_stock_watchlist()

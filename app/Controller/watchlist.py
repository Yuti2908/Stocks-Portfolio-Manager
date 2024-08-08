from flask import Blueprint, jsonify, request
from app.Services.watchlist import (
    get_all_short_term_stock_watchlists,
    get_all_long_term_stock_watchlists,
    add_long_term_stock_watchlist,
    add_short_term_stock_watchlist
)

watchlist_bp = Blueprint('watchlist', __name__)

@watchlist_bp.route('/long_term_stocks', methods=['GET'])
def fetch_long_term_stock_watchlists():
    watchlists = get_all_long_term_stock_watchlists()
    return jsonify(watchlists)

@watchlist_bp.route('/short_term_stocks', methods=['GET'])
def fetch_short_term_stock_watchlists():
    watchlists = get_all_short_term_stock_watchlists()
    return jsonify(watchlists)

@watchlist_bp.route('/long_term_stocks/', methods=['POST'])
def add_long_term_stocks_watchlist():
    ticker = request.form['ticker']
    add_long_term_stock_watchlist(ticker)
    return jsonify({'message': 'Long term stock watchlist updated successfully!'})

@watchlist_bp.route('/short_term_stocks/', methods=['POST'])
def add_short_term_stocks_watchlist():
    ticker = request.form['ticker']
    add_short_term_stock_watchlist(ticker)
    return jsonify({'message': 'Short term stock watchlist updated successfully!'})

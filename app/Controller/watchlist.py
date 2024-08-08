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
    """
    Get all long-term stock watchlists
    ---
    responses:
      200:
        description: A list of long-term stock watchlists
        schema:
          type: array
          items:
            type: object
            properties:
              watchlist_id:
                type: integer
              watchlist_name:
                type: string
              user_id:
                type: integer
              ticker:
                type: string
    """
    watchlists = get_all_long_term_stock_watchlists()
    return jsonify(watchlists)

@watchlist_bp.route('/short_term_stocks', methods=['GET'])
def fetch_short_term_stock_watchlists():
    """
    Get all short-term stock watchlists
    ---
    responses:
      200:
        description: A list of short-term stock watchlists
        schema:
          type: array
          items:
            type: object
            properties:
              watchlist_id:
                type: integer
              watchlist_name:
                type: string
              user_id:
                type: integer
              ticker:
                type: string
    """
    watchlists = get_all_short_term_stock_watchlists()
    return jsonify(watchlists)

@watchlist_bp.route('/long_term_stocks/', methods=['POST'])
def add_long_term_stocks_watchlist():
    """
    Add to long-term stock watchlist
    ---
    parameters:
      - name: ticker
        in: formData
        type: string
        required: true
        description: The ticker of the stock to add
    responses:
      200:
        description: A message indicating the watchlist was updated successfully
        schema:
          type: object
          properties:
            message:
              type: string
    """
    ticker = request.form['ticker']
    add_long_term_stock_watchlist(ticker)
    return jsonify({'message': 'Long term stock watchlist updated successfully!'})

@watchlist_bp.route('/short_term_stocks/', methods=['POST'])
def add_short_term_stocks_watchlist():
    """
    Add to short-term stock watchlist
    ---
    parameters:
      - name: ticker
        in: formData
        type: string
        required: true
        description: The ticker of the stock to add
    responses:
      200:
        description: A message indicating the watchlist was updated successfully
        schema:
          type: object
          properties:
            message:
              type: string
    """
    ticker = request.form['ticker']
    add_short_term_stock_watchlist(ticker)
    return jsonify({'message': 'Short term stock watchlist updated successfully!'})

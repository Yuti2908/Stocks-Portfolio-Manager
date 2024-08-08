from flask import Blueprint, jsonify, request, Flask

from app.Services.holdings import get_all_holdings, add_holding

holdings_bp = Blueprint('holdings', __name__)

@holdings_bp.route('/', methods=['GET'])
def fetch_holdings():
    holdings = get_all_holdings()
    return jsonify(holdings)

@holdings_bp.route('/', methods=['POST'])
def create_holding():
    ticker = request.form['ticker']
    buyPrice = request.form['buy_price']
    quantity = request.form['quantity']
    add_holding(buyPrice,ticker,quantity)
    return jsonify({'message': 'Holding added successfully!'})

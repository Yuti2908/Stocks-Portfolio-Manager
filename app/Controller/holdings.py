from flask import Blueprint, jsonify, request, Flask

from app.Services.holdings import get_all_holdings, add_holding, sell_user_holdings
from app.Services.transactions import add_transaction

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
    date = request.form['date']
    add_holding(buyPrice,ticker,quantity)
    add_transaction(buyPrice, ticker, "BUY", quantity, date)
    return jsonify({'message': 'Holding added successfully!'})

@holdings_bp.route('/sell_holdings', methods=['POST'])
def sell_holdings():
    ticker = request.form['ticker']
    sellPrice = request.form['sell_price']
    quantity = request.form['quantity']
    date = request.form['date']
    sell_user_holdings(ticker,sellPrice,quantity)
    try:
        add_transaction(sellPrice, ticker, "SELL", quantity, date)
        print("Transaction added successfully!")
    except Exception as e:
        print(e)
    return jsonify({'message': 'Holding updated successfully!'})

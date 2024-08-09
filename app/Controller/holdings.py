from flask import Blueprint, jsonify, request, Flask
from app.Services.holdings import get_all_holdings, add_holding, sell_user_holdings
from app.Services.transactions import add_transaction

holdings_bp = Blueprint('holdings', __name__)

@holdings_bp.route('/', methods=['GET'])
def fetch_holdings():
    """
    Get all holdings
    ---
    responses:
      200:
        description: A list of holdings
        schema:
          type: array
          items:
            type: object
            properties:
              ticker:
                type: string
              buyPrice:
                type: number
              quantity:
                type: integer
              date:
                type: string
    """
    holdings = get_all_holdings()
    return jsonify(holdings)

@holdings_bp.route('/', methods=['POST'])
def create_holding():
    """
    Create a new holding
    ---
    parameters:
      - name: ticker
        in: formData
        type: string
        required: true
        description: The ticker of the holding
      - name: buyPrice
        in: formData
        type: number
        required: true
        description: The buying price of the holding
      - name: quantity
        in: formData
        type: integer
        required: true
        description: The quantity of the holding
      - name: date
        in: formData
        type: string
        required: true
        description: The date of the holding
    responses:
      200:
        description: A message indicating the holding was added successfully
        schema:
          type: object
          properties:
            message:
              type: string
    """
    ticker = request.form['ticker']
    buyPrice = request.form['buy_price']
    quantity = request.form['quantity']
    date = request.form['date']
    add_holding(buyPrice, ticker, quantity)
    add_transaction(buyPrice, ticker, "BUY", quantity, date)
    return jsonify({'message': 'Holding added successfully!'})

@holdings_bp.route('/sell_holdings', methods=['POST'])
def sell_holdings():
    """
    Sell a holding
    ---
    parameters:
      - name: ticker
        in: formData
        type: string
        required: true
        description: The ticker of the holding to sell
      - name: sellPrice
        in: formData
        type: number
        required: true
        description: The selling price of the holding
      - name: quantity
        in: formData
        type: integer
        required: true
        description: The quantity of the holding to sell
      - name: date
        in: formData
        type: string
        required: true
        description: The date of the holding
    responses:
      200:
        description: A message indicating the holding was sold successfully
        schema:
          type: object
          properties:
            message:
              type: string
    """
    ticker = request.form['ticker']
    sellPrice = request.form['sell_price']
    quantity = request.form['quantity']
    date = request.form['date']
    sell_user_holdings(ticker, sellPrice, quantity)
    try:
        add_transaction(sellPrice, ticker, "SELL", quantity, date)
        print("Transaction added successfully!")
    except Exception as e:
        print(e)
    return jsonify({'message': 'Holding updated successfully!'})

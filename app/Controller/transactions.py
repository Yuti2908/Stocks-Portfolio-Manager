from flask import Blueprint, jsonify, request
from app.Services.transactions import get_all_transactions, add_transaction

transactions_bp = Blueprint('transactions', __name__)

@transactions_bp.route('/', methods=['GET'])
def fetch_transactions():
    """
    Get all transactions
    ---
    responses:
      200:
        description: A list of transactions
        schema:
          type: array
          items:
            type: object
            properties:
              trans_id:
                type: integer
              user_id:
                type: integer
              ticker:
                type: string
              trans_type:
                type: string
              quantity:
                type: integer
              price_per_charge:
                type: number
              tot_amnt:
                type: number
    """
    transactions = get_all_transactions()
    return jsonify(transactions)

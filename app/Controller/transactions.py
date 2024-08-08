from flask import Blueprint, jsonify, request
from app.Services.transactions import get_all_transactions, add_transaction

transactions_bp = Blueprint('transactions', __name__)

@transactions_bp.route('/', methods=['GET'])
def fetch_transactions():
    transactions = get_all_transactions()
    return jsonify(transactions)


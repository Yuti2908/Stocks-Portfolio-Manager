from flask import Blueprint, jsonify, request, Flask
from app.Services.chart_distribution import percentage_distribution_service

chart_distribution_bp = Blueprint('chartDistribution', __name__)

@chart_distribution_bp.route('/', methods=['GET'])
def chart_distribution():
    return jsonify(percentage_distribution_service())
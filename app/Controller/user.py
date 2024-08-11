from flask import Blueprint, jsonify, request
from app.Services.user import user_profits_service

user_bp = Blueprint('userDetails', __name__)

@user_bp.route('/',methods=['GET'])
def user_profits():
    result = user_profits_service();
    return result


if __name__=='__main__':
    user_profits()
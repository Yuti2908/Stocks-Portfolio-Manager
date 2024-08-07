from flask import Flask
from flask_mysqldb import MySQL

# mysql = MySQL()

def create_app():
    app = Flask(__name__)
    # app.config.from_object('config')

    # mysql.init_app(app)

    from app.Controller.transactions import transactions_bp
    from app.Controller.holdings import holdings_bp

    app.register_blueprint(transactions_bp, url_prefix='/transactions')
    app.register_blueprint(holdings_bp, url_prefix='/holdings')

    return app

if __name__=='__main__':
    app=create_app()
    app.run(debug=True)

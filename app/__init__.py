from flask import Flask

def create_app():
    app = Flask(__name__)
    # app.config.from_object('config')

    # mysql.init_app(app)

    from app.Controller.transactions import transactions_bp
    from app.Controller.holdings import holdings_bp
    from app.Controller.watchlist import watchlist_bp

    app.register_blueprint(transactions_bp, url_prefix='/transactions')
    app.register_blueprint(holdings_bp, url_prefix='/holdings')
    app.register_blueprint(watchlist_bp, url_prefix='/watchlist')

    return app

if __name__=='__main__':
    app=create_app()
    app.run(debug=True)

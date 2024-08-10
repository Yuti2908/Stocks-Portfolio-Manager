import json

from flask import Flask, render_template, request, redirect, url_for
from app.Repository.holdings import fetch_all_holdings,check_ticker
from app.Repository.transactions import fetch_all_transactions
from app.Repository.watchlist import fetch_all_short_term_stock_watchlists, fetch_all_long_term_stock_watchlists
from app.Services.holdings import add_holding, sell_user_holdings
from app.Services.transactions import add_transaction
from app.Services.watchlist import add_short_term_stock_watchlist, add_long_term_stock_watchlist, delete_stocks_watchlist_service
from app.Services.user import add_cash_service
import os

def create_app():
    app = Flask(__name__, template_folder="D:\\projects\\Stocks-Portfolio-Manager\\templates", static_folder="D:\\projects\\Stocks-Portfolio-Manager\\templates")
    # app.config.from_object('config')

    # mysql.init_app(app)

    from app.Controller.transactions import transactions_bp
    from app.Controller.holdings import holdings_bp
    from app.Controller.watchlist import watchlist_bp
    from app.Controller.user import user_bp
    from app.Controller.chart_distribution import chart_distribution_bp
    # from app.Controller.start import start_bp

    app.register_blueprint(transactions_bp, url_prefix='/transactions')
    app.register_blueprint(holdings_bp, url_prefix='/holdings')
    app.register_blueprint(watchlist_bp, url_prefix='/watchlist')
    # app.register_blueprint(start_bp, url_prefix='/start')
    app.register_blueprint(user_bp, url_prefix='/userDetails')
    app.register_blueprint(chart_distribution_bp, url_prefix='/chartDistribution')

    @app.route("/start")
    def start():
        result = fetch_all_holdings()
        print(result)
        lst = []
        for i in result[::-1]:
            dic = {}
            dic['ticker'] = i[2]
            dic['buyPrice'] = float(i[4])
            dic['quantity'] = i[3]
            dic['currentPrice'] = float(i[5])
            dic['profit'] = round((dic['currentPrice']-dic['buyPrice'])*dic['quantity'],2)
            lst.append(dic)
        print(lst)
        transres=fetch_all_transactions()
        print(transres)
        translst=[]
        for i in transres[::-1]:
            dic={}
            dic['ticker'] = i[2]
            dic['quantity'] = i[4]
            dic['type']=i[3]
            dic['price']=float(i[6])
            dic['date']=i[7]
            translst.append(dic)
        shortres=fetch_all_short_term_stock_watchlists()
        print(shortres)
        shortlst=[]
        for i in shortres[::-1]:
            dic={}
            dic['ticker'] = i[2]
            if i[3]==None:
                dic['price'] = 'NA'
            else:
                dic['price'] = float(i[3])
            shortlst.append(dic)
        longres = fetch_all_long_term_stock_watchlists()
        print(longres)
        longlst = []
        for i in longres[::-1]:
            dic = {}
            dic['ticker'] = i[2]
            if i[3] == None:
                dic['price'] = 'NA'
            else:
                dic['price'] = float(i[3])
            longlst.append(dic)

        return render_template("index.html",holdings=lst,transactions=translst,watchlistshort=shortlst,watchlistlong=longlst)

    @app.route("/sellerror")
    def sellerror():
        return render_template("sellerror.html")

    @app.route("/addsuccess")
    def addsuccess():
        return render_template("addsuccess.html")

    @app.route("/sellsuccess")
    def sellsuccess():
        return render_template("sellsuccess.html")

    @app.route("/delsuccess")
    def delsuccess():
        return render_template("delsuccess.html")

    @app.route("/changepwd")
    def changepwd():
        return render_template("forget-pass.html")

    @app.route("/register")
    def register():
        return render_template("register.html")
    @app.route("/addholding",methods=['POST'])
    def addholding():
        ticker = request.form['ticker']
        buyPrice = request.form['buy_price']
        quantity = request.form['quantity']
        date = request.form['date']
        add_holding(buyPrice, ticker, quantity)
        add_transaction(buyPrice, ticker, "BUY", quantity, date)
        return redirect(url_for('addsuccess'))

    @app.route("/addwatchshort", methods=['POST'])
    def addwatchshort():
        ticker = request.form['ticker']
        add_short_term_stock_watchlist(ticker)
        return redirect(url_for('addsuccess'))

    @app.route("/addwatchlong", methods=['POST'])
    def addwatchlong():
        ticker = request.form['ticker']
        add_long_term_stock_watchlist(ticker)
        return redirect(url_for('addsuccess'))

    @app.route("/sellholding", methods=['POST'])
    def sellholding():
        ticker = request.form['ticker']
        sellPrice = request.form['sell_price']
        quantity = int(request.form['quantity'])
        date = request.form['date']
        res=check_ticker(ticker)
        print(res)
        print(type(quantity))
        print(type(res['quantity']))
        if quantity>res['quantity']:
            return redirect(url_for('sellerror'))
        sell_user_holdings(ticker, sellPrice, quantity)
        try:
            add_transaction(sellPrice, ticker, "SELL", quantity, date)
            print("Transaction added successfully!")
        except Exception as e:
            print(e)
        return redirect(url_for('sellsuccess'))

    @app.route("/delwatchshort", methods=['POST'])
    def delwatchshort():
        ticker = request.form['ticker']
        watchlist_name = 'short'
        delete_stocks_watchlist_service(ticker, watchlist_name);
        return redirect(url_for('delsuccess'))

    @app.route("/addcash", methods=['POST'])
    def addcash():
        added_cash = request.form['added_cash']
        add_cash_service(added_cash)
        return redirect(url_for('delsuccess'))

    @app.route("/delwatchlong", methods=['POST'])
    def delwatchlong():
        ticker = request.form['ticker']
        watchlist_name = 'long'
        delete_stocks_watchlist_service(ticker, watchlist_name);
        return redirect(url_for('delsuccess'))

    return app



if __name__=='__main__':
    app=create_app()
    app.run(debug=True)
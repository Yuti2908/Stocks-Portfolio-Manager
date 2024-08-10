import decimal

import mysql
from flask import jsonify

from app.Repository.database_access import get_db_connection
from app.Repository.yahoo_api import get_yahoo_data

def updateRealisedProfit(profit):
    conn = get_db_connection()
    cur = conn.cursor()
    query = "SELECT DISTINCT realised_profit FROM user_table LIMIT 1;"
    try:
        cur.execute(query)
        result = cur.fetchone()

        if result:
            realised_profit = int(result[0])+profit
            update_query = "UPDATE user_table SET realised_profit = %s"
            print(realised_profit)
            cur.execute(update_query, (realised_profit,))
            print("Realised Profit:", realised_profit)

        else:
            print("No data found.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.commit()
        cur.close()
        conn.close()

def updateUnrealisedProfit():
    unrealisedProfit = calculateUnrealisedProfit()
    print(unrealisedProfit)
    query = "UPDATE user_table SET unrealised_profit = %s"
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(query, (unrealisedProfit,))
    conn.commit()
    cur.close()
    conn.close()


def fetch_all_holdings():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM holdings")
    holdings = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    ticker_index = columns.index('ticker')
    ticker_values = [row[ticker_index] for row in holdings]
    print(ticker_values)
    for ticker in ticker_values:
        closing_price = get_yahoo_data(ticker)
        print(closing_price,ticker)
        update_query = "UPDATE holdings SET current_value = %s WHERE ticker = %s"
        cur.execute(update_query, (closing_price, ticker))
    conn.commit()
    cur.execute("SELECT * FROM holdings")
    holdings = cur.fetchall()
    cur.close()
    conn.close()
    updateUnrealisedProfit()
    return holdings

def calculateUnrealisedProfit():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM holdings")
    holdings = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    quantity_index = columns.index('quantity')
    buyPrice_index = columns.index('avg_purchasing_price')
    currentPrice_index = columns.index('current_value')
    unrealisedProfit = 0
    for holding in holdings:
        unrealisedProfit+=holding[quantity_index]*(-holding[buyPrice_index]+holding[currentPrice_index])
    cur.close()
    conn.close()
    return unrealisedProfit

def check_ticker(ticker):
    conn = get_db_connection()
    cur = conn.cursor()
    query = "SELECT quantity, avg_purchasing_price,current_value FROM holdings WHERE ticker = %s LIMIT 1;"
    cur.execute(query, (ticker,))
    result = cur.fetchone()

    if result:
        quantity, avg_purchasing_price,current_value = result
        return {"quantity": quantity, "avg_purchasing_price": avg_purchasing_price,"current_value":current_value}
    else:
        return {"quantity": -1, "avg_purchasing_price": -1,"current_value": -1}

def insert_holding(buyPrice,ticker,quantity):
    conn = get_db_connection()
    cur = conn.cursor()
    ticker = ticker.upper()
    print(ticker,quantity,buyPrice)
    buyPrice = decimal.Decimal(buyPrice)
    quantity = int(quantity)
    check_ticker_exists = check_ticker(ticker)
    if check_ticker_exists["quantity"]==-1:
        cur.execute("INSERT INTO holdings (user_id, ticker, quantity, avg_purchasing_price, current_value) VALUES (%s, %s, %s, %s, %s);",
                (1, ticker, quantity, buyPrice, buyPrice))
    else:
        print(check_ticker_exists["quantity"])
        updated_quantity=(quantity+check_ticker_exists["quantity"])
        avg_purchasing_pric = (buyPrice*quantity+check_ticker_exists["quantity"]*check_ticker_exists["avg_purchasing_price"])/updated_quantity
        query = "UPDATE holdings SET avg_purchasing_price = %s, quantity = %s WHERE ticker = %s;"
        cur.execute(query, (avg_purchasing_pric, updated_quantity,ticker))
    conn.commit()
    cur.close()
    conn.close()


def update_holding(ticker,sellPrice,quantity):
    conn = get_db_connection()
    cur = conn.cursor()
    quantity = int(quantity)
    ticker = ticker.upper()
    check_ticker_exists = check_ticker(ticker)
    print(check_ticker_exists["quantity"])
    updated_quantity = (-quantity + check_ticker_exists["quantity"])
    profit = -check_ticker_exists["avg_purchasing_price"]*quantity+check_ticker_exists["current_value"]*quantity

    try:
        if updated_quantity != 0:
            query = "UPDATE holdings SET quantity = %s WHERE ticker = %s;"
            cur.execute(query, (updated_quantity, ticker))
        else:
            query = "DELETE FROM holdings WHERE ticker = %s;"
            cur.execute(query, (ticker,))
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        conn.commit()
        cur.close()
        conn.close()
        updateRealisedProfit(profit)



import decimal

import mysql
from flask import jsonify

from app.Repository.database_access import get_db_connection

def fetch_all_holdings():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM holdings WHERE user_id='1'")
    holdings = cur.fetchall()
    cur.close()
    conn.close()
    return holdings


def check_ticker(ticker):
    conn = get_db_connection()
    cur = conn.cursor()
    query = "SELECT quantity, avg_purchasing_price FROM holdings WHERE ticker = %s LIMIT 1;"
    cur.execute(query, (ticker,))
    result = cur.fetchone()

    if result:
        quantity, avg_purchasing_price = result
        return {"quantity": quantity, "avg_purchasing_price": avg_purchasing_price}
    else:
        return {"quantity": -1, "avg_purchasing_price": -1}

def insert_holding(buyPrice,ticker,quantity):
    conn = get_db_connection()
    cur = conn.cursor()
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
    check_ticker_exists = check_ticker(ticker)
    print(check_ticker_exists["quantity"])
    updated_quantity = (-quantity + check_ticker_exists["quantity"])
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


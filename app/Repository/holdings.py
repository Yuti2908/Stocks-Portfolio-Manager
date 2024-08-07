from app.Repository.database_access import get_db_connection

def fetch_all_holdings():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM holdings WHERE user_id=1")
    holdings = cur.fetchall()
    cur.close()
    conn.close()
    return holdings

def insert_holding(data):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO holdings (user_id, ticker, quantity, avg_purchasing_price, current_value) VALUES (%s, %s, %s, %s, %s)",
                (data['user_id'], data['ticker'], data['quantity'], data['avg_purchasing_price'], data['current_value']))

    cur.close()
    conn.close()
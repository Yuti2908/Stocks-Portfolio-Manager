
from app.Repository.database_access import get_db_connection
def fetch_all_transactions():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM transactions")
    transactions = cur.fetchall()
    cur.close()
    return transactions

def insert_transaction(buyPrice, ticker):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO transactions (user_id, ticker, trans_type, quantity, price_per_charge, tot_amnt) VALUES (%s, %s, %s, %s, %s, %s)",
                (data['user_id'], data['ticker'], data['trans_type'], data['quantity'], data['price_per_charge'], data['tot_amnt']))
    conn.close()
    cur.close()


from app.Repository.database_access import get_db_connection
def fetch_all_transactions():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM transactions")
    transactions = cur.fetchall()
    cur.close()
    return transactions

def insert_transaction(price, ticker, trans_type, quantity, date):
    conn = get_db_connection()
    cur = conn.cursor()
    quantity=int(quantity)
    price=int(price)
    print("Inserting into transaction table")
    cur.execute("INSERT INTO transactions (user_id, ticker, trans_type, quantity, price_per_charge, tot_amnt, date) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (1, ticker, trans_type, quantity, price, quantity*price, date))
    conn.commit()
    conn.close()
    cur.close()

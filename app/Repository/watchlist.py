from app.Repository.database_access import get_db_connection

def fetch_all_short_term_stock_watchlists():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM watchlist (watchlist_name) VALUES (%s)",("short"))
    watchlists = cur.fetchall()
    cur.close()
    conn.close()
    return watchlists

def fetch_all_long_term_stock_watchlists():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM watchlist (watchlist_name) VALUES (%s)",("long"))
    watchlists = cur.fetchall()
    cur.close()
    conn.close()
    return watchlists

def insert_long_term_stock_watchlist(data):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO watchlist (watchlist_name, user_id, ticker) VALUES (%s, %s, %s)",
        ("long", data['user_id'], data['ticker'])
    )
    cur.close()
    conn.close()
def insert_short_term_stock_watchlist(data):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO watchlist (watchlist_name, user_id, ticker) VALUES (%s, %s, %s)",
        ("short", data['user_id'], data['ticker'])
    )
    cur.close()
    conn.close()

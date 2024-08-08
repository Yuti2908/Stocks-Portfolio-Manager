from app.Repository.database_access import get_db_connection

def fetch_all_short_term_stock_watchlists():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM watchlist WHERE watchlist_name = %s", ("short",))
    watchlists = cur.fetchall()
    cur.close()
    conn.close()
    return watchlists

def fetch_all_long_term_stock_watchlists():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM watchlist WHERE watchlist_name = %s", ("long",))
    watchlists = cur.fetchall()
    cur.close()
    conn.close()
    return watchlists

def insert_long_term_stock_watchlist(ticker):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO watchlist (watchlist_name, ticker) VALUES (%s, %s)",
        ("long", ticker)
    )
    conn.commit()
    cur.close()
    conn.close()
def insert_short_term_stock_watchlist(ticker):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO watchlist (watchlist_name, ticker) VALUES (%s, %s)",
        ("short", ticker)
    )
    conn.commit()
    cur.close()
    conn.close()

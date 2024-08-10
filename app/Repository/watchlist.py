from app.Repository.database_access import get_db_connection
from app.Repository.yahoo_api import get_yahoo_data
def fetch_all_short_term_stock_watchlists():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM watchlist WHERE watchlist_name = %s", ("short",))
    watchlists = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    ticker_index = columns.index('ticker')
    ticker_values = [row[ticker_index] for row in watchlists]
    print(ticker_values)
    for ticker in ticker_values:
        closing_price = get_yahoo_data(ticker)
        print(closing_price, ticker)
        update_query = "UPDATE watchlist SET current_price = %s WHERE ticker = %s AND watchlist_name = %s"
        cur.execute(update_query, (closing_price, ticker,"short"))
    conn.commit()
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
    columns = [desc[0] for desc in cur.description]
    ticker_index = columns.index('ticker')
    ticker_values = [row[ticker_index] for row in watchlists]
    print(ticker_values)
    for ticker in ticker_values:
        closing_price = get_yahoo_data(ticker)
        print(closing_price, ticker)
        update_query = "UPDATE watchlist SET current_price = %s WHERE ticker = %s AND watchlist_name = %s"
        cur.execute(update_query, (closing_price, ticker, "long"))
    conn.commit()
    cur.execute("SELECT * FROM watchlist WHERE watchlist_name = %s", ("long",))
    watchlists = cur.fetchall()
    cur.close()
    conn.close()
    return watchlists

def insert_long_term_stock_watchlist(ticker):
    conn = get_db_connection()
    cur = conn.cursor()
    ticker = ticker.upper()
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
    ticker = ticker.upper()
    cur.execute(
        "INSERT INTO watchlist (watchlist_name, ticker) VALUES (%s, %s)",
        ("short", ticker)
    )
    conn.commit()
    cur.close()
    conn.close()


def delete_stocks_watchlist_repository(ticker,watchlist_name):
    conn = get_db_connection()
    cur = conn.cursor()
    ticker = ticker.upper()
    try:
        cur.execute(
            "DELETE FROM watchlist WHERE watchlist_name = %s AND ticker = %s;",
            (watchlist_name ,ticker)
        )
        conn.commit()
    except Exception as e:
        print(e)
    cur.close()
    conn.close()
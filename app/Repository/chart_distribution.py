from app.Repository.database_access import get_db_connection

def percentage_distribution():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM holdings")
    holdings = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    quantity_index = columns.index('quantity')
    buyPrice_index = columns.index('avg_purchasing_price')
    ticker_index = columns.index('ticker')
    percent_div = {}
    total_amnt = 0
    for holding in holdings:
        percent_div[holding[ticker_index]] = round(int(holding[quantity_index]) * (float(holding[buyPrice_index])),2)
        total_amnt += (int(holding[quantity_index]) * (float(holding[buyPrice_index])))

    for key in percent_div.keys():
        percent_div[key] = round((percent_div[key]*100)/total_amnt,2)
    cur.close()
    conn.close()
    total_amnt=round(total_amnt,2)
    print(percent_div, total_amnt)
    return percent_div

if __name__ == '__main__':
    percentage_distribution()
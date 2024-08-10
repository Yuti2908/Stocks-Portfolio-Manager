
from app.Repository.database_access import get_db_connection

def user_profits_repository():
    conn = get_db_connection()
    cur = conn.cursor()
    query = "SELECT DISTINCT realised_profit,unrealised_profit FROM user_table LIMIT 1;"
    try:
        cur.execute(query)
        result = cur.fetchone()
        print(result)
        if result:
            realised_profit = int(result[0])
            unrealised_profit = int(result[1])
            print(realised_profit,unrealised_profit)
            return {"realised_profit": realised_profit,"unrealised_profit": unrealised_profit}
        else: return {"realised_profit": 0, "unrealised_profit": 0}
    except Exception as e:
        return {"realised_profit": 0, "unrealised_profit": 0}
    finally:
        conn.close()
        cur.close()

if __name__=='__main__':
    user_profits_repository()
import psycopg2

"""Скрипт для заполнения данными таблиц в БД Postgres."""
if __name__ == '__main__':
    conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='1003')
    cur = conn.cursor()
    try:

        sql = "COPY %s FROM STDIN WITH CSV HEADER DELIMITER AS ','"
        e = open('north_data/employees_data.csv', 'r', encoding='utf8')
        cur.execute("truncate " + 'employees' + ";")
        cur.copy_expert(sql=sql % 'employees', file=e)

        sql = "COPY %s FROM STDIN WITH CSV HEADER DELIMITER AS ','"
        e = open('north_data/customers_data.csv', 'r', encoding='utf8')
        cur.execute("truncate " + 'customers' + ";")
        cur.copy_expert(sql=sql % 'customers', file=e)

        with open('north_data/orders_data.csv', 'r', encoding='utf-8') as f:
            cur.execute("truncate " + 'orders' + ";")
            cur.copy_expert("COPY orders FROM STDIN WITH CSV HEADER DELIMITER AS ','", f)

    finally:
        conn.commit()
        cur.close()
        conn.close()

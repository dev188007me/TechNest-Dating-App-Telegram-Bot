import psycopg2

db_url = "postgres://postgres:667371@localhost:5432/technest_telegram_dating_bot_db"

conn = psycopg2.connect(db_url)
cur = conn.cursor()
cur.execute("CREATE TABLE test_table (id SERIAL PRIMARY KEY);")
cur.execute("DROP TABLE test_table;")
conn.commit()
cur.close()
conn.close()
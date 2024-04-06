import psycopg2

try:
    db_connection = psycopg2.connect(dbname='postgres',
                                 user='postgres',
                                 password='root',
                                 host='localhost',
                                 port=5432)
    print("ddd")
except Exception as e:
    print(str(e))

print("Successfully connected to the database.")
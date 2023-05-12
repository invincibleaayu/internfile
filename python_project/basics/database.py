import psycopg2

db_connection = psycopg2.connect(dbname='postgres',
                                 user='postgres',
                                 password='aayu',
                                 host='localhost',
                                 port=5432)

print("Successfully connected to the database.")
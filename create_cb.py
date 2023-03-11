from psycopg2 import connect, ProgrammingError
import sql_engine


def create_db(cursor):
    create_database = """ CREATE DATABASE to_do_list_db"""
    cursor.execute(create_database)


def execute_sql():
    cnx = connect(user='postgres', host='localhost', password='ambrozja')
    cnx.autocommit = True
    cursor = cnx.cursor()
    try:
        create_db(cursor)
        print("Udało się utworzyć bazę danych! Brawo")
    except ProgrammingError:
        print("Coś poszło nie tak")
    cnx.close()
    cursor.close()

execute_sql()




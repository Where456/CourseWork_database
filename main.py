import os
from database.db_manager import DBManager
from dotenv import load_dotenv

load_dotenv()

dbname = os.getenv('dbname')
user = os.getenv('user')
password = os.getenv('password')
host = os.getenv('host')
port = os.getenv('port')


def main():
    key_w = input('Ведите ключевое слово: ')
    db_manager = DBManager(dbname=dbname, user=user, password=password, host=host, port=port)

    db_manager.create_tables()

    print("Companies and Vacancies Count:", db_manager.get_companies_and_vacancies_count())
    print("All Vacancies:", db_manager.get_all_vacancies())
    print("Average Salary:", db_manager.get_avg_salary())
    print("Vacancies with Higher Salary:", db_manager.get_vacancies_with_higher_salary())
    print("Vacancies with Keyword:", db_manager.get_vacancies_with_keyword(key_w))

    db_manager.close_connection()


if __name__ == "__main__":
    main()

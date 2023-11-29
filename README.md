# Database Project README

## О проекте

Этот проект представляет собой базу данных для хранения информации о вакансиях различных компаний, полученных с использованием API hh.ru.

## Используемые технологии

- Python
- PostgreSQL
- psycopg2 (для работы с PostgreSQL)
- requests (для работы с API hh.ru)

## Установка

1. Убедитесь, что у вас установлен Python.
2. Установите необходимые библиотеки, выполнив `pip install -r requirements.txt`.
3. Создайте базу данных PostgreSQL и таблицы, используя SQL-скрипты в папке `database_scripts`.
4. Запустите скрипт `main.py` для получения данных с hh.ru и загрузки их в базу данных.

## Структура проекта

- `main.py`: Основной скрипт для выполнения проекта.
- `database_scripts`: SQL-скрипты для создания базы данных и таблиц.
- `database`: Классы и методы для работы с базой данных.

## Использование DBManager

Пример использования класса DBManager для выполнения запросов к базе данных:

```python
from database.db_manager import DBManager

# Создаем экземпляр DBManager
db_manager = DBManager()

# Пример использования метода для получения вакансий с зарплатой выше средней
higher_salary_vacancies = db_manager.get_vacancies_with_higher_salary()
print("Vacancies with Higher Salary:", higher_salary_vacancies)

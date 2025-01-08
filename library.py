"""
Задача на тему SQLite3:

Создайте базу данных university.db.
Создайте таблицу students со следующими полями:
id (INTEGER, PRIMARY KEY),
name (TEXT, NOT NULL),
age (INTEGER),
major (TEXT),
gpa (REAL).
Добавьте данные для следующих студентов:
Алиса, 20 лет, специальность "Computer Science", средний балл 4.2.
Боб, 22 года, специальность "Mathematics", средний балл 3.8.
Чарли, 19 лет, специальность "Physics", средний балл 4.5.
Диана, 21 год, специальность "Economics", средний балл 4.0.
Выполните следующие действия:
Найдите студентов с GPA выше 4.0.
Обновите специальность студента с именем "Диана" на "Business".
Удалите из базы данных всех студентов младше 20 лет.
Посчитайте средний GPA всех оставшихся студентов.
Выведите список студентов, отсортированный по их имени в алфавитном порядке.
Напишите Python-скрипт с использованием модуля sqlite3 для выполнения этой задачи.
"""
import sqlite3 

connect = sqlite3.connect("library.db")
cursor = connect.cursor()

cursor.execute("""
        CREATE TABLE IF NOT EXISTS books(
               id INTEGER PRIMARY KEY AUTOINCREMENT, 
               name TEXT NO NULL,
               age INT, 
               major TEXT,
               gpa TEXT,  
               )
""")

def registor():
    name = input("")



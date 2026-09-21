"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2


conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="maria",
    password="",
    port=5432,
)
cur = conn.cursor()

# 1. Заполняем таблицу сотрудников (employees)
with open('homework-1/north_data/employees_data.csv', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # пропускаем строку с заголовками
    for row in reader:
        cur.execute(
            "INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)",
            row
        )

# 2. Заполняем таблицу клиентов (customers)
with open('homework-1/north_data/customers_data.csv', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # пропускаем строку с заголовками
    for row in reader:
        cur.execute(
            "INSERT INTO customers VALUES (%s, %s, %s)",
            row
        )

# 3. Заполняем таблицу заказов (orders)
with open('homework-1/north_data/orders_data.csv', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # пропускаем строку с заголовками
    for row in reader:
        cur.execute(
            "INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",
            row
        )

# Сохраняем изменения и закрываем соединение
conn.commit()
cur.close()
conn.close()

print("Данные успешно добавлены!")
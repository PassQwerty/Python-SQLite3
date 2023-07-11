# pip install pysqlite3
import sqlite3

# SQL (сокращение от англ. Structured Query Language)
#     — это язык запросов, который применяют, чтобы работать с базами данных


def main():
    db = sqlite3.connect('database.db')
    sql = db.cursor()

    # Всего существует несколько типов запросов:
    # Существуют несколько типов переменных:
    # NULL - пустое поле
    # TEXT - текст
    # INTEGER - число
    # INT - число, сокращение INTEGER
    # REAL - число с плавающей точкой
    # BLOB - файлоподобный объект, который может читать и записывать данные

    # - CREATE: Этот запрос используется для создания новой таблицы в базе данных SQLite3
    sql.execute("""CREATE TABLE IF NOT EXISTS products (
                        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        product TEXT,
                        supplier TEXT,
                        price INTEGER
                    )""")

    product = 'Бананы'
    supplier = 'Новые Бананы'
    price = 1200

    # - INSERT: Этот запрос используется для добавления новых строк в таблицу.
    # Вариант 1:
    sql.execute(
        "INSERT INTO products (product, supplier, price) VALUES ('Помидоры', 'ООО Томатос', 20)")

    # Вариант 2:
    sql.execute(
        "INSERT INTO products (product, supplier, price) VALUES (?,?,?)", ('Помело', 'ИП Энигов', 20))

    # Вариант 3:
    sql.execute(
        f"INSERT INTO products (product, supplier, price) VALUES ('{product}', '{supplier}', {price})")
    # подтверждение изменений
    db.commit()

    # SELECT: Этот запрос используется для выборки данных из таблицы.
    # (Поиск продукта с именем Помело и вывод его цены)
    sql.execute("SELECT price FROM products WHERE product='Помело'")
    # Печать найденного результата
    # print(sql.fetchone())

    # Вывод всех данных из продуктов через цикл
    cursor = sql.execute("SELECT product, supplier, price FROM products")
    for row in cursor:
        print(f"NAME      = {row[0]}\
              \nSUPPLIER  = {row[1]}\
              \nPRICE     = {row[2]}\n")

    # Нахождение элемента с проверкой и вывод первого найденного элемента
    cursor = sql.execute(
        "SELECT product FROM products WHERE product=?", ('Помидоры',))
    row = cursor.fetchone()
    if row:
        print("Product = ", row[0])
    else:
        print("Продукта не существует!!")

    # Нахождение всех элементов с проверкой
    cursor = sql.execute(
        "SELECT product FROM products WHERE product LIKE ?", ('%Помидоры%',))
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print("Product = ", row[0])
    else:
        print("Продуктов не существует!!")

    productsToInsert = [
        ('Авакадо', 'ООО Авакандо', 1200),
        ('Апельсины', 'ООО Альпасино', 800),
        ('Ананасы', 'ИП Кирченко', 300),
        ('Киви', 'ООО ВкуСвилл', 1000)
    ]

    # Запрос на добавления нескольких продуктов
    sql.executemany("""
                    INSERT INTO products(product, supplier, price)
                    VALUES (?,?,?)
                    """, productsToInsert)
    # подтверждение изменений
    db.commit()

    # SELECT: Этот запрос используется для выборки данных из таблицы. (Выбор необходимых данных из таблицы)
    sql.execute("SELECT * FROM products")
    # Печать всех найденных данных
    print(sql.fetchall())

    # Выбрать все продукты
    sql.execute("SELECT product FROM products")
    # Напечатать все продукты
    print(sql.fetchall())

    # Получить все продукты с ценной 1000
    sql.execute(f"SELECT * FROM products WHERE price={1000}")
    # Напечатать все найденные продукты
    print(sql.fetchall())

    # UPDATE: Этот запрос используется для обновления существующих строк в таблице
    sql.execute(
        f"UPDATE products SET supplier = 'ООО Кивикус' WHERE price = {800}")

    # Функция Update не возвращает результат поэтому необходимо делать Select
    sql.execute("SELECT supplier FROM products")
    # подтверждение изменений
    # db.commit()
    print(sql.fetchall())

    # DELETE: Этот запрос используется для удаления строк из таблицы
    sql.execute(f"DELETE FROM products WHERE product_id={2}")
    # подтверждение изменений
    db.commit()

    # Закрытие соединения sql
    # sql.close()


if __name__ == "__main__":
    main()

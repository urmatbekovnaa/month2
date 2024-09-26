# import sqlite3
# db_name = '''group_46.db'''
#
# CREATE TABLE categories(
#     code VARCHAR(2)  PRIMARY KEY,
#     title VARCHAR(200) NOT NULL
# );
# INSERT INTO categories(code, title)
# VALUES
# ('FD', 'Food products'),
# ('EL', 'Electronics'),
# ('CL', 'Clothes');
#
#
# CREATE TABLE products(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     title VARCHAR(200) NOT NULL,
#     category_code INT,
#     unit_price fLOAT NOT NULL,
#     stock_quantity INTEGER,
#     store_id INT,
#      FOREIGN KEY (category_code) REFERENCES categories(code),
#     FOREIGN KEY (store_id) REFERENCES store(id)
#);

# CREATE TABLE store (
#     store_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     title VARCHAR(100) NOT NULL
#);
#
# INSERT INTO store (title)
# VALUES
# ('Asia'),
# ('Globus'),
# ('Frunse');
#
import sqlite3

conn = sqlite3.connect('group_46.db')
cursor = conn.cursor()

def get_store():
    cursor.execute("SELECT id, title FROM store")
    stores = cursor.fetchall()

    print("Вы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, для выхода из программы введите цифру 0:")
    for store in stores:
        print(f"{store[0]}. {store[1]}")


    return stores

def get_products(store_id):
    query = """
        SELECT p.title, c.title, p.unit_price, p.stock_quantity
        FROM products p
        JOIN categories c ON p.category_code = c.code
        WHERE p.store_id = ?
    """
    cursor.execute(query, (store_id,))
    products = cursor.fetchall()

    if products:
        for product in products:
            print(
                f"Название продукта: {product[0]}; Категория: {product[1]}; Цена: {product[2]}; Количество на складе: {product[3]}")
    else:
            print("Нет продуктов в этом магазине.")



while True:
    stores = get_store()

    try:
        store_id = int(input("\nВведите id магазина: "))
    except ValueError:
        print("Неверный ввод. Пожалуйста, введите число.")
        continue


    if store_id == 0:
        print("Вы вышли из программы.")

    if any(store[0] == store_id for store in stores):
        get_products(store_id)
    else:
        print("Неверный id магазина. Пожалуйста, введите корректный id.")

conn.close()


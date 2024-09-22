import sqlite3
db_name = '''hw.db'''

def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return connection

def create_table(sql):
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

sql_to_create_products_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price REAL NOT NULL DEFAULT 0.0,
    quantity INTEGER  NOT NULL DEFAULT 0
);
'''


my_connection = create_connection(db_name)
if my_connection is not None:
    print('Successfully connected to database!')
    create_table(sql_to_create_products_table)
    my_connection.close()

def delete_products(id):
    try:
        sql = ''' DELETE FROM products WHERE id = ?
        '''
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (id,))
    except sqlite3.Error as e:
        print(e)
def select_all_products():
    try:
        sql = ''' SELECT * FROM products
        '''
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)
def update_products(products):
    try:
        sql = ''' UPDATE products SET quantity = ?, price = ? WHERE id = ?
        '''
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, products)
    except sqlite3.Error as e:
        print(e)
def select_products_by_price(price):
    try:
        sql = ''' SELECT * FROM products WHERE price < ?
        '''
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (price,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)
def select_products_by_quantity(quantity):
    try:
        sql = ''' SELECT * FROM products WHERE quantity > ?
        '''
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (quantity,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)

def insert_products(products):
    try:
        sql = '''INSERT INTO products
        (product_title, price, quantity)
        VALUES (?, ?, ?)
        '''
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, products)
    except sqlite3.Error as e:
        print(e)
# create_table(sql_to_create_products_table)
# insert_products(('soup', 130, 10))
# insert_products(('milk', 20, 13))
# insert_products(('shampoo ELSEVE', 450.0, 25))
# insert_products(('baby shampoo', 350, 1))
# insert_products(('juice 7UP', 40, 70))
# insert_products(('candy', 90, 12))
# insert_products(('tea', 220, 60))
# insert_products(('toothpaste', 180, 30))
# insert_products(('orange juice', 70, 5))
# insert_products(('apple juice', 140, 20))
# insert_products(('toys', 1000, 3))
# insert_products(('cream', 250.5, 10))
# insert_products(('chocolate milk', 85.9, 10))
# insert_products(('ice cream', 40.2, 10))
# insert_products(('Teddy bear toys', 800, 9))


update_products((50, 39, 5))
delete_products(1)
select_all_products()
select_products_by_price(100)
select_products_by_quantity(5)

import sqlite3
conection = sqlite3.connect('gtarp.db')
cursor = conection.cursor()
# Criação das tabelas
cursor.execute(''' DROP TABLE IF EXISTS username ''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS username(
    id INTEGER PRIMARY KEY,
    name TEXT
)''')
cursor.execute(''' DROP TABLE IF EXISTS items ''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS items(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT NOT NULL
)''')
cursor.execute(''' DROP TABLE IF EXISTS stock_player ''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS stock_player(
    id INTEGER PRIMARY KEY,
    username_id INTEGER NOT NULL,
    items_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,    
    FOREIGN KEY (username_id) REFERENCES username(id),
    FOREIGN KEY (items_id) REFERENCES items(id)
)''')
cursor.execute(''' DROP TABLE IF EXISTS recipe ''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS recipe(
    id INTEGER PRIMARY KEY,
    final_product_id INTEGER NOT NULL,
    material_id INTEGER NOT NULL,
    necessary_quantity INTEGER NOT NULL,
    FOREIGN KEY (final_product_id) REFERENCES items(id),
    FOREIGN KEY (material_id) REFERENCES items(id)
)''')
conection.commit()

#Inserção usernames
cursor.execute('''
   INSERT INTO username (name) VALUES ('Tiago')
''')
cursor.execute('''
   INSERT INTO username (name) VALUES ('Pedro')
''')
cursor.execute('''
   INSERT INTO username (name) VALUES ('Alexa')
''')
cursor.execute('''
   INSERT INTO username (name) VALUES ('André')
''')
#Inserção items
cursor.execute('''
   INSERT INTO items (name, type) VALUES ('UZI', 'Produto final')
''')
cursor.execute('''
   INSERT INTO items (name, type) VALUES ('Tec-9', 'Produto final')
''')
cursor.execute('''
   INSERT INTO items (name, type) VALUES ('Tec Pistol', 'Produto final')
''')
cursor.execute('''
   INSERT INTO items (name, type) VALUES ('Ap Pistol', 'Produto final')
''')
cursor.execute('''
   INSERT INTO items (name, type) VALUES ('Heavy Pistol', 'Produto final')
''')
cursor.execute('''
   INSERT INTO items (name, type) VALUES ('Peças', 'Material')
''')
cursor.execute('''
   INSERT INTO items (name, type) VALUES ('Aço', 'Material')
''')
cursor.execute('''
   INSERT INTO items (name, type) VALUES ('Dinheiro', 'Material')
''')
cursor.execute('''
   INSERT INTO items (name, type) VALUES ('Blue Print', 'Material')
''')
cursor.execute('''
   INSERT INTO items (name, type) VALUES ('Orange Print', 'Material')
''')
#Inserir stock nos players
#Tiago
cursor.execute('''
   INSERT INTO stock_player (username_id, items_id, quantity) VALUES (?,?,? )
''', (1,6,35))
cursor.execute('''
   INSERT INTO stock_player (username_id, items_id, quantity) VALUES (?,?,? )
''', (1,7,20))
cursor.execute('''
   INSERT INTO stock_player (username_id, items_id, quantity) VALUES (?,?,? )
''', (1,8,50000))
cursor.execute('''
   INSERT INTO stock_player (username_id, items_id, quantity) VALUES (?,?,? )
''', (1,9,5))
cursor.execute('''
   INSERT INTO stock_player (username_id, items_id, quantity) VALUES (?,?,? )
''', (1,10,7))
#Pedro
cursor.execute('''
   INSERT INTO stock_player (username_id, items_id, quantity) VALUES (?,?,? )
''', (2,6,55))
cursor.execute('''
   INSERT INTO stock_player (username_id, items_id, quantity) VALUES (?,?,? )
''', (2,7,10))
cursor.execute('''
   INSERT INTO stock_player (username_id, items_id, quantity) VALUES (?,?,? )
''', (2,8,50000))
cursor.execute('''
   INSERT INTO stock_player (username_id, items_id, quantity) VALUES (?,?,? )
''', (2,9,5))
cursor.execute('''
   INSERT INTO stock_player (username_id, items_id, quantity) VALUES (?,?,? )
''', (2,10,7))
#Alexa
cursor.execute('''
   INSERT INTO stock_player (username_id, items_id, quantity) VALUES (?,?,? )
''', (3,6,55))
cursor.execute('''
   INSERT INTO stock_player (username_id, items_id, quantity) VALUES (?,?,? )
''', (3,7,15))
cursor.execute('''
   INSERT INTO stock_player (username_id, items_id, quantity) VALUES (?,?,? )
''', (3,8,50000))
cursor.execute('''
   INSERT INTO stock_player (username_id, items_id, quantity) VALUES (?,?,? )
''', (3,9,5))
cursor.execute('''
   INSERT INTO stock_player (username_id, items_id, quantity) VALUES (?,?,? )
''', (3,10,7))
#André
cursor.execute('''
   INSERT INTO stock_player (username_id, items_id, quantity) VALUES (?,?,? )
''', (4,6,20))
cursor.execute('''
   INSERT INTO stock_player (username_id, items_id, quantity) VALUES (?,?,? )
''', (4,7,10))
cursor.execute('''
   INSERT INTO stock_player (username_id, items_id, quantity) VALUES (?,?,? )
''', (4,8,50000))
cursor.execute('''
   INSERT INTO stock_player (username_id, items_id, quantity) VALUES (?,?,? )
''', (4,9,5))
cursor.execute('''
   INSERT INTO stock_player (username_id, items_id, quantity) VALUES (?,?,? )
''', (4,10,7))
#Definir receitas
#Receita Uzi
cursor.execute('''
   INSERT INTO recipe (final_product_id, material_id, necessary_quantity) VALUES (?,?,? )
''', (1,6,30))
cursor.execute('''
   INSERT INTO recipe (final_product_id, material_id, necessary_quantity) VALUES (?,?,? )
''', (1,7,10))
cursor.execute('''
   INSERT INTO recipe (final_product_id, material_id, necessary_quantity) VALUES (?,?,? )
''', (1,8,30000))
cursor.execute('''
   INSERT INTO recipe (final_product_id, material_id, necessary_quantity) VALUES (?,?,? )
''', (1,10,1))
#Receita Tec-9
cursor.execute('''
   INSERT INTO recipe (final_product_id, material_id, necessary_quantity) VALUES (?,?,? )
''', (2,6,35))
cursor.execute('''
   INSERT INTO recipe (final_product_id, material_id, necessary_quantity) VALUES (?,?,? )
''', (2,7,10))
cursor.execute('''
   INSERT INTO recipe (final_product_id, material_id, necessary_quantity) VALUES (?,?,? )
''', (2,8,30000))
cursor.execute('''
   INSERT INTO recipe (final_product_id, material_id, necessary_quantity) VALUES (?,?,? )
''', (2,10,1))
#Receita Tec pistol
cursor.execute('''
   INSERT INTO recipe (final_product_id, material_id, necessary_quantity) VALUES (?,?,? )
''', (3,6,45))
cursor.execute('''
   INSERT INTO recipe (final_product_id, material_id, necessary_quantity) VALUES (?,?,? )
''', (3,7,10))
cursor.execute('''
   INSERT INTO recipe (final_product_id, material_id, necessary_quantity) VALUES (?,?,? )
''', (3,8,35000))
cursor.execute('''
   INSERT INTO recipe (final_product_id, material_id, necessary_quantity) VALUES (?,?,? )
''', (3,10,1))
#Receita AP Pistol
cursor.execute('''
   INSERT INTO recipe (final_product_id, material_id, necessary_quantity) VALUES (?,?,? )
''', (4,6,45))
cursor.execute('''
   INSERT INTO recipe (final_product_id, material_id, necessary_quantity) VALUES (?,?,? )
''', (4,7,10))
cursor.execute('''
   INSERT INTO recipe (final_product_id, material_id, necessary_quantity) VALUES (?,?,? )
''', (4,8,35000))
cursor.execute('''
   INSERT INTO recipe (final_product_id, material_id, necessary_quantity) VALUES (?,?,? )
''', (4,10,1))
#Receita Heavy Pistol
cursor.execute('''
   INSERT INTO recipe (final_product_id, material_id, necessary_quantity) VALUES (?,?,? )
''', (5,6,50))
cursor.execute('''
   INSERT INTO recipe (final_product_id, material_id, necessary_quantity) VALUES (?,?,? )
''', (5,7,10))
cursor.execute('''
   INSERT INTO recipe (final_product_id, material_id, necessary_quantity) VALUES (?,?,? )
''', (5,8,25000))
cursor.execute('''
   INSERT INTO recipe (final_product_id, material_id, necessary_quantity) VALUES (?,?,? )
''', (5,9,1))
conection.commit()
#Function that checks if the user has the necessary stock to create an item.
def create_item(username_id, final_product_id):
    cursor.execute('''
        SELECT material_id, necessary_quantity
        FROM recipe
        WHERE final_product_id = ?
    ''', (final_product_id,))
    materials = cursor.fetchall()

    for material_id, necessary_quantity in materials:
        cursor.execute('''
            SELECT quantity
            FROM stock_player
            WHERE username_id = ? AND items_id = ?
        ''', (username_id, material_id))
        stock = cursor.fetchone()
        if stock is None or stock[0] < necessary_quantity:
            print(f'Insufficient materials to create item {final_product_id}')
            return

    for material_id, necessary_quantity in materials:
        cursor.execute('''
            UPDATE stock_player
            SET quantity = quantity - ?
            WHERE username_id = ? AND items_id = ?
        ''', (necessary_quantity, username_id, material_id))
    print(f'Item {final_product_id} successfully created!')
    print("Stock updated!")
#Function that checks the user inventory
def stock_consult(username_id):
    cursor.execute('''
        SELECT items.name, stock_player.quantity
        FROM stock_player
        JOIN items ON stock_player.items_id = items.id
        WHERE stock_player.username_id = ?    
    ''',  (username_id,))

    stock = cursor.fetchall()
    for item, quantity in stock:
        print(f'Item {item}, Quantity {quantity}')
#Function that checks the necessary quantity do to a item.
def requirements(final_product_id):
    cursor.execute('''
        SELECT items.name, recipe.necessary_quantity
        FROM recipe
        JOIN items ON recipe.material_id = items.id
        WHERE recipe.final_product_id = ?    
    ''',  (final_product_id,))

    requirements = cursor.fetchall()
    for item, quantity in requirements:
        print(f'Material {item}, Necessary quantity {quantity}')
conection.commit()
create_item(2,1)
stock_consult(2)
cursor.close()

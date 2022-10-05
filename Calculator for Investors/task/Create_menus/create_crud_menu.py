import sqlite3
con = sqlite3.connect(r'../menu.db')
cursor = con.cursor()
# use the execute method to create the first table
try:
    cursor.execute("""CREATE TABLE CRUD_MENU(id INTEGER PRIMARY KEY, name TEXT);""")
except Exception as e:
    print("Error: ", e)
menu_list = [
    (0, 'Back'),
    (1, 'Create a company'),
    (2, 'Read a company'),
    (3, 'Update a company'),
    (4, 'Delete a company'),
    (5, 'List all companies'),
]

cursor.executemany('INSERT INTO CRUD_MENU VALUES (?, ?)', menu_list)

con.commit()
cursor.close()
con.close()

import sqlite3
con = sqlite3.connect(r'../menu.db')
cursor = con.cursor()
# use the execute method to create the first table
try:
    cursor.execute("""CREATE TABLE MAIN_MENU(id INTEGER PRIMARY KEY, name TEXT);""")
except Exception as e:
    print("Error: ", e)
menu_list = [
    (0, 'Exit'),
    (1, 'CRUD operations'),
    (2, 'Show top ten companies by criteria'),
]

cursor.executemany('INSERT INTO MAIN_MENU VALUES (?, ?)', menu_list)

con.commit()
cursor.close()
con.close()

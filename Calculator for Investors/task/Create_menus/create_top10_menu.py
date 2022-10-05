import sqlite3
con = sqlite3.connect(r'../menu.db')
cursor = con.cursor()
# use the execute method to create the first table
try:
    cursor.execute("""CREATE TABLE TOP10_MENU(id INTEGER PRIMARY KEY, name TEXT);""")
except Exception as e:
    print("Error: ", e)
menu_list = [
    (0, 'Back'),
    (1, 'List by ND/EBITDA'),
    (2, 'List by ROE'),
    (3, 'List by ROA')
]

cursor.executemany('INSERT INTO TOP10_MENU VALUES (?, ?)', menu_list)

con.commit()
cursor.close()
con.close()

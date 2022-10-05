import sqlite3
import pandas as pd
con = sqlite3.connect('menu.db')
cursor = con.cursor()

def print_main_menu():
    print('MAIN MENU')
    cursor.execute("SELECT * FROM MAIN_MENU;")
    all_rows = cursor.fetchall()
    for row in all_rows:
        for col in row:
            print(col,end=' ')
        print()
def print_crud_menu():
    print('CRUD MENU')
    cursor.execute("SELECT * FROM CRUD_MENU;")
    all_rows = cursor.fetchall()
    for row in all_rows:
        for col in row:
            print(col,end=' ')
        print()
def print_top10_menu():
    print('TOP TEN MENU')
    cursor.execute("SELECT * FROM TOP10_MENU;")
    all_rows = cursor.fetchall()
    for row in all_rows:
        for col in row:
            print(col,end=' ')
        print()


def after_main():
    print_main_menu()
    option = input("Enter an option:\n")
    if option == '0':
        print('Have a nice day!')

    elif option == '1':
        print_crud_menu()
        option2 = input("Enter an option:\n")
        try:
            if (int(option2) >=0) and (int(option2) <=5):
                print('Not implemented!')
                after_main()
            else:
                print('Invalid option!\n')
                after_main()
        except:
            print('Invalid option!\n')
    elif option == '2':
        print_top10_menu()
        option2 = input("Enter an option:\n")
        try:
            if (int(option2) >=0) and (int(option2) <=3):
                print('Not implemented!\n')
                after_main()
            else:
                print('Invalid option!\n')
                after_main()
        except:
            print('Invalid option!\n')
    else:
        print('Invalid option!\n')
        after_main()

after_main()

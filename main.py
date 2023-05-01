import psycopg2

from user_class import User
from banker_class import Banker
from bank_system_class import BankSystem

from menu.user_menu import user_menu
from menu.banker_menu import banker_menu

from misc import generate_card_number

from db.start_db import postgre_start


def main():
    postgre_start()
    
    bank_system = BankSystem('kursach','postgres','2545','localhost')

    while True:
        print("1. Register User")
        print("2. Login User")
        print("3. Login Banker")
        print("4. Register Banker")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            login = input("Enter login: ")
            password = input("Enter password: ")
            card_number = generate_card_number()
            
            user = bank_system.register_user(login, password, card_number)
            user = bank_system.login_user(user[0], user[1])
            
            user_menu(user)
            
        elif choice == '2':
            login = input("Enter login: ")
            password = input("Enter password: ")
            user = bank_system.login_user(login, password)
            if user:
                user_menu(user)
            else:
                print("Invalid login or password.")
        elif choice == '3':
            login = input("Enter login: ")
            password = input("Enter password: ")
            banker = bank_system.login_banker(login, password)
            
            if banker:
                banker_menu(banker)
            else:
                print("Invalid login or password.")
        elif choice == '4':
            login = input("Enter login: ")
            password = input("Enter password: ")
            
            banker = bank_system.register_banker(login, password)
            banker = bank_system.login_banker(banker[0], banker[1])
            banker_menu(banker)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid input. Try again.")
            
if __name__ == '__main__':
    main()
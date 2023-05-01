import psycopg2

def banker_menu(banker):
    while True:
        print(f"Welcome, Banker {banker.login}!")
        print("1. View User Balance")
        print("2. Set User Balance")
        print("3. Transfer from User to Bank")
        print("4. Transfer from Bank to User")
        print("5. Logout")
        choice = input("Enter choice: ")
        
        if choice == '1':
            user_id = input("Enter User ID: ")
            balance = banker.get_user_balance(user_id)
            if balance is None:
                print("Invalid User ID.")
            else:
                print(f"User ID {user_id} has a balance of {balance}")
        elif choice == '2':
            user_id = input("Enter User ID: ")
            operation = input("Enter 1 if withdraw else 0: ")
            amount = input("Enter changing sum: ")
            if operation == '1':
                banker.set_user_balance(user_id, amount,'withdraw')
            else:
                banker.set_user_balance(user_id, amount,'add')
            print(f"User ID {user_id} now has a balance of {amount}")
        elif choice == '3':
            user_id = input("Enter User ID: ")
            amount = input("Enter amount to transfer: ")
            banker.transfer_from_user(user_id, amount)
            print(f"Transferred {amount} from User ID {user_id} to Bank")
        elif choice == '4':
            user_id = input("Enter User ID: ")
            amount = input("Enter amount to transfer: ")
            banker.transfer_to_user(user_id, amount)
            print(f"Transferred {amount} from Bank to User ID {user_id}")
        elif choice == '5':
            print("Logging out.")
            break
        else:
            print("Invalid input. Try again.")

import psycopg2

def user_menu(user):
    while True:
        print(f"Welcome, User {user.login}!")
        print("1. Transfer Money")
        print("2. View Balance")
        print("3. View Last Transactions")
        print("4. Logout")
        choice = input("Enter choice: ")
        
        if choice == '1':
            recipient_card_number = input("Enter recipient's card number: ")
            amount = input("Enter amount to transfer: ")
            user.transfer_money(recipient_card_number, amount)
            print(f"Transferred {amount} to card number {recipient_card_number}")
        elif choice == '2':
            balance = user.get_balance()
            print(f"Your balance is {balance}")
        elif choice == '3':
            transactions = user.view_last_transactions()
            for transaction in transactions:
                print(transaction)
        elif choice == '4':
            print("Logging out.")
            break
        else:
            print("Invalid input. Try again.")
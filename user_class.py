import psycopg2

class User:
    def __init__(self, id, login, password, card_number, balance):
        self.id = id
        self.login = login
        self.password = password
        self.card_number = card_number
        self.balance = balance
    
    def get_balance(self):
        conn = psycopg2.connect(database="kursach", user="postgres", password="2545", host="localhost")
        cur = conn.cursor()
        cur.execute("SELECT balance FROM users WHERE id = %s", (self.id,))
        balance = cur.fetchone()[0]
        cur.close()
        conn.close()
        return balance
    
    def transfer_money(self, recipient_card_number, amount):
        if self.balance >= amount:
            self.balance -= amount
            recipient = None
            
            conn = psycopg2.connect(database="kursach", user="postgres", password="2545", host="localhost")
            cur = conn.cursor()
            cur.execute("SELECT * FROM users")
            users = cur.fetchall()
            
            for user in users:
                if user.card_number == recipient_card_number:
                    recipient = user
                    break
            if recipient:
                recipient.balance += amount
                # self.transactions.append(f'Sent {amount} to user with card number {recipient.card_number}')
                # recipient.transactions.append(f'Received {amount} from user with card number {self.card_number}')

                # Обновляем баланс текущего пользователя в базе данных
                conn = psycopg2.connect(database="kursach", user="postgres", password="2545", host="localhost")
                cur = conn.cursor()
                cur.execute("UPDATE users SET balance = %s WHERE id = %s", (self.balance, self.id))
                conn.commit()
                cur.close()
                conn.close()

                # Обновляем баланс получателя в базе данных
                conn = psycopg2.connect(database="kursach", user="postgres", password="2545", host="localhost")
                cur = conn.cursor()
                cur.execute("UPDATE users SET balance = %s WHERE id = %s", (recipient.balance, recipient.id))
                conn.commit()
                cur.close()
                conn.close()

                return True
            else:
                self.balance += amount
                return False
        else:
            return False
    
    def view_last_transactions(self):
        try:
            conn = psycopg2.connect(database="kursach", user="postgres", password="2545", host="localhost")
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM transactions WHERE sender='{self.card_number}' OR recipient='{self.card_number}' ORDER BY id DESC LIMIT 10")
            rows = cur.fetchall()
            print(f"Last 10 transactions for user with card number {self.card_number}:")
            for row in rows:
                if row[1] == self.card_number:
                    print(f"Sent {row[3]} to {row[2]} on {row[4]}")
                else:
                    print(f"Received {row[3]} from {row[1]} on {row[4]}")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
import psycopg2

class Banker:
    def __init__(self, id, login, password):
        self.id = id
        self.login = login
        self.password = password
    
    def get_user_balance(self, user_id):
        conn = psycopg2.connect(database="kursach", user="postgres", password="2545", host="localhost")
        cur = conn.cursor()
        cur.execute("SELECT balance FROM users WHERE id = %s", (user_id,))
        balance = cur.fetchone()
        
        cur.close()
        conn.close()
        return balance[0] if balance else None
    
    
    def set_user_balance(self, user_id, amount,operation):
        conn = psycopg2.connect(database="kursach", user="postgres", password="2545", host="localhost")
        cur = conn.cursor()
        if operation == "withdraw":
            cur.execute("UPDATE users SET balance = balance - %s WHERE id = %s", (amount,user_id))
        else:
            cur.execute("UPDATE users SET balance = balance + %s WHERE id = %s", (amount,user_id))
            
        conn.commit()
        cur.close()
        conn.close()
    
    def transfer_from_user(self, user_id, amount):
        pass
    
    def transfer_to_user(self, user_id, amount):
        pass
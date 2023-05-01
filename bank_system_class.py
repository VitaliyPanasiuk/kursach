import psycopg2

from user_class import User
from banker_class import Banker

class BankSystem:
    def __init__(self, db_name, db_user, db_password, db_host):
        self.conn = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
        )

    def register_user(self, login, password, card_number, balance=0):
        try:
            cur = self.conn.cursor()
            cur.execute(f"INSERT INTO users (login, password, card_number, balance) VALUES ('{login}', '{password}', '{card_number}', {balance})")
            self.conn.commit()
            print("User registered successfully!")
            return password, card_number
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            self.conn.rollback()
        finally:
            if cur is not None:
                cur.close()
        

    def login_user(self, login, password):
        try:
            cur = self.conn.cursor()
            cur.execute(f"SELECT * FROM users WHERE login='{login}' AND password='{password}'")
            user = cur.fetchone()
            if user:
                user_obj = User(user[0], user[1], user[2], user[3], user[4])
                return user_obj
            else:
                print("Invalid login credentials.")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if cur is not None:
                cur.close()
                
    def register_banker(self, login, password):
        try:
            cur = self.conn.cursor()
            cur.execute(f"INSERT INTO bankers (login, password) VALUES ('{login}', '{password}')")
            self.conn.commit()
            print("Ифтлук registered successfully!")
            return login, password
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            self.conn.rollback()
        finally:
            if cur is not None:
                cur.close()

    def login_banker(self, login, password):
        try:
            cur = self.conn.cursor()
            cur.execute(f"SELECT * FROM bankers WHERE login='{login}' AND password='{password}'")
            banker = cur.fetchone()
            if banker:
                banker_obj = Banker(banker[0], banker[1], banker[2])
                return banker_obj
            else:
                print("Invalid login credentials.")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if cur is not None:
                cur.close()

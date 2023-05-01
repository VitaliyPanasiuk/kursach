import psycopg2
from psycopg2 import sql
from psycopg2.extensions import AsIs


def postgre_start():
    base = psycopg2.connect(database="kursach", user="postgres", password="2545", host="localhost")
    cur = base.cursor()
    if base:
        print(f"data base connect success!")
    cur.execute('''CREATE TABLE IF NOT EXISTS bankers
                (
                    id       serial primary key,
                    login    text not null unique,
                    password text not null
                );
                
                CREATE TABLE IF NOT EXISTS banks
                (
                    id         serial primary key,
                    name       text not null unique,
                    requisites text not null unique,
                    balance    real not null
                );
                
                CREATE TABLE IF NOT EXISTS transactions
                (
                    id          serial primary key,
                    sender_id   integer   not null references users,
                    receiver_id integer   not null references users,
                    amount      real      not null,
                    timestamp   timestamp not null
                );
                
                CREATE TABLE IF NOT EXISTS users
                (
                    id          serial primary key,
                    login       text not null unique,
                    password    text not null,
                    card_number text not null unique,
                    balance     real not null
                );
                ''')

    
    
    base.commit()
    cur.close()
    base.close()
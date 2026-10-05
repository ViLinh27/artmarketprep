import streamlit as st
import sqlite3
import pandas as pd

def init_transactions():
    conn = sqlite3.connect('transactions.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS transactions(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_bought TEXT NOT NULL,
            item_price INTEGER NOT NULL,
            payment_method TEXT NOT NULL,
            notes TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_transaction(item_bought, item_price, payment_method:str, notes):
    conn = sqlite3.connect('transactions.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO transactions (item_bought, item_price, payment_method, notes)
        VALUES(?,?,:val,?)
    ''',(item_bought,item_price, payment_method, notes))
    conn.commit()
    conn.close()

def get_transactions():
    conn = sqlite3.connect('transactions.db')
    df = pd.read_sql_query("SELECT * FROM transactions", conn)
    conn.close()
    return df

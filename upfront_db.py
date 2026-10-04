import streamlit as st
import sqlite3
import pandas as pd

def init_upfront():
    conn = sqlite3.connect('upfront.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS upfront(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fee INTEGER NOT NULL,
            due_date TEXT NOT NULL,
            payed BOOL NOT NULL      
        )
    ''')
    conn.commit()
    conn.close()

def add_upfront_cost(fee,due_date, payed):
    conn = sqlite3.connect('upfront.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO upfront (fee,due_date, payed)
        VALUES(?,?,?)
    '''),(fee,due_date,payed)
    conn.commit()
    conn.close()

def get_upfront_costs():
    conn = sqlite3.connect('upfront.db')
    df = pd.read_sql_query("SELECT * FROM upfront", conn)
    conn.close()
    return df

def delete_upfront_cost(fee):
    conn = sqlite3.connect('upfront.db')
    c = conn.cursor()
    c.execute('DELETE FROM upfront WHERE fee = ?',(fee))
    conn.commit()
    conn.close()

def update_upfront_cost(fee, new_upfront_cost):
    conn = sqlite3.connect('upfront.db')
    c = conn.cursor()
    c.execute('UPDATE upfront upfront_cost = ? WHERE fee=?',(fee, new_upfront_cost))
    conn.commit()
    conn.close()


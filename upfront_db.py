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
            fee_desc TEXT NOT NULL,
            due_date TEXT NOT NULL,
            payed TEXT NOT NULL      
        )
    ''')
    conn.commit()
    conn.close()

def add_upfront_cost(fee,fee_desc, due_date, payed):
    conn = sqlite3.connect('upfront.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO upfront (fee, fee_desc, due_date, payed)
        VALUES(?,?,?,?)
    ''',(fee,fee_desc, due_date,"True" if payed else "False"))
    conn.commit()
    conn.close()

def get_upfront_costs():
    conn = sqlite3.connect('upfront.db')
    df = pd.read_sql_query("SELECT * FROM upfront", conn)
    conn.close()
    return df

def delete_upfront_cost(fee_desc):
    conn = sqlite3.connect('upfront.db')
    c = conn.cursor()
    c.execute('DELETE FROM upfront WHERE fee_desc = ?',(fee_desc))
    conn.commit()
    conn.close()

def update_fee_status(fee_desc):
    conn = sqlite3.connect('upfront.db')
    c = conn.cursor()
    c.execute('UPDATE upfront SET payed = CASE WHEN payed ="True" THEN "False" ELSE "True" END WHERE fee_desc=?', (fee_desc,))
    conn.commit()
    conn.close()


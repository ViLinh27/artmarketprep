import streamlit as st
import sqlite3
import pandas as pd

def init_profits_db():
    conn = sqlite3.connect('profits_overtime.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS profits_overtime (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            market_name TEXT NOT NULL,
            upfront_costs INTEGER NOT NULL,
            sales_total INTEGER NOT NULL,
            profits INTEGER NOT NULL,
            notes TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_profits(market_name, upfront_costs, sales_total, profits, notes):
    conn = sqlite3.connect('profits_overtime.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO profits_overtime (market_name, upfront_costs, sales_total, profits, notes)
        VALUES (?,?,?,?,?)
    ''', (market_name, upfront_costs, sales_total, profits , notes))
    conn.commit()
    conn.close()

def get_profits_overtime():
    conn = sqlite3.connect('profits_overtime.db')
    df = pd.read_sql_query("SELECT * FROM profits_overtime",conn)
    conn.close()
    return df

def delete_profits(market_name):
    conn = sqlite3.connect('profits_overtime.db')
    c = conn.cursor()
    c.execute('DELETE FROM profits_overtime WHERE market_name = ?', (market_name,))
    conn.commit()
    conn.close()

